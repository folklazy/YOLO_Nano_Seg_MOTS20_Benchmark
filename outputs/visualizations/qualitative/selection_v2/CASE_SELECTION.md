# Nano — qualitative case selection v2

Selected from 12 frozen visualization frames using per-frame metrics, original/GT images and saved RLE masks at confidence ≥0.25 and mask matching IoU ≥0.50, with the original evaluator and ignore policy. No inference was run.

One shared anchor plus three cases selected for tier-specific behavior. Tiers need not share every frame; within each case, all models use the same full frame. ROI views supplement the full comparison and do not hide errors elsewhere.

| Case | Sequence / frame | Why selected / decision use | Source comparison |
|---|---|---|---|
| 1 | MOTS20-11 / 000001 | Tier diagnostic: equal TP for two models, unequal FP and different GT. Compare GT 2028 coverage and extra masks: YOLO26n and YOLO11n have TP 8 and the same FN set, but YOLO11n has an FP on already matched GT 2006; YOLOv8n has TP 7. | new composite from saved predictions |
| 2 | MOTS20-09 / 000263 | Shared anchor: common failure. Examine common limitations and unmatched outputs among overlapping people; counts do not give a clear winner in this case. | reuse existing image |
| 3 | MOTS20-02 / 000300 | Trade-off: additional valid GT and more unmatched outputs. YOLOv8n recovers more GT but has more FP, directionally consistent with its higher Recall / lower Precision at dataset level. | reuse existing image |
| 4 | MOTS20-09 / 000001 | Similar coverage with extra masks on already matched GT. All models have TP 6 / FN 0; YOLO26n adds a mask overlapping GT 2001, and YOLOv8n adds two masks overlapping GT 2019. YOLO11n has no FP. | reuse existing image |

## Why some frames are shared across tiers

Case 2 (09/263) compares FN/FP against the same GT. Other frames may repeat when the same error region helps compare different models: 05/419 examines GT 2002 in Second-largest/Medium; 02/1 examines equal counts and different GT sets in Second-largest/Medium; 02/600 provides a counterexample in Largest/Small; 02/300 examines TP–FP trade-offs in Small/Nano; 11/1 examines GT 2016 in Second-largest and GT 2028 with extra masks in Nano; 11/450 compares equal coverage with extra outputs in Largest/Medium. Reused frames are not additional independent evidence.

## Replacement of previous cases

Previous Case 1 (02/600) contained a real GT trade-off. Its replacement (11/1) adds scene context and separates outputs of the equal-TP pair. Cases 3 and 4 retain the GT/FP trade-off and extra masks on real people. Previous images and evidence remain unchanged for audit; the previous presentation is retained under reports/archive.

## Scope

Across five tiers, 20 case slots use 10 distinct original frames (previously 6). The selection includes MOTS20-11, common failures and counterexamples, rather than only frames where the accuracy leader wins. The 12-frame pool does not represent the dataset, and these are not claimed to be the most divergent frames among all 2,862. Images do not measure latency, VRAM or statistical significance.

[Candidate pool](CANDIDATE_POOL.json) · [Case evidence](CASE_EVIDENCE.json) · [Focus evidence](FOCUS_EVIDENCE.json) · [Decision audit](CASE_DECISION_AUDIT.json) · [Active selection](../../../../manifests/QUALITATIVE_SELECTION.json)
