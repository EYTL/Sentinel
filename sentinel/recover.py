"""recover.py: fix a failed service by restarting its Docker container.

PHASE 2.

WHAT TO BUILD
A function:  restart_container(container_name) -> True if the restart worked, else False

- Start with the `subprocess` module to run the same command you would type:
      docker restart <container_name>
  (The Docker Python SDK is a later upgrade. Keep it simple first.)
- Check the command's return code to know if it worked.
- Never pass user-typed text into a shell string. Pass a list of arguments instead
  (look up why: "command injection").

COOLDOWN (the part interviewers like)
- Keep track of WHEN each container was last restarted.
- If it was restarted less than `cooldown_seconds` ago, do not restart it again.
- Why: if a service is truly broken, restarting it every second just makes things worse.
  The cooldown gives it time, and the alert tells a human it needs help.

HOW YOU KNOW IT WORKS (your proof)
- Start demo-service in Docker, stop it with `docker stop demo-service`, call your function,
  and `docker ps` shows it running again.
- Call it twice quickly: the second call is refused because of the cooldown.
"""

# TODO: write your code below this line.
