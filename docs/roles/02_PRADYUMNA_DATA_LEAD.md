# Pradyumna Singh — Data Engineering & DVC Lead
**S24CSEU1400** · Group G211 · MP235 · **Own area: data versioning, seven checks and cleaning**

## Your exact work
1. Extract data from the original G211 ZIP. Do **not** open and save `train.csv` in Excel or modify original bytes. Compute the raw train SHA-256; communicate it to Saivats.
2. Put raw files in `data/raw/`. Run `dvc init` and `dvc add data/raw/train.csv data/raw/later.csv`. Commit `.dvc/config`, `data/raw/train.csv.dvc`, `data/raw/later.csv.dvc`—**not** raw train/later CSV files. Place `holdout_features.csv` at `data/raw/holdout_features.csv` as the handbook requires.
3. Write reproducible checks in `src/mp235/data_audit.py` for **all seven**, each potentially true or false:
   - `leaking_column`: post-event field, missing from holdout
   - `unit_mixup`: feature, affected `chamber` and exact scale factor (wrong = right × factor)
   - `sentinel_value`: column, repeated impossible value and count
   - `duplicate_rows`: extra fully duplicated copies via `df.duplicated().sum()`
   - `stuck_sensor`: constant reading and exact start/end dates
   - `target_typos`: count of `spoilage_pct` values typed 10× too large
   - `spelling_variants`: inconsistent text category and count of canonical levels
4. Implement deterministic cleaning **only for problems supported by the data**; never overwrite raw CSV. Test with small synthetic DataFrames, not private files. Ensure clean values and categories match the model features.
5. Copy the starter `findings.yaml` into **`reports/findings.yaml`**; keep all keys. Complete `data_issues` from measured evidence. Set `present: false` and leave details null when an issue is absent. Share evidence with group.

## Files you should personally work on
`.dvc/config`, `data/raw/*.csv.dvc`, `src/mp235/data_audit.py`, `src/mp235/cleaning.py`, `tests/test_data.py`, `reports/data_audit.md` and the `data_issues` section in `reports/findings.yaml`.

## Daily targets and sample commit messages
| Date | What to finish | Commit message example — only after real work |
|---|---|---|
| 24 Nov | Raw hashes, DVC, initial seven-check audit | `feat(data): initialize dvc and data audit` |
| 25 Nov | Implement verified cleaning rules | `fix(data): clean verified anomalies` |
| 26 Nov | Add synthetic tests and DVC integrity checks | `test(data): cover raw data integrity` |
| 27 Nov | Exact audit evidence and data findings | `docs(data): document cleaning evidence` |
| 28 Nov | Re-test and review findings fields | `test(data): validate findings evidence` |
| 29 Nov | Final DVC pointers/hashes and clean YAML | `docs(findings): finalize measured data checks` |

## Done when
- [ ] Original CSV bytes retained; DVC pointers committed, raw train/later not in Git.
- [ ] Seven problems each have evidence-backed true/false and exact details.
- [ ] Cleaning code is deterministic, CI-safe, and uses no leakage predictor.
- [ ] Own tests pass; Saivats can consume the cleaned dataset.
- [ ] `reports/findings.yaml` data fields match measured results.

**Handoffs:** Clean data + raw hash to Saivats; category values to Deepanshu; cleaned reference data to Daksh.

**Faculty rules:** Commit only your own genuine changes. Do not backdate or fabricate findings. Read the original group-provided `PROBLEM.md`, `STUDENT_HANDBOOK.md`, `findings.yaml`. Submit individually https://forms.cloud.microsoft/r/9ZPB1ZzcAK by **29 Nov 2026, 11:59 PM IST**. Be ready for your individual viva.
