# Nano (N) YOLO Segmentation Benchmark — MOTS20

## 1. Experiment Status

COMPLETE / PASS WITH WARNINGS. Scientific integrity PASS; run `benchmark-20261005T083307Z`.

## 2. Models Tested

| Family | Model | Parameters | GFLOPs | Checkpoint MB |
| --- | --- | --- | --- | --- |
| YOLO26 | YOLO26n-Seg | 3,126,280 | 10.630 | 6.72 |
| YOLO11 | YOLO11n-Seg | 2,876,848 | 9.959 | 6.18 |
| YOLOv8 | YOLOv8n-Seg | 3,409,968 | 12.141 | 7.07 |


## 3. Protocol Compatibility

Dataset/environment/framework compatible with the frozen Largest baseline. See [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) and [Master methodology](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/main/METHODOLOGY_REFERENCE.md).

| Item | Status |
|---|---|
| Exactly 3 expected models | PASS |
| 2862 frames and 26894 GT per model | PASS |
| Dataset hashes, dimensions and ordering | PASS |
| Frozen evaluator and preprocessing | PASS |
| Config and protocol freeze | PASS |
| Framework and environment | PASS |
| AP maxDet 200 preflight | PASS |
| Finite native Person predictions | PASS |
| No model cap saturation | PASS |
| Accuracy arithmetic and sequence completeness | PASS |
| Three clean timing rounds per model | PASS |
| Exact timing frame order | PASS |
| Timing pooled statistics and VRAM | PASS |
| Checkpoint hashes | PASS |
| Frozen input archive | PASS |


## 4. Overall Results

| Model | Mask mAP50-95 | AP50 | AP75 | Precision | Recall | F1 | TP-only IoU | TP-only Dice | Inference ms | Pipeline ms | FPS | Peak VRAM MiB | Params | GFLOPs | Checkpoint MB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO26n-Seg | 0.472698 | 0.774367 | 0.506766 | 0.901850 | 0.687068 | 0.779942 | 0.810328 | 0.891429 | 13.042 | 82.390 | 12.137 | 1043.13 | 3,126,280 | 10.630 | 6.72 |
| YOLO11n-Seg | 0.431929 | 0.757732 | 0.450826 | 0.866571 | 0.693798 | 0.770619 | 0.785422 | 0.875606 | 11.745 | 97.441 | 10.263 | 1030.00 | 2,876,848 | 9.959 | 6.18 |
| YOLOv8n-Seg | 0.423062 | 0.750024 | 0.439115 | 0.826411 | 0.696921 | 0.756163 | 0.781325 | 0.872824 | 9.045 | 95.683 | 10.451 | 1117.09 | 3,409,968 | 12.141 | 7.07 |


## 5. Tier Winners

| Category | Model | Value |
|---|---|---|
| Mask mAP50-95 | YOLO26n-Seg | 0.472698 |
| AP75 | YOLO26n-Seg | 0.506766 |
| Recall | YOLOv8n-Seg | 0.696921 |
| Inference speed | YOLOv8n-Seg | 9.045 ms |
| Pipeline speed | YOLO26n-Seg | 82.390 ms |
| VRAM | YOLO11n-Seg | 1030.00 MiB |
| Highest FPS | YOLO26n-Seg | 12.137 |


## 6. Key Findings

- YOLO26n นำ mAP เหนือ YOLO11n/YOLOv8n ประมาณ 0.040768/0.049636 แต่ Recall ต่ำสุด เป็น accuracy–coverage trade-off
- YOLO11n/YOLOv8n เป็นคู่ mAP ใกล้ที่สุด ต่างประมาณ 0.008867; AP75/Precision นำใน YOLO11n แต่ Recall/forward นำใน YOLOv8n ไม่มี significance test
- YOLOv8n forward เร็วสุด 9.045 ms แต่ YOLO26n pipeline เร็วสุด 82.390 ms / 12.137 FPS เพราะผลรวม stage ที่วัดต่างจาก forward อย่างเดียว
- YOLO11n VRAM ต่ำสุด 1030.00 MiB และ GFLOPs ต่ำสุด แต่ pipeline ช้าที่สุด; complexity ไม่กำหนดอันดับ latency โดยตรง

