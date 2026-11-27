# Sentinel plan: tick each box when you have the PROOF

Rule: commit every day. Write 3 lines in LOG.md after every session.
Stuck for 30 minutes? Write the exact question in LOG.md, then look it up or ask.

## Phase 0: set up (Nov 26-27)
- [ ] Create the GitHub repo `sentinel` and push this skeleton. Proof: the link works.
- [ ] Create a virtual environment in WSL and install `requirements.txt`. Proof: `pytest` runs.

## Phase 1: it checks (Nov 28 - Dec 4)
- [ ] `check_http` reports up or down plus latency. Proof: good URL and dead URL both reported correctly.
- [ ] `demo_service` runs with /health and /break. Proof: you can break it from a browser.
- [ ] `demo_service` runs in Docker. Proof: `docker ps` shows it; `curl localhost:5000/health` answers.
- [ ] Loop over the services in `config.yaml`. Proof: terminal output with timestamps.
- [ ] Book the AWS Cloud Practitioner exam. Send 5 job applications.

## Phase 2: it heals (Dec 5-11)
- [ ] Count consecutive failures per service. Proof: break the service, watch the counter rise.
- [ ] `restart_container` works. Proof: recording of break, detect, restart.
- [ ] Cooldown stops restart loops. Proof: a service that cannot recover is not restarted every second.
- [ ] Incident log with start, end and duration. Proof: a log showing one real incident.
- [ ] Alert when an incident opens and closes. Proof: a message or log line.

## Phase 3: quality (Dec 12-18)
- [ ] 5 tests (failure counter, cooldown, incident duration, config parse, one faked check).
- [ ] CI workflow (`.github/workflows/ci.yml`). Proof: green badge in the README.
- [ ] Update the internship end date on LinkedIn.

## Phase 4: ship (Dec 19-25)
- [ ] README complete with diagram and how to run.
- [ ] 30-second demo GIF (break, detect, restart, recover).
- [ ] Add Sentinel to LinkedIn and the resume.
- [ ] Stretch: run it on EC2 for a day.

## Phase 5: land it (Dec 26 - Jan 2)
- [ ] Take the Cloud Practitioner exam.
- [ ] Explain Sentinel out loud (why a cooldown? why 3 failures?).
- [ ] Apply to 5 roles a day.

## If you fall behind, cut in this order
1. EC2 deployment  2. Telegram (log only)  3. Tests (keep 3)
Never cut: the checker, the recovery, the incident log, the README, the demo.
