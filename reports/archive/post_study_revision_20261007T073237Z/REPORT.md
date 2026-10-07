# Nano (N) YOLO Segmentation Benchmark — MOTS20

## 1. Experiment Status

PASS WITH WARNINGS

- Models completed: 3/3
- Frames: 2,862 per model; Person GT instances: 26,894
- Run ID: `benchmark-20261005T083307Z`

## 2. Models Tested

| Family | Model | Parameters | GFLOPs | Checkpoint MB |
| --- | --- | --- | --- | --- |
| YOLO26 | YOLO26n-Seg | 3,126,280 | 10.630 | 6.72 |
| YOLO11 | YOLO11n-Seg | 2,876,848 | 9.959 | 6.18 |
| YOLOv8 | YOLOv8n-Seg | 3,409,968 | 12.141 | 7.07 |


## 3. Protocol Compatibility

| Item | Status |
|---|---|
| Dataset | PASS |
| Evaluator | PASS |
| Preprocessing | PASS |
| Input size | PASS |
| Precision | PASS |
| Thresholds | PASS |
| maxDet | PASS |
| Timing protocol | PASS |
| Environment | PASS |

Dataset compatibility: PASS

Preprocessing compatibility: PASS

[Common methodology](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study/blob/main/METHODOLOGY_REFERENCE.md) · [Frozen protocol](EXPERIMENT_PROTOCOL.md)

Scientific integrity PASS; all 15 detailed checks are retained in [final integrity](manifests/final_integrity.json), including model/frame coverage, checkpoint hashes, native predictions, cap saturation and clean timing.

## 4. Overall Results

| Model | Mask mAP50-95 | AP50 | AP75 | Precision | Recall | F1 | TP-only IoU | TP-only Dice | Inference ms | Pipeline ms | FPS | Peak VRAM MiB | Params | GFLOPs | Checkpoint MB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLO26n-Seg | 0.472698 | 0.774367 | 0.506766 | 0.901850 | 0.687068 | 0.779942 | 0.810328 | 0.891429 | 13.042 | 82.390 | 12.137 | 1043.13 | 3,126,280 | 10.630 | 6.72 |
| YOLO11n-Seg | 0.431929 | 0.757732 | 0.450826 | 0.866571 | 0.693798 | 0.770619 | 0.785422 | 0.875606 | 11.745 | 97.441 | 10.263 | 1030.00 | 2,876,848 | 9.959 | 6.18 |
| YOLOv8n-Seg | 0.423062 | 0.750024 | 0.439115 | 0.826411 | 0.696921 | 0.756163 | 0.781325 | 0.872824 | 9.045 | 95.683 | 10.451 | 1117.09 | 3,409,968 | 12.141 | 7.07 |


## 5. Tier Winners

| Category | Model | Value |
|---|---|---|
| Highest Mask mAP50-95 | YOLO26n-Seg | 0.472698 |
| Highest AP75 | YOLO26n-Seg | 0.506766 |
| Highest Recall | YOLOv8n-Seg | 0.696921 |
| Fastest inference | YOLOv8n-Seg | 9.045 |
| Fastest pipeline | YOLO26n-Seg | 82.390 |
| Highest FPS | YOLO26n-Seg | 12.137 |
| Lowest VRAM | YOLO11n-Seg | 1030.00 |

Inference and pipeline latency are in ms/frame; FPS is derived from mean pipeline latency; VRAM is peak allocated MiB.

## 6. Key Findings

- Observation: YOLO26n-Seg has the highest Mask mAP50-95, 0.472698; the gap to the runner-up is 0.040768 on the 0–1 scale.
- Observation: YOLO26n-Seg leads AP75, but YOLOv8n-Seg leads Recall; YOLO26n has the lowest Recall, so mask accuracy and instance coverage must be considered separately.
- Observation: the fastest forward pass is from YOLOv8n-Seg; the fastest pipeline and highest FPS are from YOLO26n-Seg; the lowest VRAM is from YOLO11n-Seg.
- Closest pair in Mask mAP50-95: YOLO11n-Seg / YOLOv8n-Seg differ by 0.008867; this does not establish equivalence or statistical significance without testing.
- Interpretation: selection must distinguish accuracy, forward latency, pipeline latency and memory; lower GFLOPs or parameter counts do not guarantee lower latency or VRAM.

## 7. Per-sequence Observations

- YOLO26n-Seg: strongest MOTS20-11 (0.541629); weakest MOTS20-02 (0.335752) by Mask mAP50-95.
- YOLO11n-Seg: strongest MOTS20-11 (0.501796); weakest MOTS20-02 (0.290888) by Mask mAP50-95.
- YOLOv8n-Seg: strongest MOTS20-11 (0.495783); weakest MOTS20-02 (0.271786) by Mask mAP50-95.
- Ranking changes relative to pooled AP: none across the four sequences.

