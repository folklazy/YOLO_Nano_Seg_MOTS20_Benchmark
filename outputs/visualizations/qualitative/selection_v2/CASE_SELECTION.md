# Nano — qualitative case selection v2

คัดจาก 12 frozen visualization frames โดยตรวจ per-frame metrics, original/GT และ saved RLE ที่ confidence ≥0.25 / mask matching IoU ≥0.50 ตาม evaluator/ignore policy เดิม ไม่รัน inference

1 shared anchor + 3 cases ตามพฤติกรรมของ tier ไม่บังคับภาพทั้งหมดตรงกันระหว่าง tier; ภายใน case ใช้เฟรมเต็มเดียวกันทุกโมเดล ROI เป็นภาพเสริม ไม่ซ่อน full-frame errors

| Case | Sequence / frame | Why selected / decision use | Source comparison |
|---|---|---|---|
| 1 | MOTS20-11 / 000001 | tier diagnostic: equal TP for two models, unequal FP and different GT; ใช้เทียบการเก็บ GT 2028 กับภาระ extra masks: YOLO26n/YOLO11n มี TP 8 และ FN ชุดเดียวกัน แต่ YOLO11n มี FP บน GT 2006 ที่มีคู่แล้ว; YOLOv8n มี TP 7 | new composite from saved predictions |
| 2 | MOTS20-09 / 000263 | shared anchor: common failure; ใช้แสดงข้อจำกัดร่วมและภาระตรวจ unmatched output เมื่อคนซ้อนกัน ไม่ใช่ case ที่ counts ให้ผู้ชนะชัด | reuse existing image |
| 3 | MOTS20-02 / 000300 | trade-off: added valid GT and more unmatched outputs; ช่วยเลือกตาม priority: YOLOv8n เก็บ GT เพิ่ม แต่ FP มากขึ้น; สอดคล้องในทิศทางกับ Recall สูง/Precision ต่ำใน dataset | reuse existing image |
| 4 | MOTS20-09 / 000001 | similar coverage but extra masks on already matched GT; เป็น pain point ด้าน extra-instance output: ทุกโมเดลมี TP 6 / FN 0 แต่ YOLO26n มี mask เพิ่มทับ GT 2001 และ YOLOv8n มีสอง mask เพิ่มทับ GT 2019; YOLO11n ไม่มี FP | reuse existing image |

## ทำไมบางภาพยังตรงกับ tier อื่น

Case 2 (09/263) ใช้ร่วมเพื่อเทียบ FN/FP บน GT ชุดเดียวกัน กรณีอื่นซ้ำได้เมื่อ error เดียวกันช่วยตรวจคนละโมเดล: 05/419 ใช้ L/M ตรวจ GT 2002; 02/1 ใช้ L/M ตรวจ equal counts และ GT ต่างชุด; 02/600 ใช้ Largest/Small ตรวจกรณีสวนอันดับ; 02/300 ใช้ Small/Nano ตรวจ TP–FP trade-off; 11/1 ใช้ L/N แต่ L ตรวจ GT 2016 ส่วน N ตรวจ GT 2028 และ extra mask; 11/450 ใช้ Largest/Medium ตรวจ coverage เท่ากันกับ extra output ของคนละชุดโมเดล ไม่ใช้จำนวนภาพซ้ำเป็นหลักฐานอิสระเพิ่ม

## การแทน case เดิม

เดิม Case 1 (02/600) มี GT trade-off จริง แต่ 11/1 เพิ่มบริบทและแยก output ของคู่ TP เท่ากัน; Case 3/4 ยังคง GT–FP trade-off และ extra masks บนคนจริงไว้ ภาพ/หลักฐานเก่ายังคงเดิมเพื่อ audit; presentation เก่าเก็บใน reports/archive

## ขอบเขต

ทั้งห้า tier มี 20 case slots แต่ใช้ original frames ต่างกัน 10 เฟรม (เดิม 6) ชุดใหม่มี MOTS20-11 และยังมี common failure / counterexample ไม่เลือกเฉพาะ frame ที่ accuracy leader ชนะ ทั้งนี้ pool 12 เฟรมไม่แทน dataset; ไม่อ้างว่าเป็นเฟรมที่ต่างที่สุดใน 2,862 เฟรม ไม่ใช้ภาพวัด latency/VRAM หรือ statistical significance

[Candidate pool](CANDIDATE_POOL.json) · [Case evidence](CASE_EVIDENCE.json) · [Focus evidence](FOCUS_EVIDENCE.json) · [Decision audit](CASE_DECISION_AUDIT.json) · [Active selection](../../../../manifests/QUALITATIVE_SELECTION.json)
