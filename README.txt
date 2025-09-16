# Medical Hub – Ready-to-Run Flask App

## Quick Start
1) In VS Code: open this folder.
2) Create a virtual env and activate it.
3) Install deps: `pip install -r requirements.txt`
4) Copy `.env.example` to `.env` and fill SMTP settings if you want emails.
5) Run: `python run.py`
6) Open http://127.0.0.1:5000

- Register requires accepting Terms.
- A welcome email is sent (if SMTP configured).
- Forgot/reset password flows at /auth/forgot (token valid 1h).

DB tables are auto-created on first run; later you can enable migrations:
```
python -m flask --app run db init
python -m flask --app run db migrate -m "init"
python -m flask --app run db upgrade
```
