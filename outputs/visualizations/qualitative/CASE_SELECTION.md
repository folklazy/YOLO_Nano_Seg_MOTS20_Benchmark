# Nano case selection

Pool: 12 exact frozen visualization frames. Shortlisted using saved per-frame TP/FP/FN/matched IoU; four full-frame comparisons manually inspected. No inference rerun. Not a representative sample.

| Case | Sequence | Frame | Reason |
|---|---|---|---|
| 1 | MOTS20-02 | 000600 | accuracy leader additional matched instance, with remaining errors |
| 2 | MOTS20-09 | 000263 | common unmatched GT and false positives |
| 3 | MOTS20-02 | 000300 | higher recall with extra unmatched predictions |
| 4 | MOTS20-09 | 000001 | all valid GT matched, differing false positives; closest-pair check |

Includes leader advantage, common failures, recall counterexample with additional FP, and similar valid-person outputs with different extra masks. Sources and SHA256: [CASE_EVIDENCE.json](CASE_EVIDENCE.json). Numbers are limited to selected frames and must not be extrapolated to dataset-wide failure frequencies.

## Decision-use review (2026-10-06)

All 12 frozen candidates were rechecked; all four full comparisons and four identical-ROI views were inspected. Selected frames retained for diagnostic diversity, not because every case shows a leader win. The pool does not represent all frames or sequences.

| Case | Role | Pain point |
|---|---|---|
| 1 | จำแนกโมเดล / ต่าง GT | GT 2029/2043/2048 ในกลุ่มคนเล็ก |
| 2 | ข้อจำกัดร่วม | FN ชุดเดียวกันหก GT และ unmatched masks |
| 3 | TP–FP trade-off | GT 2026/2040 และ FP เพิ่ม |
| 4 | extra mask บนคนจริง | unmatched masks ทับ GT ที่มีคู่แล้ว |

See [FOCUS_EVIDENCE.json](FOCUS_EVIDENCE.json) for fixed-metric assignments and per-target diagnostic IoU. Full comparisons are unchanged. ROI views are supplementary; count semantics refer to the full frame. These examples support conditional decisions about segmentation coverage and extra masks; they cannot establish dataset-wide error frequency, system speed or VRAM.
