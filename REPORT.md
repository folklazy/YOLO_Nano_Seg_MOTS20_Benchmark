# Nano (N) การทดสอบ YOLO Instance Segmentation — MOTS20

## 1. สถานะการทดลอง

PASS WITH WARNINGS

- โมเดลที่เสร็จแล้ว: 3/3
- จำนวนเฟรม: 2,862 ต่อโมเดล; Person GT รายเฟรม: 26,894 instances
- รหัสรอบทดลอง: `benchmark-20261005T083307Z`

## 2. โมเดลที่ทดสอบ

| ตระกูล | โมเดล | จำนวนพารามิเตอร์ | GFLOPs | Checkpoint (MB) |
| --- | --- | --- | --- | --- |
| YOLO26 | YOLO26n-Seg | 3,126,280 | 10.630 | 6.72 |
| YOLO11 | YOLO11n-Seg | 2,876,848 | 9.959 | 6.18 |
| YOLOv8 | YOLOv8n-Seg | 3,409,968 | 12.141 | 7.07 |

## 3. ความสอดคล้องกับโพรโทคอล

| รายการ | สถานะ |
|---|---|
| ข้อมูล | PASS |
| ตัวประเมิน | PASS |
| การเตรียมภาพ | PASS |
| ขนาดภาพเข้าโมเดล | PASS |
| ความละเอียดเชิงตัวเลข | PASS |
| ค่าเกณฑ์ | PASS |
| maxDet | PASS |
| วิธีวัดเวลา | PASS |
| สภาพแวดล้อม | PASS |

ความสอดคล้องของข้อมูล: PASS

ความสอดคล้องของการเตรียมภาพ: PASS

[วิธีทดลองร่วม](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/main/METHODOLOGY_REFERENCE.md) · [โพรโทคอลการทดลอง](EXPERIMENT_PROTOCOL.md) · [หลักฐานการกำหนดมาตรฐาน](manifests/STANDARDIZATION.json)

ผลตรวจความถูกต้องทางวิทยาศาสตร์: PASS; รายการตรวจละเอียดทั้ง 15 ข้อยังคงอยู่ใน [หลักฐานตรวจรอบทดลอง](manifests/final_integrity.json)

## 4. ผลลัพธ์รวม

