"""main.py: the loop that ties everything together.

PHASE 1 (basic loop) -> PHASE 2 (failure counting, recovery, incidents, alerts).

THE LOOP, IN PLAIN WORDS
1. Load config.yaml (look up `yaml.safe_load`).
2. Forever, every `interval_seconds`:
     for each service in the config:
         result = check it                      (checks.py)
         if result.ok:
             reset that service's failure counter to 0
             if an incident was open: close it and alert "recovered"   (incidents.py, notify.py)
         else:
             add 1 to that service's failure counter
             if the counter reached `failure_threshold`:
                 open an incident and alert "down"
                 restart its container (unless the cooldown says wait)  (recover.py)
3. Print a short status line for every check, with a timestamp.

THINGS TO KEEP IN MIND
- Keep the failure counters in a dictionary: {service_name: count}.
- One broken service must never stop Sentinel from checking the others.
- Let the user stop it cleanly with Ctrl+C (look up KeyboardInterrupt).
- Write this in small steps: first just print the check results in a loop,
  and only then add counting, recovery and incidents.

HOW YOU KNOW IT WORKS (your proof)
- `python -m sentinel.main` prints a check line every 10 seconds.
- After you break demo-service: counter climbs, then restart, then "recovered".
"""

# TODO: write your code below this line.
