"""checks.py: ask a service "are you alive?" and report the answer.

PHASE 1. Build this first.

WHAT TO BUILD
1. A small result type that carries one check's outcome. Look up `dataclasses`.
   Fields: name, ok (True/False), latency_ms, detail (a short message, e.g. "HTTP 200" or "timeout").

2. A function:  check_http(name, url, timeout) -> the result type
   - Send a GET request to `url` (the `requests` library).
   - Measure how long it took.
   - ok is True only if the status code is 200.
   - It must NEVER crash when the service is down. A dead service is a normal answer
     ("ok=False, detail=connection refused"), not an exception. Look up try/except
     and requests.exceptions.

HOW YOU KNOW IT WORKS (your proof)
- Point it at a URL that works (e.g. https://example.com): ok=True and a latency.
- Point it at http://localhost:1 (nothing there): ok=False, no crash.

LEARN FIRST (15 minutes)
- Boot.dev Python lessons on functions, dictionaries and exceptions.
- requests docs: "Quickstart" and "Timeouts".
"""

# TODO: write your code below this line.
