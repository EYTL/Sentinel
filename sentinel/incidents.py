"""incidents.py: keep a record of every outage.

PHASE 2.

WHAT TO BUILD
An incident is "service X was down from time A to time B".
- open_incident(service_name): remember when the outage started (only if one isn't open already).
- close_incident(service_name): when the service is healthy again, work out how long it was down.
- Write each finished incident as one line to `incidents.log` (path comes from config.yaml).
  A simple format is JSON per line, for example:
      {"service": "demo-service", "started": "...", "ended": "...", "duration_seconds": 64}
  Look up: the `json` module, `datetime`, and opening a file in append mode ("a").

IMPORTANT DETAIL
- An incident must open once, not every failed check. Use a dictionary
  {service_name: start_time} to remember what is currently open.

HOW YOU KNOW IT WORKS (your proof)
- Break demo-service, wait for the restart, and incidents.log has ONE line with a sensible duration.
"""

# TODO: write your code below this line.