Recall ordering differs: YOLOv8n leads on MOTS20-02, YOLO11n leads on MOTS20-05, and YOLO26n leads on MOTS20-09/11. Pooled AP is not a simple mean of sequence AP; complete values remain in [PER_SEQUENCE_RESULTS.csv](metrics/PER_SEQUENCE_RESULTS.csv).

## 8. Efficiency and Resource Observations

- Closest pair in mean inference latency: YOLO26n-Seg / YOLO11n-Seg differ by 1.297 ms; statistical significance was not tested.
- Closest pair in mean pipeline latency: YOLO11n-Seg / YOLOv8n-Seg differ by 1.758 ms; statistical significance was not tested.

YOLO11n-Seg has the lowest peak allocated VRAM. Loaded/fused parameters, GFLOPs and separate load times are retained in [MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv). Peak reserved VRAM is preserved in [source timing summary](timing/benchmark-20261005T083307Z/clean_repetition/summary.csv). Separate RLE preparation means: yolo26n-seg.pt: 336.791 ms; yolo11n-seg.pt: 409.860 ms; yolov8n-seg.pt: 405.991 ms.

Nine accepted CLEAN rounds: 3 per model, 100 measured frames per round after 10 warmups with CUDA synchronization. Pipeline = preprocess + inference + postprocess. Mean postprocess: YOLO26n-Seg: 67.627 ms; YOLO11n-Seg: 83.942 ms; YOLOv8n-Seg: 84.911 ms. RLE preparation and disk I/O are excluded; Ultralytics-inclusive postprocess is a diagnostic subset and must not be added again to pipeline.

## 9. Warnings and Anomalies

CPU NNPACK unsupported-hardware warnings were recorded during Nano setup/complexity inspection. Scientific integrity PASS and primary timing contains nine CLEAN GPU rounds; no package versions or measured values were changed to suppress warnings. maxDet100 fails at least one AP convergence field for each model; maxDet200/300/1000 converge for all three, so the frozen AP maxDet200 remains valid. Pipeline excludes RLE preparation and disk I/O; reported FPS is not end-to-end mask-saving/CCTV throughput. No training, fine-tuning or inference rerun for documentation.

## 10. Limitations

This evaluates frame-level Person instance segmentation on MOTS20, rather than MOTS tracking. The 26,894 GT instances are frame-level annotations, not unique people. TP-only IoU/Dice are conditional on successful matching.

Consecutive video frames are correlated, and no statistical significance test was performed; small differences are descriptive. Selected qualitative cases do not replace dataset-level metrics.

These measurements do not establish robustness to blur, low light, camera angle or occlusion severity, or deployment suitability. They support candidate selection for later CCTV robustness evaluation only. No weighted score or architectural causal conclusion is used.

## 11. Reproducibility and Source Artifacts

- [TIER_RESULTS.csv](metrics/TIER_RESULTS.csv)
- [PER_SEQUENCE_RESULTS.csv](metrics/PER_SEQUENCE_RESULTS.csv)
- [TIMING_SUMMARY.csv](metrics/TIMING_SUMMARY.csv)
- [MODEL_COMPLEXITY.csv](metrics/MODEL_COMPLEXITY.csv)
- [PREFLIGHT_MAXDET.csv](metrics/PREFLIGHT_MAXDET.csv)

[Standardization provenance](manifests/STANDARDIZATION.json) · [Final integrity](manifests/final_integrity.json) · [Public environment](manifests/environment_public.json) · [Timing source](timing/benchmark-20261005T083307Z/clean_repetition/summary.csv) · [Plots](outputs/plots/INDEX.md)

Lossless per-frame RLE predictions and full telemetry remain local under predictions/benchmark-20261005T083307Z/ and timing/benchmark-20261005T083307Z/. Published manifests record hashes; this editorial update does not recalculate metrics or rerun inference.

## 12. Relation to Full Scaling Study

[Master Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study) — this is the Nano tier only. All five tiers are complete, but the final 17-model synthesis remains pending and requires explicit authorization. This report update starts no benchmark or synthesis.

## Qualitative Analysis

Four same-frame diagnostic comparisons from saved lossless predictions are discussed in [PRESENTATION_SUMMARY_TH.md](PRESENTATION_SUMMARY_TH.md). See [current case selection](outputs/visualizations/qualitative/selection_v2/CASE_SELECTION.md) and [active selection](manifests/QUALITATIVE_SELECTION.json) for selection reasons, shared and tier-specific behaviors, and evidence limits. Comparisons use original MOTS20 frames. No inference or measured values were changed for this documentation update.
