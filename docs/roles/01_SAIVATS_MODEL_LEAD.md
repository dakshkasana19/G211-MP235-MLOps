# Saivats — ML & Experiment Lead
**S24CSEU1436** · Group G211 · MP235 · **Own area: training, MLflow and holdout**

## Your exact work
1. Build reproducible regression training for `spoilage_pct` using **cleaned train.csv only**. Read `params.yaml` via `yaml.safe_load`; handle six numeric predictors and categorical `crop`, `chamber`. Exclude identifiers, date, target and any post-event leakage column.
2. Train v1; make **at least 3 real MLflow runs**, all with an MAE metric and `data_sha256` calculated from the original, unmodified raw `train.csv`. Use `mlflow.set_tracking_uri("sqlite:///mlflow.db")`. Commit `mlflow.db`.
3. Register model v1 as version 1; set the MLflow `champion` alias. Store the champion artifact in `models/model.joblib` for Deepanshu.
4. Evaluate v1's MAE on `later.csv` **separately for each chamber**. Share the measured numbers with Daksh.
5. Sort `later.csv` by date. Train v2 on cleaned train plus its **first 70%**. Compare v1/v2 on the **same last 30%**. Promote v2 only if `MAE_v2 <= 0.92 * MAE_v1`; register v2 as version 2, and update champion alias only if promotion is justified.
6. Export `predictions/holdout_predictions.csv` using champion for all **250 holdout rows**. Columns must be **exactly** `record_id,prediction` with no index.
7. Record actual `tracking` fields in `reports/findings.yaml`: experiment name, v1 best run ID, registered model name, champion version. Coordinate monitoring entries with Daksh.

## Files you should personally work on
`params.yaml` (shared), `src/mp235/train.py`, `src/mp235/evaluate.py`, `src/mp235/predict_holdout.py`, `tests/test_model.py`, `mlflow.db`, `models/model.joblib`, `predictions/holdout_predictions.csv`.

## Daily targets and sample commit messages
| Date | What to finish | Commit message example — only after real work |
|---|---|---|
| 24 Nov | Configurable training skeleton and data contract | `feat(model): add configurable training entry point` |
| 25 Nov | Train v1 and log first genuine MLflow run | `feat(model): train baseline with mlflow tracking` |
| 26 Nov | 3+ runs; registry v1 + champion | `feat(model): register tracked champion model` |
| 27 Nov | v1 MAE for each chamber on later | `feat(model): evaluate chamber-wise later mae` |
| 28 Nov | v2 70/30 evaluation and 8% decision | `feat(model): evaluate v2 promotion rule` |
| 29 Nov | Final champion, holdout CSV and tracking findings | `feat(predictions): export champion holdout results` |

## Done when
- [ ] Real 3+ MLflow runs with `data_sha256` + MAE; SQLite DB committed.
- [ ] v1/v2 registry versions, correct champion alias, model artifact loadable.
- [ ] Chamber MAEs + v1/v2 comparison are measured, not fabricated.
- [ ] Holdout CSV has all record IDs and exactly two required columns.
- [ ] Your own commits and tests demonstrate what you wrote.

**Handoffs:** Get cleaned data and original hash from Pradyumna; give champion model/schema to Deepanshu; give metrics/decision to Daksh.

**Faculty rules:** Your own genuine commits; no backdating or fake results. Source: group `PROBLEM.md`, `STUDENT_HANDBOOK.md`, `findings.yaml`. Every member separately submits https://forms.cloud.microsoft/r/9ZPB1ZzcAK by **29 Nov 2026, 11:59 PM IST**. AI can explain/debug; each member must implement and defend their own code in the viva.
