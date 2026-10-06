# Nano (N) — การทดสอบ YOLO Instance Segmentation บน MOTS20

## ภาพรวม

เปรียบเทียบการแยก Person เป็นราย instance บน MOTS20 ด้วยโมเดล pretrained โดยไม่ฝึกเพิ่มหรือปรับจูน ประเมินรายเฟรมไม่ใช่การติดตามคน เอกสารนี้ใช้แนะนำ repository และเชื่อมไปยังผลเชิงตัวเลขรายงานเทคนิคและการวิเคราะห์ภาพ

## โมเดลที่ทดสอบ

| ตระกูล | โมเดล | ขนาด |
| --- | --- | --- |
| YOLO26 | YOLO26n-Seg | Nano (N) |
| YOLO11 | YOLO11n-Seg | Nano (N) |
| YOLOv8 | YOLOv8n-Seg | Nano (N) |

## สถานะการทดลอง

COMPLETE / PASS WITH WARNINGS — ครบ 3/3 โมเดล โมเดลละ 2,862 เฟรมและ Person GT รายเฟรม 26,894 instances
รอบทดลอง: `benchmark-20261005T083307Z` ใช้ผลที่บันทึกไว้ ไม่มีการรัน inference ใหม่เพื่อปรับเอกสาร

## ผลลัพธ์หลัก

| โมเดล | Mask mAP50-95 | Recall | F1 | Inference (ms) | Pipeline (ms) | FPS | Peak allocated VRAM (MiB) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO26n-Seg | 0.472698 | 0.687068 | 0.779942 | 13.042 | 82.390 | 12.137 | 1043.13 |
| YOLO11n-Seg | 0.431929 | 0.693798 | 0.770619 | 11.745 | 97.441 | 10.263 | 1030.00 |
| YOLOv8n-Seg | 0.423062 | 0.696921 | 0.756163 | 9.045 | 95.683 | 10.451 | 1117.09 |

## เอกสารประกอบ

- [บทสรุปเชิงตัวเลข](RESULTS_SUMMARY_TH.md)
- [การวิเคราะห์ภาพและพฤติกรรมเชิงคุณภาพ](PRESENTATION_SUMMARY_TH.md)
- [รายงานเทคนิค](REPORT.md)
- [โพรโทคอลการทดลอง](EXPERIMENT_PROTOCOL.md)

## การนำทางในชุดการศึกษา

[Largest (X/E)](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark) | [Second-largest (L/C)](https://github.com/folklazy/YOLO_Second_Largest_Seg_MOTS20_Benchmark) | [Medium (M)](https://github.com/folklazy/YOLO_Medium_Seg_MOTS20_Benchmark) | [Small (S)](https://github.com/folklazy/YOLO_Small_Seg_MOTS20_Benchmark) | [Nano (N)](https://github.com/folklazy/YOLO_Nano_Seg_MOTS20_Benchmark) | [การศึกษาหลัก](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)

## หลักฐานสำหรับตรวจสอบซ้ำ

[ค่าตัวชี้วัด](metrics/) · [การตั้งค่า](configs/) · [หลักฐานและแหล่งที่มา](manifests/) · [ภาพและกราฟ](outputs/) · [บันทึกย้อนหลัง](reports/archive/)
