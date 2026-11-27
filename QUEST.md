# SENTINEL: The System

You are an E-Rank Engineer. Your Sentinel is asleep. Clear the gates to wake it.

**The one law: XP is earned only with PROOF.** Reading and watching earn nothing until something runs.

## Player card

| Field | Value |
|---|---|
| Rank | Unranked |
| Total XP | 0 / 1500 |
| Current streak | 0 days |
| Best streak | 0 days |

## Daily quests (bonus XP, on top of the 1500)

- +10 XP: one real commit
- +5 XP: 3 lines in LOG.md
- +5 XP: each job application sent (max +25 a day)
- +10 XP: 30 minutes of Boot.dev Python with a lesson completed

---

## Gate 0: Awakening (Nov 27-28)
- [ ] 10 XP: Git identity set (`git config --global --list` shows it)
- [ ] 30 XP: Skeleton pushed to GitHub
- [ ] 20 XP: `pytest -q` runs in your virtual environment
- [ ] **BOSS, 40 XP, "First Blood":** tick Phase 0 in PLAN.md, commit and push it yourself

**Clear reward: E-Rank**

## Gate 1: The Watcher (until Dec 4)
- [ ] 60 XP: `check_http` handles a live URL and a dead one without crashing
- [ ] 40 XP: `demo_service` answers /health and breaks on /break
- [ ] 50 XP: `demo_service` runs in Docker
- [ ] 50 XP: Sentinel loops over `config.yaml`
- [ ] 40 XP: AWS Cloud Practitioner exam booked
- [ ] 40 XP: 5 applications sent
- [ ] **BOSS, 60 XP, "The Silent Failure":** break the service, and Sentinel reports DOWN with no help from you

**Clear reward: D-Rank. Skill unlocked: [Detection]**

## Gate 2: The Phoenix (until Dec 11)
- [ ] 40 XP: failure counter climbs and resets
- [ ] 60 XP: `restart_container` works
- [ ] 60 XP: cooldown stops a restart loop
- [ ] 60 XP: incident log records a real outage with its duration
- [ ] 40 XP: alert on open and on close
- [ ] **BOSS, 100 XP, "Rise Again":** run `docker stop demo-service`, touch nothing, and record it coming back

**Clear reward: C-Rank. Skill unlocked: [Self-Healing]**

## Gate 3: The Green Shield (until Dec 18)
- [ ] 100 XP: 5 tests (20 XP each)
- [ ] 80 XP: CI badge is green
- [ ] **BOSS, 70 XP, "The Saboteur":** on a new branch, plant a bug, open a pull request, watch CI turn red, fix it, watch it turn green

**Clear reward: B-Rank. Skill unlocked: [CI Guard]**

## Gate 4: The Showcase (until Dec 25)
- [ ] 50 XP: README with a diagram and run steps
- [ ] 60 XP: 30-second demo GIF
- [ ] 40 XP: Sentinel added to LinkedIn and your resume
- [ ] **BOSS, 80 XP, "The Stranger":** in a fresh folder, clone your repo and get it running using ONLY the README
- [ ] Hidden quest, +100 bonus XP: run Sentinel on EC2 for a day, then shut the instance down

**Clear reward: A-Rank. Skill unlocked: [Deployment] (only if you cleared the hidden quest)**

## Gate 5: The Monarch (until Jan 2)
- [ ] 150 XP: sit the Cloud Practitioner exam (XP for showing up)
- [ ] **FINAL BOSS, 70 XP, "The Interviewer":** record yourself explaining Sentinel in 2 minutes. Answer: why 3 failures? why a cooldown? what can't it fix?

**Clear reward: S-Rank**

---

## System rules

1. **Rank up only by beating the gate's boss.** Daily XP can't buy a rank.
2. **Never miss two days in a row.** One miss is allowed.
3. **Penalty quest** if you miss two: just 25 minutes on one small task. No guilt, no catching up on everything.
4. **No XP farming.** Editing this file, redesigning the game, making new trackers or adding to ARISE earns 0 XP.
5. **Late gate?** Don't stop. Use the cut list in PLAN.md and move on.

## Hint ladder (when a boss beats you)

1. Fight alone for 30 minutes, and write the exact error in LOG.md.
2. Ask for a **hint** (a direction, no code).
3. Ask for an **explanation** (why it happens, with a tiny unrelated example).
4. Ask for a **review** of what you wrote.

## Loot (fill these in yourself, before you start)

| Rank | My reward |
|---|---|
| E | |
| D | |
| C | |
| B | |
| A | |
| S | |
