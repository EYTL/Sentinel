"""Tests for the failure counter, cooldown and incidents (PHASE 3).

Ideas (write each as a small function starting with test_):

1. The failure counter does not trigger a restart at 1 or 2 failures, but does at 3.
2. A successful check resets the counter to zero.
3. After a restart, a second restart inside the cooldown is refused.
4. An incident that opens and closes records a duration of the right size
   (look up how to fake the time: pass the time in as an argument, which makes it testable).
5. config.yaml loads and has the keys you expect.

TIP: functions that take their inputs as arguments and return a value are easy to test.
If something is hard to test, that often means the function does too much.

Run them with:  pytest -q
"""
