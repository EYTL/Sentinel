"""notify.py: tell a human when something happened.

PHASE 2. Start simple, upgrade later.

LEVEL 1 (do this first)
- send_alert(message): print the message with a timestamp, and also append it to the log.

LEVEL 2 (optional upgrade): Telegram
- Create a bot with @BotFather in Telegram. It gives you a token.
- Send a message with an HTTP POST to the Telegram Bot API (the `requests` library again).
- Read the token and chat id from ENVIRONMENT VARIABLES (see .env.example), using `os.environ`.
- NEVER write the token in your code or commit it to Git.
- If sending fails (no internet), do not crash Sentinel: catch the error and log it.

HOW YOU KNOW IT WORKS (your proof)
- You receive a message (or see a log line) when an incident opens and again when it closes.
"""

# TODO: write your code below this line.
