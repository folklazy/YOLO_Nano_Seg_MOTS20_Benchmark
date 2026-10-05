"""Generate Nano docs/plots once from validated CSV and inspected qualitative review."""
from pathlib import Path
import csv,json,re,hashlib,itertools,datetime
ROOT=Path(__file__).resolve().parents[2];EXP=Path(__file__).resolve().parents[1];MASTER=ROOT/'YOLO_Instance_Segmentation_MOTS20_Scaling_Study'
def rows(p):return list(csv.DictReader(p.open()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def fmt(k,v):
 if k in ['model','family','checkpoint','sequence']:return str(v)
 if k in ['parameters','loaded_parameters']:return f'{int(v):,}'
 return f"{float(v):.{3 if k in ['inference_ms_mean','pipeline_ms_mean','fps','gflops'] else 2 if k in ['peak_allocated_vram_mib','checkpoint_mb'] else 6}f}"
COLS=list(zip('model mask_map50_95 ap50 ap75 precision recall f1 tp_iou_mean tp_dice_mean inference_ms_mean pipeline_ms_mean fps peak_allocated_vram_mib parameters gflops checkpoint_mb'.split(),['Model','Mask mAP50-95','AP50','AP75','Precision','Recall','F1','TP-only IoU','TP-only Dice','Inference ms','Pipeline ms','FPS','Peak VRAM MiB','Params','GFLOPs','Checkpoint MB']))
def table(data,cols):return '| '+' | '.join(h for k,h in cols)+' |\n| '+' | '.join('---' for _ in cols)+' |\n'+''.join('| '+' | '.join(fmt(k,r[k]) for k,h in cols)+' |\n' for r in data)
def render(name,sections):
 t=(EXP/'configs/report_templates'/f'TIER_{name}_TEMPLATE.md').read_text();heads=re.findall(r'^## (.+)$',t,re.M)
 assert set(heads)==set(sections),(name,set(heads)^set(sections))
 s=t.splitlines()[0].replace('{{TIER}}','Nano (N)' if name!='RESULTS_SUMMARY_TH' else 'Nano')+'\n\n'+'\n\n'.join('## '+h+'\n\n'+sections[h] for h in heads)+'\n'
 (EXP/(name+'.md')).write_text(s)
def main():
 assert json.loads((EXP/'manifests/final_integrity.json').read_text())['status']=='PASS'
 review=json.loads((EXP/'manifests/QUALITATIVE_REVIEW.json').read_text());assert review['inspected_cases']==4 and review['status']=='PASS'
 data=rows(EXP/'metrics/TIER_RESULTS.csv');seq=rows(EXP/'metrics/PER_SEQUENCE_RESULTS.csv');assert len(data)==3
 guard={p.name:sha(p) for p in (EXP/'metrics').glob('*.csv')}
 winner=lambda k,low=False:(min if low else max)(data,key=lambda r:float(r[k]))
 a=winner('mask_map50_95');f=winner('inference_ms_mean',True);p=winner('pipeline_ms_mean',True);v=winner('peak_allocated_vram_mib',True)
 categories=[('Mask mAP50-95','mask_map50_95',False,''),('AP75','ap75',False,''),('Recall','recall',False,''),('Inference speed','inference_ms_mean',True,' ms'),('Pipeline speed','pipeline_ms_mean',True,' ms'),('VRAM','peak_allocated_vram_mib',True,' MiB')]
 winners='| ด้าน | Model | Result |\n|---|---|---|\n'+''.join(f"| {title} | {winner(k,low)['model']} | {fmt(k,winner(k,low)[k])}{unit} |\n" for title,k,low,unit in categories)
 bullets=[f"ทดสอบ {', '.join(r['model'] for r in data)} สำหรับ Person instance segmentation",'MOTS20 2,862 frames / 26,894 Person GT instances รายเฟรม; pretrained / no fine-tuning',f"Accuracy สูงสุด: {a['model']} mAP50-95 {fmt('mask_map50_95',a['mask_map50_95'])}",f"Inference เร็วสุด: {f['model']} {fmt('inference_ms_mean',f['inference_ms_mean'])} ms",f"Pipeline เร็วสุด/FPS สูงสุด: {p['model']} {fmt('pipeline_ms_mean',p['pipeline_ms_mean'])} ms / {fmt('fps',p['fps'])} FPS",f"Peak allocated VRAM ต่ำสุด: {v['model']} {fmt('peak_allocated_vram_mib',v['peak_allocated_vram_mib'])} MiB",review['main_tradeoff']]
 interpretation='[canonical CSV](metrics/TIER_RESULTS.csv) / [REPORT](REPORT.md) เป็นแหล่ง AP50 และ TP-only IoU/Dice ที่ไม่แสดงในตารางย่อ; TP-only quality ใช้เฉพาะคู่ที่ผ่าน matching และอาจเป็น GT คนละชุด\n\n'+'\n\n'.join('### '+r['model']+'\n\n'+review['model_interpretation'][r['model']] for r in data)
 compact_cols=[COLS[i] for i in [0,1,3,5,9,10,11,12]]
 render('RESULTS_SUMMARY_TH',{'สรุปใน 1 นาที':'\n'.join('- '+b for b in bullets),'ผลลัพธ์หลัก':table(data,compact_cols),'สรุปผลจากตาราง':interpretation,'Winner ของแต่ละด้าน':winners,'สิ่งที่ตัวเลขบอกเรา':'\n'.join('- '+x for x in review['numeric_findings']),'Trade-off หลัก':'### Accuracy vs Speed\n\n'+review['accuracy_speed']+'\n\n### Accuracy vs Memory\n\n'+review['accuracy_memory'],'ข้อควรระวังในการตีความ':'ไม่มีการทดสอบ statistical significance; MOTS20 ไม่ใช่ผลทดสอบ CCTV robustness ขั้นสุดท้าย Pipeline ไม่รวม RLE preparation และ disk I/O; VRAM เป็น peak allocated ของ benchmark การเลือก GT ที่ match กระทบ TP-only quality และภาพต่อเนื่องไม่ใช่ independent samples','ข้อมูลสำหรับนำไปรวมต่อ':review['cross_tier']+'\n\n[TIER_RESULTS.csv](metrics/TIER_RESULTS.csv) · [REPORT.md](REPORT.md) · [Visual analysis](PRESENTATION_SUMMARY_TH.md) · [Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)'})
 presentation=review['presentation_markdown'];assert presentation.startswith('# Nano (N) — Visual and Qualitative Analysis\n');(EXP/'PRESENTATION_SUMMARY_TH.md').write_text(presentation)
 nav=re.search(r'## Study Navigation\n\n(.+)',(MASTER/'templates/TIER_README_TEMPLATE.md').read_text()).group(1)
 modeltable='| Family | Model | Tier |\n|---|---|---|\n'+''.join(f"| {r['family']} | {r['model']} | Nano (N) |\n" for r in data)
 render('README',{'Overview':'Pretrained Person instance segmentation on MOTS20 using the frozen study protocol. Three Nano checkpoints; no training, fine-tuning or adaptation. Four same-frame saved-prediction cases are in PRESENTATION_SUMMARY_TH.md.','Models':modeltable,'Experimental Status':f"COMPLETE / PASS WITH WARNINGS; run `{data[0]['run_id']}`. Three models × 2,862 frames; nine accepted clean timing rounds; no automatic master synthesis.",'Main Result':table(data,[COLS[i] for i in [0,1,5,6,9,10,11,12]]),'Reports':'\n'.join(f'- [{n}]({n})' for n in ['PRESENTATION_SUMMARY_TH.md','RESULTS_SUMMARY_TH.md','REPORT.md','EXPERIMENT_PROTOCOL.md']),'Study Navigation':nav,'Reproducibility':'[configs](configs/) · [metrics](metrics/) · [manifests](manifests/) · [src](src/)'})
 integrity=json.loads((EXP/'manifests/final_integrity.json').read_text());checks='| Item | Status |\n|---|---|\n'+''.join('| '+x['item']+' | '+x['status']+' |\n' for x in integrity['checks'])
 sequence='\n'.join(f"- {r['model']} / {r['sequence']}: mAP {float(r['mask_map50_95']):.6f}, Recall {float(r['recall']):.6f}" for r in seq)
 fullwinner=winners.replace('ด้าน','Category').replace('Result','Value');fullwinner+=f"| Highest FPS | {p['model']} | {fmt('fps',p['fps'])} |\n"
 render('REPORT',{'1. Experiment Status':f"COMPLETE / PASS WITH WARNINGS. Scientific integrity PASS; run `{data[0]['run_id']}`.",'2. Models Tested':table(data,[('family','Family'),('model','Model'),('parameters','Parameters'),('gflops','GFLOPs'),('checkpoint_mb','Checkpoint MB')]),'3. Protocol Compatibility':'Dataset/environment/framework compatible with the frozen Largest baseline. See [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) and [Master methodology](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/main/METHODOLOGY_REFERENCE.md).\n\n'+checks,'4. Overall Results':table(data,COLS),'5. Tier Winners':fullwinner,'6. Key Findings':'\n'.join('- '+x for x in review['numeric_findings']),'7. Per-sequence Observations':sequence+'\n\n'+review['sequence_findings'],'8. Efficiency and Resource Observations':review['timing_findings']+'\n\n[MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv) retains loaded/fused parameters, GFLOPs and load time. Reserved VRAM remains in accepted timing source.','9. Warnings and Anomalies':review['warnings'],'10. Limitations':'Frame-level segmentation, not MOTS tracking. TP-only quality is conditional on matching; selected qualitative cases are diagnostic. No statistical-significance test, causal architecture claim, weighted score or final CCTV superiority.','11. Reproducibility and Source Artifacts':'Canonical [TIER_RESULTS](metrics/TIER_RESULTS.csv), [PER_SEQUENCE_RESULTS](metrics/PER_SEQUENCE_RESULTS.csv), [TIMING_SUMMARY](metrics/TIMING_SUMMARY.csv), [MODEL_COMPLEXITY](metrics/MODEL_COMPLEXITY.csv), [PREFLIGHT_MAXDET](metrics/PREFLIGHT_MAXDET.csv).\n\n[STANDARDIZATION](manifests/STANDARDIZATION.json), [final integrity](manifests/final_integrity.json), [public environment](manifests/environment_public.json). Saved lossless predictions and detailed telemetry remain local/ignored. See [canonical plots](outputs/plots/INDEX.md).','12. Relation to Full Scaling Study':'Nano only; no automatic final 17-model synthesis. [Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study). STOP after Nano.','Qualitative Analysis':'Four inspected comparisons from saved predictions are discussed in [PRESENTATION_SUMMARY_TH.md](PRESENTATION_SUMMARY_TH.md). [CASE_SELECTION](outputs/visualizations/qualitative/CASE_SELECTION.md) documents balanced selection and limitations. No inference was run for documentation.'})
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 out=EXP/'outputs/plots';out.mkdir(parents=True,exist_ok=True);colors=['#2563eb','#ea580c','#9333ea'];names=[r['model'] for r in data]
 def bar(name,key,ylabel):
  target=out/name;assert not target.exists();fig,ax=plt.subplots(figsize=(8,4.8));vals=[float(r[key]) for r in data];ax.bar(names,vals,color=colors);ax.set_ylabel(ylabel);ax.set_title('Nano (N) — MOTS20');ax.set_ylim(0,max(vals)*1.18)
  for j,r in enumerate(data):ax.text(j,vals[j],fmt(key,r[key]),ha='center',va='bottom',fontsize=9)
  fig.tight_layout();fig.savefig(target,dpi=160);plt.close(fig)
 bar('01_mask_map50_95.png','mask_map50_95','Mask mAP50-95 (0–1)');bar('03_inference_latency.png','inference_ms_mean','Inference mean (ms/frame)');bar('04_pipeline_fps.png','fps','Pipeline FPS (excludes RLE / disk I/O)');bar('05_peak_vram.png','peak_allocated_vram_mib','Peak allocated VRAM (MiB)')
 fig,ax=plt.subplots(figsize=(8,4.8));xs=range(3)
 for offset,key,col in [(-.2,'ap50','#2563eb'),(.2,'ap75','#ea580c')]:ax.bar([j+offset for j in xs],[float(r[key]) for r in data],width=.4,label=key.upper(),color=col)
 ax.set_xticks(list(xs),names);ax.set_ylim(0,1);ax.set_ylabel('AP (0–1)');ax.set_title('Nano (N) — MOTS20');ax.legend();fig.tight_layout();fig.savefig(out/'02_ap50_ap75.png',dpi=160);plt.close(fig)
 fig,ax=plt.subplots(figsize=(8,5.2))
 for j,r in enumerate(data):ax.scatter(float(r['inference_ms_mean']),float(r['mask_map50_95']),color=colors[j],label=r['model'],s=80)
 ax.set_xlabel('Inference mean (ms/frame)');ax.set_ylabel('Mask mAP50-95 (0–1)');ax.set_title('Nano (N) — MOTS20');ax.legend();ax.grid(alpha=.2);fig.tight_layout();fig.savefig(out/'06_accuracy_vs_latency.png',dpi=160);plt.close(fig)
 plots=sorted(out.glob('0*.png'));(out/'INDEX.md').write_text('# Canonical Nano plots\n\nSource: [TIER_RESULTS.csv](../../metrics/TIER_RESULTS.csv).\n\n'+'\n'.join(f'- [{p.name}]({p.name})' for p in plots)+'\n')
 write(EXP/'manifests/PLOT_PROVENANCE.json',{'source_sha256':sha(EXP/'metrics/TIER_RESULTS.csv'),'generator_sha256':sha(Path(__file__)),'outputs':{str(p.relative_to(EXP)):sha(p) for p in plots}})
 assert guard=={p.name:sha(p) for p in (EXP/'metrics').glob('*.csv')}
 print('Nano reports and six canonical plots generated from saved data and inspected review.')
if __name__=='__main__':main()
