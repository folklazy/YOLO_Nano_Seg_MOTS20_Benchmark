# สรุปผล Nano YOLO Instance Segmentation

## สรุปใน 1 นาที

- โมเดล: YOLO26n-Seg, YOLO11n-Seg, YOLOv8n-Seg
- MOTS20 2,862 frames / 26,894 Person GT instances รายเฟรม
- Official pretrained checkpoints; ไม่มี training หรือ fine-tuning; สถานะ PASS WITH WARNINGS
- Accuracy สูงสุด: YOLO26n-Seg — Mask mAP50-95 0.472698
- Inference เร็วสุด: YOLOv8n-Seg — 9.045 ms
- Pipeline เร็วสุด: YOLO26n-Seg — 82.390 ms / 12.137 FPS
- Peak allocated VRAM ต่ำสุด: YOLO11n-Seg — 1030.00 MiB
- Trade-off หลัก: ตัวนำ mAP สูงกว่ารองอันดับสอง 4.077 percentage points; ต้องแยก forward จาก pipeline

## ผลลัพธ์หลัก

| Model | Mask mAP50-95 | AP75 | Recall | Inference ms | Pipeline ms | FPS | Peak VRAM MiB |
|---|---|---|---|---|---|---|---|
| YOLO26n-Seg | 0.472698 | 0.506766 | 0.687068 | 13.042 | 82.390 | 12.137 | 1043.13 |
| YOLO11n-Seg | 0.431929 | 0.450826 | 0.693798 | 11.745 | 97.441 | 10.263 | 1030.00 |
| YOLOv8n-Seg | 0.423062 | 0.439115 | 0.696921 | 9.045 | 95.683 | 10.451 | 1117.09 |

AP/Recall เป็น fraction ช่วง 0–1; latency เป็น ms/frame และ FPS มาจาก mean pipeline

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

- YOLO26n-Seg นำ YOLO11n-Seg ด้าน mAP 4.077 percentage points
- YOLOv8n นำ Recall แต่มี Precision ต่ำสุด; YOLO26n นำ mAP/AP75 แต่ Recall ต่ำสุด
- YOLOv8n forward เร็วสุด แต่ YOLO26n pipeline เร็วสุด; YOLO11n ใช้ VRAM ต่ำสุดแต่ pipeline ช้าที่สุด
- ไม่มีคู่ผ่าน descriptive mAP near-tie screen ≤0.001; ความใกล้ของ latency เป็นคนละประเด็น; near tie ไม่ใช่ equivalence หรือ statistical significance

## บทบาทของแต่ละโมเดล

| Model | จุดเด่น | สิ่งที่แลก | เหมาะพิจารณาเมื่อ |
|---|---|---|---|
| YOLO26n-Seg | นำ mAP/AP75/Precision; pipeline เร็วสุด | Recall ต่ำสุด; forward ช้าสุด | เน้น mask AP และ pipeline โดยตรวจ coverage เพิ่ม |
| YOLO11n-Seg | VRAM, parameters และ checkpoint ต่ำสุดใน tier | Pipeline ช้าที่สุด; Recall ต่ำกว่า YOLOv8n | Memory หรือขนาด checkpoint เป็นข้อจำกัด |
| YOLOv8n-Seg | Recall สูงสุดและ inference เร็วสุด | Precision/mAP ต่ำสุด; VRAM สูงสุด | สนใจ forward หรือ Recall พร้อมตรวจ FP |

## Trade-off หลัก

### Accuracy vs Speed

YOLO26n-Seg มี mAP 0.472698; ตัว forward เร็วสุด YOLOv8n-Seg มี mAP 0.423062 และ inference ต่ำกว่า 3.997 ms ส่วน pipeline ต้องดู YOLO26n-Seg แยก ไม่ถือว่า forward winner เป็น throughput winner

### Accuracy vs Memory

YOLO26n-Seg ใช้ VRAM มากกว่า YOLO11n-Seg 13.13 MiB เพื่อ mAP สูงกว่า 4.077 percentage points ไม่ใช้ชื่อขนาดหรือ parameters แทน memory measurement

## ข้อควรระวังในการตีความ

ไม่มี significance test; ภาพวิดีโอสัมพันธ์กัน TP-only quality วัดเฉพาะคู่ที่ match และ Recall เป็น mask matching ไม่ใช่ box Recall Pipeline ไม่รวม decode, RLE preparation และการเขียนผล; VRAM เป็น peak allocated ภายใต้ benchmark นี้ การแบ่ง tier ไม่ทำให้ capacity/pretraining เท่ากัน และยังไม่ยืนยัน CCTV robustness ไม่มี weighted score หรือผู้ชนะทุกข้อจำกัด

## รายละเอียดเพิ่มเติม

[REPORT.md](REPORT.md) · [รายงานวิจัยภาพเชิงคุณภาพ](PRESENTATION_SUMMARY_TH.md) · [TIER_RESULTS.csv](metrics/TIER_RESULTS.csv) · [Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)
