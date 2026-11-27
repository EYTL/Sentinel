"""demo_service/app.py: a tiny web app that Sentinel will watch, and that you can break on purpose.

PHASE 1.

WHAT TO BUILD (Flask; 15 lines or fewer is plenty)
- GET /health  -> answers "OK" with status 200, while the service is "healthy".
- GET /break   -> flips an internal switch so /health starts answering with status 500.
- GET /fix     -> flips it back (optional; Sentinel's restart should also fix it).
- Run it on port 5000, listening on all interfaces (host "0.0.0.0") so Docker can expose it.

WHY IT EXISTS
Sentinel needs something to watch. This lets you cause a failure whenever you like,
which is perfect for testing and for your demo GIF.

IDEA FOR A REAL CRASH
Also add a /crash route that stops the whole process (look up `os._exit`).
Docker then shows the container as exited, and Sentinel has to restart it.

HOW YOU KNOW IT WORKS (your proof)
- Open http://localhost:5000/health in a browser: OK.
- Open /break, then /health: now it fails.

LEARN FIRST: the Flask "Quickstart" page (routes and returning a status code).
"""

# TODO: write your code below this line.
