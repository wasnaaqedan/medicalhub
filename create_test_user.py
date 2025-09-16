#!/usr/bin/env python3
"""
סקריפט ליצירת משתמש דמה לבדיקת איפוס סיסמה
"""

from app import create_app
from app.models import User, Post
from app.extensions import db
from datetime import datetime, timedelta

def create_test_user():
    app = create_app()
    
    with app.app_context():
        # יצירת הטבלאות במסד הנתונים
        db.create_all()
        
        # בדיקה אם המשתמש כבר קיים
        try:
            existing_user = User.query.filter_by(email='test@medical-hub.com').first()
            if existing_user:
                print("משתמש דמה כבר קיים!")
                print(f"אימייל: {existing_user.email}")
                print(f"שם: {existing_user.full_name}")
                return
        except Exception as e:
            print(f"יוצר מסד נתונים חדש... {e}")
            db.create_all()
        
        # יצירת משתמש דמה עם מידע מלא
        user = User(
            email='test@medical-hub.com',
            full_name='ד"ר שרה כהן',
            is_verified=True,
            role='member',
            bio='רופאה קרדיולוגית עם ניסיון של 10 שנים בטיפול במחלות לב. מתמחה באבחון וטיפול במחלות כלי דם.',
            specialty='cardiology',
            workplace='בית חולים הדסה עין כרם',
            location='ירושלים',
            experience_years=10,
            education='תואר ראשון ברפואה - האוניברסיטה העברית\nהתמחות בקרדיולוגיה - בית חולים הדסה',
            certifications='רישיון רופא - משרד הבריאות\nבורד ישראלי בקרדיולוגיה\nהסמכה באקו לב',
            languages='עברית, אנגלית, ערבית'
        )
        user.set_password('123456')  # סיסמה פשוטה לבדיקה
        
        db.session.add(user)
        db.session.commit()
        
        # יצירת פוסטים דמה
        posts_data = [
            {
                'title': 'מקרה מעניין: חולה עם כאבי חזה אטיפיים',
                'content': 'מטופל בן 45, מגיע עם כאבי חזה לא אופייניים שנמשכים כשבוע. EKG תקין, טרופונין שלילי. בדיקת stress test הראתה שינויים קלים. מה הצעד הבא? האם יש צורך בקטטר?',
                'post_type': 'case',
                'tags': 'קרדיולוגיה, כאבי חזה, אבחון',
                'created_at': datetime.utcnow() - timedelta(days=2)
            },
            {
                'title': 'המלצה על מחקר חדש בטיפול בהיפרטנזיה',
                'content': 'קראתי מחקר מעניין שפורסם השבוע ב-NEJM על שילוב תרופות חדש לטיפול בלחץ דם גבוה. התוצאות מרשימות - ירידה של 25% בסיכון לאירועים קרדיווסקולריים.',
                'post_type': 'research',
                'tags': 'היפרטנזיה, מחקר, טיפול',
                'created_at': datetime.utcnow() - timedelta(days=5)
            },
            {
                'title': 'ניסיון עם אבחון מוקדם של אוטם שריר הלב',
                'content': 'השבוע הצלנו חיים של מטופל צעיר שהגיע עם תסמינים לא אופייניים. חשוב לזכור שגם בצעירים יכול להיות אוטם, במיוחד עם גורמי סיכון כמו עישון ומשפחתיות.',
                'post_type': 'experience',
                'tags': 'אוטם, אבחון מוקדם, מניעה',
                'created_at': datetime.utcnow() - timedelta(days=1)
            }
        ]
        
        for post_data in posts_data:
            post = Post(
                title=post_data['title'],
                content=post_data['content'],
                post_type=post_data['post_type'],
                tags=post_data['tags'],
                user_id=user.id,
                created_at=post_data['created_at']
            )
            db.session.add(post)
        
        db.session.commit()
        
        print("✅ משתמש דמה נוצר בהצלחה!")
        print("אימייל: test@medical-hub.com")
        print("סיסמה: 123456")
        print("✅ נוצרו 3 פוסטים דמה")
        print("עכשיו תוכלי לבדוק את הפרופיל המלא!")

if __name__ == '__main__':
    create_test_user()
