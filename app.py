#!/usr/bin/env python3
"""
Medical Hub - פלטפורמה רפואית ישראלית
נקודת הכניסה הראשית של האפליקציה
"""

import os
from app import create_app

# יצירת האפליקציה
app = create_app()

if __name__ == "__main__":
    # הגדרות פיתוח
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=True
    )