## 7. Per-sequence Observations

- YOLO26n-Seg / MOTS20-02: mAP 0.335752, Recall 0.550220
- YOLO26n-Seg / MOTS20-05: mAP 0.523544, Recall 0.713242
- YOLO26n-Seg / MOTS20-09: mAP 0.468691, Recall 0.759740
- YOLO26n-Seg / MOTS20-11: mAP 0.541629, Recall 0.739279
- YOLO11n-Seg / MOTS20-02: mAP 0.290888, Recall 0.564143
- YOLO11n-Seg / MOTS20-05: mAP 0.489640, Recall 0.733486
- YOLO11n-Seg / MOTS20-09: mAP 0.426000, Recall 0.755551
- YOLO11n-Seg / MOTS20-11: mAP 0.501796, Recall 0.735754
- YOLOv8n-Seg / MOTS20-02: mAP 0.271786, Recall 0.582611
- YOLOv8n-Seg / MOTS20-05: mAP 0.485786, Recall 0.729985
- YOLOv8n-Seg / MOTS20-09: mAP 0.416278, Recall 0.745915
- YOLOv8n-Seg / MOTS20-11: mAP 0.495783, Recall 0.738456

All four sequences rank YOLO26n > YOLO11n > YOLOv8n by mAP. All models have their lowest sequence mAP on MOTS20-02 and highest on MOTS20-11. Recall ordering differs: YOLO26n leads on 09/11 but trails on 02/05. Pooled AP is not a simple mean of sequence AP.

## 8. Efficiency and Resource Observations

Nine accepted CLEAN rounds: 3 per model, 100 measured frames per round after 10 warmups with CUDA synchronization. Pipeline = preprocess + inference + postprocess. Mean postprocess: YOLO26n 67.627 ms; YOLO11n 83.942 ms; YOLOv8n 84.911 ms. Mean RLE preparation 336.791/409.860/405.991 ms is excluded from pipeline along with disk I/O; do not treat reported FPS as artifact-export throughput. Ultralytics-inclusive diagnostic is not added again to pipeline.

[MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv) retains loaded/fused parameters, GFLOPs and load time. Reserved VRAM remains in accepted timing source.

## 9. Warnings and Anomalies

CPU NNPACK unsupported-hardware warnings were recorded during setup/complexity inspection. Scientific integrity PASS and nine CLEAN GPU timing rounds; no warning is used to modify a measured value. maxDet100 fails at least one AP convergence field for each model; maxDet200/300/1000 converge for all three. No package upgrade, training, fine-tuning or inference rerun for documentation.

## 10. Limitations

Frame-level segmentation, not MOTS tracking. TP-only quality is conditional on matching; selected qualitative cases are diagnostic. No statistical-significance test, causal architecture claim, weighted score or final CCTV superiority.

## 11. Reproducibility and Source Artifacts

Canonical [TIER_RESULTS](metrics/TIER_RESULTS.csv), [PER_SEQUENCE_RESULTS](metrics/PER_SEQUENCE_RESULTS.csv), [TIMING_SUMMARY](metrics/TIMING_SUMMARY.csv), [MODEL_COMPLEXITY](metrics/MODEL_COMPLEXITY.csv), [PREFLIGHT_MAXDET](metrics/PREFLIGHT_MAXDET.csv).

[STANDARDIZATION](manifests/STANDARDIZATION.json), [final integrity](manifests/final_integrity.json), [public environment](manifests/environment_public.json). Saved lossless predictions and detailed telemetry remain local/ignored. See [canonical plots](outputs/plots/INDEX.md).

## 12. Relation to Full Scaling Study

Nano only; no automatic final 17-model synthesis. [Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study). STOP after Nano.

## Qualitative Analysis

Four inspected comparisons from saved predictions are discussed in [PRESENTATION_SUMMARY_TH.md](PRESENTATION_SUMMARY_TH.md). [CASE_SELECTION](outputs/visualizations/qualitative/CASE_SELECTION.md) documents balanced selection and limitations. No inference was run for documentation.
