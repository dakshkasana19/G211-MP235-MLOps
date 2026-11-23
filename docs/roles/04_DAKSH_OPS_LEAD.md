# Daksh Kasana — DevOps & Monitoring Lead
**S24CSEU2714** · Group G211 · MP235 · **Own area: CI, Kubernetes, logs, PSI and retraining checks**

## Your exact work
1. Create `.github/workflows/ci.yml` with **`on:`** -> push trigger, pinned dependency installation from `requirements.txt`, and `pytest`. At least 3 repository tests are required overall, with at least 1 `TestClient` test from Deepanshu. They must run without train/later CSVs. Confirm a **real green GitHub Actions run** before submission.
2. Create `k8s/deployment.yaml` with Deployment **`mp235-api`**, **3 replicas**, image **`mp235-api:1.0`**, containerPort **8000**. Create `k8s/service.yaml` named **`mp235-svc`**, Service port **80**, targetPort **8000**. Service selectors must match Pod labels. Both readiness and liveness HTTP probes must use `/health`; liveness must start later than readiness. A cluster is not compulsory for marking.
3. Integrate prediction logging with Deepanshu: standard Python `logging` plus JSON formatter, **one JSON line per prediction to stdout**, no personal details or disk log file.
4. Compute **10-bin PSI** comparing **cleaned train.csv against later.csv** for **all six required numeric feature columns**: `storage_days`, `temp_set_c`, `humidity_pct`, `power_cuts_hours`, `bag_weight_kg`, `door_openings_per_day`. Use consistent bin boundaries and safe handling of empty bins. Record six measured values plus `most_drifted_feature`.
5. Coordinate with Saivats for v1 MAE on `later.csv` by each `chamber`, identify `worst_served_group`. Verify v2 trained on cleaned train + first **70% date-sorted later**, and both models compared on **same last 30%**. The decision is **`promote`** only when `MAE_v2 <= 0.92 * MAE_v1`, else **`keep`**. Verify MLflow champion alias agrees.
6. Fill the complete **`monitoring` section** of `reports/findings.yaml` using actual metrics; inspect CI status, integration and final submission evidence.

## Files you should personally work on
`.github/workflows/ci.yml`, `k8s/deployment.yaml`, `k8s/service.yaml`, `src/mp235/monitor.py`, `src/mp235/retraining.py` (shared with Saivats), `tests/test_monitor.py`, monitoring section of `reports/findings.yaml`.

## Daily targets and sample commit messages
| Date | What to finish | Commit message example — only after real work |
|---|---|---|
| 24 Nov | CI skeleton + Deployment/Service | `ci(ops): add tests workflow and k8s manifests` |
| 25 Nov | JSON stdout prediction logs + PSI helper | `feat(ops): add structured logging and psi utility` |
| 26 Nov | Green CI, correct ports/selectors/probes | `fix(ci): verify pipeline and health probes` |
| 27 Nov | Six PSI calculations and max-drift feature | `feat(monitor): calculate feature psi drift` |
| 28 Nov | Chamber MAE and v1/v2 8% promotion integration | `feat(ops): integrate monitoring and retraining` |
| 29 Nov | Release quality check, findings, green CI | `chore(ops): verify release checklist` |

## Done when
- [ ] GitHub Actions has a real green pytest-on-push run, tests don't require CSVs.
- [ ] K8s names/image/replicas/ports/selectors/probes match exact spec.
- [ ] One valid JSON stdout log line per prediction; no sensitive data.
- [ ] All six PSI values and three chamber MAEs are measured.
- [ ] 8% decision and `champion` alias are consistent with real MAEs.
- [ ] You committed your own real implementation and can explain it.

**Handoffs:** Clean reference train from Pradyumna; v1/v2 evaluation and alias from Saivats; API health and logging hook from Deepanshu.

**Faculty rules:** Never fake green CI, results or commits. Read original `PROBLEM.md`, `STUDENT_HANDBOOK.md`, `findings.yaml`. AI may tutor/debug, not implement in your place. Every member submits https://forms.cloud.microsoft/r/9ZPB1ZzcAK individually by **29 Nov 2026, 11:59 PM IST**.
