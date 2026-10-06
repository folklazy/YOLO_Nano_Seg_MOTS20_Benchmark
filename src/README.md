# Nano benchmark and documentation

Completed run: `benchmark-20261005T083307Z`. Three models × 2,862 frames; nine CLEAN timing rounds. STOP after Nano; no automatic master synthesis.

From the workspace root, `.venv/bin/python YOLO_Nano_Seg_MOTS20_Benchmark/src/run_nano.py --all` is the deterministic scientific runner. The completed run must not be rerun. It validates shared inputs once, preflights all models and maxDet, runs sequential accuracy and clean timing, builds canonical metrics and validates scientific integrity. It stops with documentation pending. Verbose logs/predictions remain local; frozen input archives and SHA256 record the executed source/protocol/config.

`report_nano.py` generates the completed reports and six plots only after `QUALITATIVE_REVIEW.json` records four inspected saved-prediction cases; no model loading or inference. It refuses to overwrite existing plots. `validate_nano_completion.py` is a read-only validation of canonical measurements, source hashes, selected cases, template headings, links and numeric table cells; it writes a validation manifest.

The shared Master `src/build_qualitative_comparisons.py --tier Nano` renders the selected full-frame comparisons from lossless saved predictions and original/GT, without inference. Existing images are never overwritten. Documentation scripts were added after measurement freeze and do not alter frozen scientific sources.
