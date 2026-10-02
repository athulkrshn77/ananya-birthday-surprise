from flask import Flask, render_template, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

# =========================
# BIRTHDAY SETTINGS
# =========================
HER_NAME = "Ananya"

# 17 November 2026, 12:00 AM IST
BIRTHDAY_DATE = "2026-11-17"
BIRTHDAY_TIME = "00:00:00"
BIRTHDAY_ISO = f"{BIRTHDAY_DATE}T{BIRTHDAY_TIME}+05:30"

BIRTHDAY_MESSAGE = """Happy Birthday, my love ❤️🎂

You are my happiness, my favorite person, and the most beautiful part of my life. 🫶🏻 I’m so lucky to have you. May your smile always stay the same. ❤️

Love you forever! 🥹💗"""

@app.route("/")
def home():
    return render_template(
        "index.html",
        her_name=HER_NAME,
        birthday_iso=BIRTHDAY_ISO,
        message=BIRTHDAY_MESSAGE
    )

# Server-time endpoint. This prevents changing the phone's clock
# from being the source of truth for the unlock.
@app.route("/api/time")
def server_time():
    now = datetime.now(timezone.utc)
    unlock = datetime.fromisoformat(BIRTHDAY_ISO).astimezone(timezone.utc)
    return jsonify({
        "now": now.isoformat(),
        "unlock": unlock.isoformat(),
        "unlocked": now >= unlock
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
