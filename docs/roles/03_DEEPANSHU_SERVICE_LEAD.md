# Deepanshu Bhadana — FastAPI & Docker Lead
**S24CSEU0839** · Group G211 · MP235 · **Own area: service, validation, tests and container**

## Your exact work
1. Create `app/main.py` with `GET /health` returning at least `{"status":"ok"}` and `POST /predict` producing a real numeric `spoilage_pct` prediction from Saivats' champion `models/model.joblib`.
2. The **exact eight request fields** are `storage_days`, `temp_set_c`, `humidity_pct`, `power_cuts_hours`, `bag_weight_kg`, `door_openings_per_day`, `crop`, `chamber`. Do not require `record_id`, `date` or target. Configure Pydantic to forbid extra input fields.
3. Validate **in the Pydantic request schema** using `Field(..., le=300)` for `storage_days` and `Field(..., ge=20)` for `bag_weight_kg`. Verify `storage_days=301` and `bag_weight_kg=19` produce HTTP **422** before inference.
4. Write `tests/test_api.py` with FastAPI `TestClient` checks for health, valid prediction, invalid values and valid boundaries 300/20. Tests must use self-contained model fixtures and **must not depend on raw train/later CSVs**, which are not checked into Git.
5. Create `Dockerfile` from **`python:3.12-slim`**. Copy `requirements.txt` and install pinned libraries **before** copying app/code/model. Add `.dockerignore`; `EXPOSE 8000`; run uvicorn with `--host 0.0.0.0 --port 8000`. Build/tag **`mp235-api:1.0`**. Verify container if Docker available.
6. Work with Daksh on one JSON prediction log line on **stdout**, not a file; no customer personal details.

## Files you should personally work on
`app/main.py`, optionally `app/schemas.py`, `tests/test_api.py`, `Dockerfile`, `.dockerignore`, pinned `requirements.txt` (shared), `docs/api.md`.

## Daily targets and sample commit messages
| Date | What to finish | Commit message example — only after real work |
|---|---|---|
| 24 Nov | Schema + health endpoint + initial TestClient tests | `feat(api): define schemas and health endpoint` |
| 25 Nov | Real `/predict` with compatible model loading | `feat(api): implement model prediction endpoint` |
| 26 Nov | Docker build and runtime verification | `build(api): containerize prediction service` |
| 27 Nov | 422, boundary, health, response tests | `test(api): add boundary and health tests` |
| 28 Nov | Full champion integration and stdout logs | `test(api): verify model integration` |
| 29 Nov | Final API tests and run instructions | `test(api): complete service verification` |

## Check locally, after implementation
```bash
python -m pytest -q tests/test_api.py
uvicorn app.main:app --host 127.0.0.1 --port 8000
# In another shell: curl http://127.0.0.1:8000/health
docker build -t mp235-api:1.0 .
docker run --rm -p 8000:8000 mp235-api:1.0
```

## Done when
- [ ] Exact eight fields; 422 for 301 storage days and 19 kg bags.
- [ ] Real champion prediction, health response, and a passing TestClient test.
- [ ] Correct Docker base image, build order, container port and tag.
- [ ] One structured JSON stdout log line per prediction.
- [ ] Own verified contributions, not fabricated commits.

**Handoffs:** Champion artifact and preprocessing contract from Saivats; canonical categories from Pradyumna; health/logging contract to Daksh.

**Faculty rules:** Only claim actual changes. Read `PROBLEM.md` and `STUDENT_HANDBOOK.md`; AI is tutoring/debugging, not substitute implementation. Individually submit https://forms.cloud.microsoft/r/9ZPB1ZzcAK by **29 Nov 2026, 11:59 PM IST**; prepare for separate viva.
