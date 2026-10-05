# Nano case selection

Pool: 12 exact frozen visualization frames. Shortlisted using saved per-frame TP/FP/FN/matched IoU; four full-frame comparisons manually inspected. No inference rerun. Not a representative sample.

| Case | Sequence | Frame | Reason |
|---|---|---|---|
| 1 | MOTS20-02 | 000600 | accuracy leader additional matched instance, with remaining errors |
| 2 | MOTS20-09 | 000263 | common unmatched GT and false positives |
| 3 | MOTS20-02 | 000300 | higher recall with extra unmatched predictions |
| 4 | MOTS20-09 | 000001 | all valid GT matched, differing false positives; closest-pair check |

Includes leader advantage, common failures, recall counterexample with additional FP, and similar valid-person outputs with different extra masks. Sources and SHA256: [CASE_EVIDENCE.json](CASE_EVIDENCE.json). Numbers are limited to selected frames and must not be extrapolated to dataset-wide failure frequencies.
