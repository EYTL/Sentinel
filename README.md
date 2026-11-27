# Sentinel

A self-healing uptime and incident monitor. It watches services, detects failures,
restarts them automatically, records every incident and sends an alert.

> Status: Phase 0 (skeleton). See [PLAN.md](PLAN.md) for the daily checklist.

## How it works

```
every N seconds
     |
     v
 Is the service OK? --yes--> do nothing
     | no
     v
 Failed 3 times in a row? --no--> keep watching
     | yes
     v
 Restart the container --> record the incident --> send an alert
                      (cooldown before the next restart)
```

## What I'm building it to practise
Linux, Python, Docker, Git, tests (pytest), CI (GitHub Actions) and AWS (EC2).

## Run it
TODO (fill in once it works): how to install, configure and start Sentinel.

## What I learned
TODO (fill in at the end).
