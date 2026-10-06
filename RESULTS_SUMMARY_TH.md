# สรุปผล Nano YOLO Instance Segmentation

## สรุปใน 1 นาที

- ทดสอบ YOLO26n-Seg, YOLO11n-Seg, YOLOv8n-Seg สำหรับ Person instance segmentation
- MOTS20 2,862 frames / 26,894 Person GT instances รายเฟรม; pretrained / no fine-tuning
- Accuracy สูงสุด: YOLO26n-Seg mAP50-95 0.472698
- Inference เร็วสุด: YOLOv8n-Seg 9.045 ms
- Pipeline เร็วสุด/FPS สูงสุด: YOLO26n-Seg 82.390 ms / 12.137 FPS
- Peak allocated VRAM ต่ำสุด: YOLO11n-Seg 1030.00 MiB
- YOLO26n นำ mAP/AP75 และ pipeline แต่ Recall ต่ำสุด; YOLOv8n นำ Recall/forward; YOLO11n ใช้ VRAM ต่ำสุด

## ผลลัพธ์หลัก

| Model | Mask mAP50-95 | AP75 | Recall | Inference ms | Pipeline ms | FPS | Peak VRAM MiB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO26n-Seg | 0.472698 | 0.506766 | 0.687068 | 13.042 | 82.390 | 12.137 | 1043.13 |
| YOLO11n-Seg | 0.431929 | 0.450826 | 0.693798 | 11.745 | 97.441 | 10.263 | 1030.00 |
| YOLOv8n-Seg | 0.423062 | 0.439115 | 0.696921 | 9.045 | 95.683 | 10.451 | 1117.09 |


## สรุปผลจากตาราง

[canonical CSV](metrics/TIER_RESULTS.csv) / [REPORT](REPORT.md) เป็นแหล่ง AP50 และ TP-only IoU/Dice ที่ไม่แสดงในตารางย่อ; TP-only quality ใช้เฉพาะคู่ที่ผ่าน matching และอาจเป็น GT คนละชุด

### YOLO26n-Seg

นำ AP50 0.774367, AP75 0.506766, mAP50-95 0.472698 และ Precision 0.901850 พร้อม TP-only IoU/Dice 0.810328/0.891429 แต่ Recall 0.687068 (68.71%) ต่ำสุด จึงไม่ควรเรียกว่าเก็บคนครบที่สุด คุณภาพเฉพาะคู่ที่ match ไม่แทน GT ที่พลาด

Forward 13.042 ms ช้าที่สุด แต่ pipeline 82.390 ms เร็วที่สุด ใช้ allocated VRAM 1043.13 MiB สูงกว่า YOLO11n เหมาะเป็น candidate เมื่อเน้น mAP และ pipeline พร้อมตรวจข้อจำกัด Recall ต่อ

### YOLO11n-Seg

mAP 0.431929 และ AP75 0.450826 สูงกว่า YOLOv8n ขณะที่ Recall 0.693798 ต่ำกว่าเล็กน้อย TP-only IoU/Dice 0.785422/0.875606 สูงกว่าเช่นกัน แต่คู่ที่ match อาจเป็น GT คนละชุด ไม่เลือกจาก mAP อย่างเดียว

Peak allocated VRAM 1030.00 MiB ต่ำสุด แม้ forward 11.745 ms เร็วกว่า YOLO26n แต่ pipeline 97.441 ms ช้าสุด จึงเป็น candidate ด้าน memory มากกว่าจะเรียกสมดุลดีที่สุดโดยอัตโนมัติ

### YOLOv8n-Seg

Recall 0.696921 สูงสุดและ forward 9.045 ms เร็วสุด แต่ Precision 0.826411, mAP 0.423062 และ AP75 0.439115 ต่ำสุด การเก็บเพิ่มจึงมี trade-off กับ unmatched predictions และคุณภาพตาม AP

Pipeline 95.683 ms ยังช้ากว่า YOLO26n และ allocated VRAM 1117.09 MiB สูงสุด เหมาะเป็น candidate เมื่อเน้น Recall หรือ forward latency; ผลนี้ไม่พิสูจน์ว่า architecture รุ่นใดดีกว่าทุกเงื่อนไข

## Winner ของแต่ละด้าน

| ด้าน | Model | Result |
|---|---|---|
| Mask mAP50-95 | YOLO26n-Seg | 0.472698 |
| AP75 | YOLO26n-Seg | 0.506766 |
| Recall | YOLOv8n-Seg | 0.696921 |
| Inference speed | YOLOv8n-Seg | 9.045 ms |
| Pipeline speed | YOLO26n-Seg | 82.390 ms |
| VRAM | YOLO11n-Seg | 1030.00 MiB |


## สิ่งที่ตัวเลขบอกเรา

- YOLO26n นำ mAP เหนือ YOLO11n/YOLOv8n ประมาณ 0.040768/0.049636 แต่ Recall ต่ำสุด เป็น accuracy–coverage trade-off
- YOLO11n/YOLOv8n เป็นคู่ mAP ใกล้ที่สุด ต่างประมาณ 0.008867; AP75/Precision นำใน YOLO11n แต่ Recall/forward นำใน YOLOv8n ไม่มี significance test
- YOLOv8n forward เร็วสุด 9.045 ms แต่ YOLO26n pipeline เร็วสุด 82.390 ms / 12.137 FPS เพราะผลรวม stage ที่วัดต่างจาก forward อย่างเดียว
- YOLO11n VRAM ต่ำสุด 1030.00 MiB และ GFLOPs ต่ำสุด แต่ pipeline ช้าที่สุด; complexity ไม่กำหนดอันดับ latency โดยตรง

## Trade-off หลัก

### Accuracy vs Speed

YOLO26n แลก forward ที่ช้ากว่า YOLOv8n ประมาณ 3.997 ms กับ mAP สูงกว่าประมาณ 0.049636 แต่ pipeline กลับเร็วกว่า 13.292 ms ใน protocol นี้ ควรเลือก stage ตามงานจริง; FPS ไม่รวม RLE/disk I/O

### Accuracy vs Memory

YOLO26n เพิ่ม peak allocated ประมาณ 13.13 MiB จาก YOLO11n แลก mAP สูงขึ้นประมาณ 0.040768 ส่วน YOLOv8n ใช้ VRAM สูงสุดแม้มี forward เร็วสุด ไม่จัดอันดับจากชื่อ Nano หรือ parameter count อย่างเดียว

## ข้อควรระวังในการตีความ

ไม่มีการทดสอบ statistical significance; MOTS20 ไม่ใช่ผลทดสอบ CCTV robustness ขั้นสุดท้าย Pipeline ไม่รวม RLE preparation และ disk I/O; VRAM เป็น peak allocated ของ benchmark การเลือก GT ที่ match กระทบ TP-only quality และภาพต่อเนื่องไม่ใช่ independent samples

## ข้อมูลสำหรับนำไปรวมต่อ

นำ YOLO26n สำหรับ mAP/pipeline, YOLOv8n สำหรับ Recall/forward และ YOLO11n สำหรับ memory ไปพิจารณาร่วมกับข้อจำกัดงาน ยังไม่สร้าง final cross-tier synthesis

[TIER_RESULTS.csv](metrics/TIER_RESULTS.csv) · [REPORT.md](REPORT.md) · [Visual analysis](PRESENTATION_SUMMARY_TH.md) · [Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)
