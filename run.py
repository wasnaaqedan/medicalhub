#!/usr/bin/env python3
"""
Medical Hub - פלטפורמה רפואית ישראלית
נקודת כניסה פשוטה להרצת האפליקציה
"""

import os
import sys
from app import create_app

def main():
    """הרצת האפליקציה"""
    try:
        # יצירת האפליקציה
        app = create_app()
        
        # הגדרות פיתוח
        debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
        port = int(os.getenv('FLASK_PORT', 5000))
        host = os.getenv('FLASK_HOST', '127.0.0.1')
        
        print("=" * 60)
        print("🏥 Medical Hub - פלטפורמה רפואית ישראלית")
        print("=" * 60)
        print(f"🌐 האתר זמין בכתובת: http://{host}:{port}")
        print(f"🔧 מצב פיתוח: {'פעיל' if debug_mode else 'לא פעיל'}")
        print("=" * 60)
        print("לעצירת השרת לחץ Ctrl+C")
        print("=" * 60)
        
        # הרצת השרת
        app.run(
            host=host,
            port=port,
            debug=debug_mode,
            use_reloader=debug_mode
        )
        
    except Exception as e:
        print(f"❌ שגיאה בהרצת האפליקציה: {e}")
        print("💡 טיפים לפתרון:")
        print("   1. ודא שהסביבה הווירטואלית פעילה")
        print("   2. התקן את התלויות: pip install -r requirements.txt")
        print("   3. בדוק שהתיקייה instance קיימת")
        sys.exit(1)

if __name__ == "__main__":
    main()