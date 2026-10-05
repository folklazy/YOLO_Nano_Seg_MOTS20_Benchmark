"""Read-only final Nano checks; writes only a validation manifest after PASS."""
from pathlib import Path
import csv,json,hashlib,re,math,datetime
from PIL import Image
ROOT=Path(__file__).resolve().parents[2];EXP=Path(__file__).resolve().parents[1];MASTER=ROOT/'YOLO_Instance_Segmentation_MOTS20_Scaling_Study'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open()))
def read(p):return json.loads(p.read_text())
def text(p):return re.sub(r'<!--.*?-->','',p.read_text(),flags=re.S)
def main():
 final=read(EXP/'manifests/final_integrity.json');assert final['status']=='PASS' and len(final['checks'])==15 and all(x['status']=='PASS' for x in final['checks'])
 data=rows(EXP/'metrics/TIER_RESULTS.csv');assert [r['checkpoint'] for r in data]==['yolo26n-seg.pt','yolo11n-seg.pt','yolov8n-seg.pt']
 assert all(r['frames']=='2862' and r['gt_instances']=='26894' and r['ap_maxdet']=='200' for r in data)
 schemas=read(MASTER/'schemas.json')
 for name,count in [('TIER_RESULTS',3),('PER_SEQUENCE_RESULTS',12),('TIMING_SUMMARY',18),('MODEL_COMPLEXITY',3),('PREFLIGHT_MAXDET',12)]:
  rr=rows(EXP/'metrics'/f'{name}.csv');assert len(rr)==count
  fields=schemas['PREFLIGHT_MAXDET'] if name=='PREFLIGHT_MAXDET' else schemas['schemas'][name]
  assert list(rr[0])==fields
 for r in rows(EXP/'metrics/TIMING_SUMMARY.csv'):assert r['contamination_status']=='CLEAN' and r['repetitions']=='3' and r['measured_frames']=='300'
 for path,h in read(EXP/'manifests/OTHER_TIERS_GUARD.json').items():assert sha(ROOT/path)==h,path
 std=read(EXP/'manifests/STANDARDIZATION.json')
 for path,h in std['source_artifact_sha256'].items():assert sha(EXP/path)==h,path
 ev=read(EXP/'outputs/visualizations/qualitative/CASE_EVIDENCE.json');assert ev['inference_rerun'] is False and ev['benchmark_values_changed'] is False and len(ev['cases'])==4
 pool={(x['sequence'],x['frame']) for x in read(EXP/'manifests/visualization_frames.json')}
 for i,c in enumerate(ev['cases'],1):
  assert (c['sequence'],c['frame']) in pool
  assert sha(ROOT/c['image'])==c['image_sha256']
  assert sha((ROOT/c['image']).parent.parent/'gt/gt.txt')==c['gt_sha256']
  im=EXP/f'outputs/visualizations/qualitative/case_{i:02d}_comparison.png';assert sha(im)==c['comparison_sha256']
  with Image.open(ROOT/c['image']) as original:h=round(original.height*960/original.width)+60
  with Image.open(im) as composite:assert composite.size==(1920,h*4);composite.verify()
  assert [m['model'] for m in c['models']]==[r['model'] for r in data]
  for model,r in zip(c['models'],data):
   assert sha(ROOT/model['prediction_path'])==model['prediction_sha256']
   f=next(x for x in rows(EXP/f"metrics/{ev['run_id']}/per_frame/{r['checkpoint']}.csv") if x['sequence']==c['sequence'] and int(x['frame'])==c['frame'])
   for k in ['tp','fp','fn','ignored_predictions']:assert model[k]==int(f[k])
 fields={'Mask mAP50-95':'mask_map50_95','AP50':'ap50','AP75':'ap75','Precision':'precision','Recall':'recall','F1':'f1','TP-only IoU':'tp_iou_mean','TP-only Dice':'tp_dice_mean','Inference ms':'inference_ms_mean','Pipeline ms':'pipeline_ms_mean','FPS':'fps','Peak VRAM MiB':'peak_allocated_vram_mib','Parameters':'parameters','Params':'parameters','GFLOPs':'gflops','Checkpoint MB':'checkpoint_mb'}
 count=0
 for name in ['README','REPORT','RESULTS_SUMMARY_TH','PRESENTATION_SUMMARY_TH']:
  s=text(EXP/(name+'.md'));assert '{{' not in s and not re.search(r'(?i)mentor|อาจารย์|สรุปสำหรับคุยกับพี่',s)
  for link in re.findall(r'\]\(([^)]+)\)',s):
   if not link.startswith(('http:','https:','#')):assert (EXP/link.split('#')[0]).exists(),(name,link)
  template=text(EXP/'configs/report_templates'/f'TIER_{name}_TEMPLATE.md')
  actual=re.findall(r'^## .+$',s,re.M);expected=re.findall(r'^## .+$',template,re.M)
  if name=='PRESENTATION_SUMMARY_TH':
   expected=[h for h in expected if not h.startswith('## Case ')]
   assert [h for h in actual if not h.startswith('## Case ')]==expected
   assert len(re.findall(r'^## Case [1-4] — ',s,re.M))==4
   assert s.count('### สิ่งที่เห็นจากภาพ')==s.count('### วิเคราะห์')==s.count('### เชื่อมกับผลเชิงตัวเลข')==4
   assert s.count('### Observation ')==s.count('**Interpretation:**')==4
  else:assert actual==expected,(name,actual,expected)
  header=None
  for line in s.splitlines():
   if not line.startswith('|'):header=None;continue
   values=[v.strip() for v in line.strip('|').split('|')]
   if 'Model' in values and any(x in values for x in ['Mask mAP50-95','Parameters']):header=values;continue
   if header is None or all(re.fullmatch('[-:]+',x) for x in values):continue
   r=next(r for r in data if r['model']==values[header.index('Model')])
   for title,value in zip(header,values):
    if title not in fields:continue
    k=fields[title];expected=f'{int(r[k]):,}' if k=='parameters' else f"{float(r[k]):.{3 if k in ['inference_ms_mean','pipeline_ms_mean','fps','gflops'] else 2 if k in ['peak_allocated_vram_mib','checkpoint_mb'] else 6}f}"
    assert value==expected,(name,title,value,expected);count+=1
 result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','numeric_table_cells_verified':count,'cases':4,'source_hashes':'PASS','local_links':'PASS','template_headings':'PASS','other_tiers_unchanged':True,'measured_values_changed':False,'inference_rerun':False,'document_sha256':{n+'.md':sha(EXP/(n+'.md')) for n in ['README','REPORT','RESULTS_SUMMARY_TH','PRESENTATION_SUMMARY_TH']},'canonical_metrics_sha256':{p.name:sha(p) for p in (EXP/'metrics').glob('*.csv')}}
 (EXP/'manifests/DOCUMENT_VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print('Nano final documentation and source validation PASS:',count,'numeric cells, four real cases.')
if __name__=='__main__':main()