| โมเดล | Mask mAP50-95 | AP50 | AP75 | Precision | Recall | F1 | TP-only IoU | TP-only Dice | Inference (ms) | Pipeline (ms) | FPS | Peak allocated VRAM (MiB) | จำนวนพารามิเตอร์ | GFLOPs | Checkpoint (MB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO26n-Seg | 0.472698 | 0.774367 | 0.506766 | 0.901850 | 0.687068 | 0.779942 | 0.810328 | 0.891429 | 13.042 | 82.390 | 12.137 | 1043.13 | 3,126,280 | 10.630 | 6.72 |
| YOLO11n-Seg | 0.431929 | 0.757732 | 0.450826 | 0.866571 | 0.693798 | 0.770619 | 0.785422 | 0.875606 | 11.745 | 97.441 | 10.263 | 1030.00 | 2,876,848 | 9.959 | 6.18 |
| YOLOv8n-Seg | 0.423062 | 0.750024 | 0.439115 | 0.826411 | 0.696921 | 0.756163 | 0.781325 | 0.872824 | 9.045 | 95.683 | 10.451 | 1117.09 | 3,409,968 | 12.141 | 7.07 |

## 5. ผู้ชนะในแต่ละด้าน

| ด้าน | โมเดล | ผลลัพธ์ |
| --- | --- | --- |
| Mask mAP50-95 สูงสุด | YOLO26n-Seg | 0.472698 |
| AP75 สูงสุด | YOLO26n-Seg | 0.506766 |
| Recall สูงสุด | YOLOv8n-Seg | 0.696921 |
| Inference เร็วสุด | YOLOv8n-Seg | 9.045 |
| Pipeline เร็วสุด | YOLO26n-Seg | 82.390 |
| FPS สูงสุด | YOLO26n-Seg | 12.137 |
| VRAM ต่ำสุด | YOLO11n-Seg | 1030.00 |

Inference / pipeline เป็น ms/เฟรม; FPS คำนวณจากค่าเฉลี่ย pipeline; VRAM เป็น peak allocated MiB.

## 6. ข้อค้นพบสำคัญ

- ข้อสังเกต: YOLO26n-Seg มี Mask mAP50-95 สูงสุด 0.472698; ห่างอันดับถัดไป 0.040768 บนสเกล 0–1
- ข้อสังเกต: YOLO26n-Seg นำ AP75; YOLOv8n-Seg นำ Recall; YOLO26n มี Recall ต่ำสุด แม้นำ mAP/AP75 จึงมีข้อแลกเปลี่ยนด้านความครบถ้วน
- ข้อสังเกต: YOLOv8n-Seg มี inference เร็วสุด; YOLO26n-Seg มี pipeline เร็วสุดและ FPS สูงสุด; YOLO11n-Seg มี VRAM ต่ำสุด
- คู่ mAP ใกล้ที่สุด: YOLO11n-Seg / YOLOv8n-Seg ต่าง 0.008867; เป็นความใกล้เชิงพรรณนา ไม่ใช่ผลทดสอบนัยสำคัญทางสถิติ
- การตีความ: แยกความแม่นยำความครบถ้วนเวลา forward เวลา pipeline และหน่วยความจำไม่มีคะแนนรวมถ่วงน้ำหนักจำนวนพารามิเตอร์หรือ GFLOPs ไม่กำหนดอันดับเวลา/VRAM โดยตรง

## 7. ข้อสังเกตรายลำดับภาพ

- YOLO26n-Seg: Mask mAP50-95 สูงสุดที่ MOTS20-11 (0.541629); ต่ำสุดที่ MOTS20-02 (0.335752)
- YOLO11n-Seg: Mask mAP50-95 สูงสุดที่ MOTS20-11 (0.501796); ต่ำสุดที่ MOTS20-02 (0.290888)
- YOLOv8n-Seg: Mask mAP50-95 สูงสุดที่ MOTS20-11 (0.495783); ต่ำสุดที่ MOTS20-02 (0.271786)
- ลำดับ mAP ที่ต่างจากผลรวม: ไม่มีในทั้งสี่ลำดับภาพ

AP รวมคำนวณจากข้อมูลทั้งหมด ไม่ใช่ค่าเฉลี่ย AP รายลำดับภาพ ดูค่าครบใน [PER_SEQUENCE_RESULTS.csv](metrics/PER_SEQUENCE_RESULTS.csv)

## 8. ประสิทธิภาพและการใช้ทรัพยากร

- คู่ที่ใกล้ที่สุดด้านค่าเฉลี่ย inference: YOLO26n-Seg / YOLO11n-Seg ต่าง 1.297 ms; ไม่ได้ทดสอบนัยสำคัญทางสถิติ
- คู่ที่ใกล้ที่สุดด้านค่าเฉลี่ย pipeline: YOLO11n-Seg / YOLOv8n-Seg ต่าง 1.758 ms; ไม่ได้ทดสอบนัยสำคัญทางสถิติ

YOLO11n-Seg ใช้ peak allocated VRAM ต่ำสุดจำนวนพารามิเตอร์ก่อน/หลัง fusion, GFLOPs และเวลาโหลดแยกเก็บใน [MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv) ส่วน peak reserved VRAM อยู่ใน [แหล่งวัดเวลา](timing/benchmark-20261005T083307Z/clean_repetition/summary.csv) เวลาเตรียม RLE แยก: yolo26n-seg.pt: 336.791 ms; yolo11n-seg.pt: 409.860 ms; yolov8n-seg.pt: 405.991 ms.

ใช้ 3 รอบที่ไม่ถูกรบกวนต่อโมเดล รอบละ 100 เฟรมหลัง 10 warmups และ synchronize CUDA ตามขอบเขต stage ค่า pipeline รวม preprocessing, inference และ postprocessing ไม่รวมการเตรียม RLE และการอ่านเขียนดิสก์ FPS จึงไม่ใช่อัตราการบันทึก mask ครบกระบวนการและไม่บวก Ultralytics-inclusive diagnostic ซ้ำ

ค่าเฉลี่ย postprocessing: YOLO26n-Seg: 67.627 ms; YOLO11n-Seg: 83.942 ms; YOLOv8n-Seg: 84.911 ms

## 9. คำเตือนและข้อสังเกตผิดปกติ

พบคำเตือน CPU NNPACK ระหว่างเตรียมรอบและตรวจความซับซ้อนโมเดล ความถูกต้องทางวิทยาศาสตร์ผ่านและผลเวลาหลักมี 9 รอบที่ไม่ถูกรบกวน ไม่เปลี่ยน package หรือค่าที่วัดเพื่อซ่อนคำเตือน maxDet100 ไม่ผ่านอย่างน้อยหนึ่งค่า AP ทุกโมเดล ส่วน 200/300/1000 ผ่านทั้งหมด จึงคง AP maxDet=200 เดิม

Pipeline ไม่รวมการเตรียม RLE และการอ่านเขียนดิสก์จึงไม่ใช่เวลา/อัตราประมวลผลครบกระบวนการสำหรับการบันทึก mask หรือระบบ CCTV การปรับเอกสารครั้งนี้ไม่รัน inference ใหม่และไม่เปลี่ยนค่าที่วัด

## 10. ข้อจำกัด

ผลนี้เป็น Person instance segmentation รายเฟรมบน MOTS20 ไม่ใช่ MOTS tracking; 26,894 GT instances เป็น annotation รายเฟรมไม่ใช่จำนวนคนไม่ซ้ำ TP-only IoU/Dice พิจารณาเฉพาะคู่ที่ จับคู่ ได้ ภาพวิดีโอต่อเนื่องสัมพันธ์กันและไม่มีการทดสอบนัยสำคัญทางสถิติตัวอย่างเชิงคุณภาพไม่แทนตัวชี้วัดระดับชุดข้อมูลผลยังไม่ยืนยันภาพพร่า, แสงน้อย, มุมกล้อง, ระดับ occlusion หรือความเหมาะสมต่อการนำไปใช้งานจึงใช้เพื่อเลือกตัวเลือกสำหรับการทดสอบต่อการประเมินความทนทานต่อ CCTV เท่านั้น ไม่มีคะแนนรวมถ่วงน้ำหนักหรือข้อสรุปเชิงสาเหตุจากโครงสร้างโมเดล

## 11. หลักฐานสำหรับตรวจสอบซ้ำ

- [TIER_RESULTS.csv](metrics/TIER_RESULTS.csv)
- [PER_SEQUENCE_RESULTS.csv](metrics/PER_SEQUENCE_RESULTS.csv)
- [TIMING_SUMMARY.csv](metrics/TIMING_SUMMARY.csv)
- [MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv)
- [PREFLIGHT_MAXDET.csv](metrics/PREFLIGHT_MAXDET.csv)

[แหล่งที่มาและค่า hash](manifests/STANDARDIZATION.json) · [โพรโทคอล](EXPERIMENT_PROTOCOL.md) · [รายการกราฟ](outputs/plots/INDEX.md) · [บันทึกย้อนหลัง](reports/archive/)

prediction แบบ RLE ที่ไม่สูญเสียข้อมูลและบันทึกการวัดเวลาละเอียดเก็บในเครื่องตามรหัสรอบทดลอง หลักฐานต้นทางคงเดิม; การปรับภาษานี้ไม่คำนวณค่าตัวชี้วัดใหม่และไม่รัน inference

## 12. ความเชื่อมโยงกับการศึกษาทุกขนาด

[การศึกษาหลัก](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study) — รายงานนี้กล่าวถึงขนาด Nano (N) เท่านั้นผลรวม 17 โมเดลยังรอคำสั่งจากผู้ใช้ แม้การทดลองทั้งห้าขนาดเสร็จแล้ว การปรับเอกสารไม่เริ่ม benchmark หรือการสังเคราะห์ผลใหม่

## การวิเคราะห์เชิงคุณภาพ

ภาพเปรียบเทียบเฟรมเดียวกัน 4 กรณีจาก prediction ที่บันทึกไว้ พร้อมข้อผิดพลาดที่พบและการตีความ อยู่ใน [PRESENTATION_SUMMARY_TH.md](PRESENTATION_SUMMARY_TH.md) ดู [เหตุผลเลือกกรณีปัจจุบัน](outputs/visualizations/qualitative/selection_v2/CASE_SELECTION.md) และ [ตัวชี้ชุดหลักฐาน](manifests/QUALITATIVE_SELECTION.json) รายงานเทคนิคนี้เชื่อมไปยังการวิเคราะห์ภาพเพื่อไม่เล่าเนื้อหาซ้ำ
