#!/usr/bin/env python3
"""
סקריפט ליצירת משתמשי דמה מבתי חולים שונים
"""

from app import create_app
from app.models import User, Post
from app.extensions import db
from datetime import datetime, timedelta
import random

def create_hospital_users():
    app = create_app()
    
    with app.app_context():
        # יצירת הטבלאות במסד הנתונים
        db.create_all()
        
        # בדיקה אם כבר יש משתמשים רבים
        existing_count = User.query.count()
        if existing_count >= 10:
            print(f"כבר יש {existing_count} משתמשים במערכת!")
            return
        
        # רשימת משתמשי דמה מבתי חולים שונים
        users_data = [
            {
                'email': 'dr.cohen@hadassah.org.il',
                'full_name': 'ד"ר דוד כהן',
                'specialty': 'neurology',
                'workplace': 'הדסה עין כרם',
                'location': 'ירושלים',
                'bio': 'נוירולוג בכיר עם התמחות במחלות נוירו-דגנרטיביות. 15 שנות ניסיון בטיפול בפרקינסון ואלצהיימר.',
                'experience_years': 15,
                'education': 'תואר ברפואה - האוניברסיטה העברית\nהתמחות נוירולוגיה - הדסה',
                'certifications': 'בורד נוירולוגיה\nהסמכה ב-EEG',
                'languages': 'עברית, אנגלית, רוסית'
            },
            {
                'email': 'dr.levy@ichilov.health.gov.il',
                'full_name': 'ד"ר מיכל לוי',
                'specialty': 'radiology',
                'workplace': 'איכילוב',
                'location': 'תל אביב',
                'bio': 'רדיולוגית מומחית בהדמיית חזה וצילומי CT. מתמחה באבחון מוקדם של מחלות ריאה.',
                'experience_years': 8,
                'education': 'תואר ברפואה - אוניברסיטת תל אביב\nהתמחות רדיולוגיה - איכילוב',
                'certifications': 'בורד רדיולוגיה\nהסמכה ב-CT חזה',
                'languages': 'עברית, אנגלית, צרפתית'
            },
            {
                'email': 'dr.rosen@sheba.health.gov.il',
                'full_name': 'ד"ר אבי רוזן',
                'specialty': 'surgery',
                'workplace': 'שיבא',
                'location': 'רמת גן',
                'bio': 'מנתח כירורג כללי ומנתח לפרוסקופי. מתמחה בניתוחי בטן וכירורגיה מינימלית פולשנית.',
                'experience_years': 12,
                'education': 'תואר ברפואה - אוניברסיטת תל אביב\nהתמחות כירורגיה - שיבא',
                'certifications': 'בורד כירורגיה כללית\nהסמכה בכירורגיה לפרוסקופית',
                'languages': 'עברית, אנגלית'
            },
            {
                'email': 'dr.goldberg@rambam.health.gov.il',
                'full_name': 'ד"ר רחל גולדברג',
                'specialty': 'pediatrics',
                'workplace': 'רמבם',
                'location': 'חיפה',
                'bio': 'רופאת ילדים מומחית בקרדיולוגיה ילדים. מטפלת במומים מולדים של הלב וטיפולים התערבותיים.',
                'experience_years': 10,
                'education': 'תואר ברפואה - הטכניון\nהתמחות רפואת ילדים - רמבם\nעמיתות קרדיולוגיה ילדים',
                'certifications': 'בורד רפואת ילדים\nבורד קרדיולוגיה ילדים',
                'languages': 'עברית, אנגלית, גרמנית'
            },
            {
                'email': 'dr.katz@beilinson.clalit.org.il',
                'full_name': 'ד"ר יוסף כץ',
                'specialty': 'emergency',
                'workplace': 'בילינסון',
                'location': 'פתח תקווה',
                'bio': 'רופא מיון בכיר עם ניסיון רב בטיפול בחולים קריטיים וטראומה. מדריך בקורסי החייאה.',
                'experience_years': 7,
                'education': 'תואר ברפואה - אוניברסיטת בן גוריון\nהתמחות רפואה דחופה - בילינסון',
                'certifications': 'בורד רפואה דחופה\nמדריך ACLS\nמדריך ATLS',
                'languages': 'עברית, אנגלית, ספרדית'
            },
            {
                'email': 'dr.ben-david@soroka.health.gov.il',
                'full_name': 'ד"ר שרה בן-דוד',
                'specialty': 'gynecology',
                'workplace': 'סורוקה',
                'location': 'באר שבע',
                'bio': 'גינקולוגית מומחית בפוריות ורפואת נשים. מתמחה בטיפולי IVF וכירורגיה גינקולוגית.',
                'experience_years': 9,
                'education': 'תואר ברפואה - אוניברסיטת בן גוריון\nהתמחות גינקולוגיה - סורוקה',
                'certifications': 'בורד גינקולוגיה\nהסמכה ברפואת פוריות',
                'languages': 'עברית, אנגלית, רוסית'
            },
            {
                'email': 'dr.private@clinic.co.il',
                'full_name': 'ד"ר אלון פרטי',
                'specialty': 'dermatology',
                'workplace': 'קליניקה פרטית',
                'location': 'הרצליה',
                'bio': 'רופא עור פרטי המתמחה בכירורגיית עור ואסתטיקה רפואית. מטפל בסרטן עור ומחלות עור.',
                'experience_years': 6,
                'education': 'תואר ברפואה - אוניברסיטת תל אביב\nהתמחות עור - איכילוב',
                'certifications': 'בורד רפואת עור\nהסמכה בלייזר רפואי',
                'languages': 'עברית, אנגלית, איטלקית'
            }
        ]
        
        created_users = []
        
        for user_data in users_data:
            # בדיקה אם המשתמש כבר קיים
            existing = User.query.filter_by(email=user_data['email']).first()
            if existing:
                print(f"משתמש {user_data['email']} כבר קיים")
                continue
            
            # יצירת משתמש חדש
            user = User(
                email=user_data['email'],
                full_name=user_data['full_name'],
                specialty=user_data['specialty'],
                workplace=user_data['workplace'],
                location=user_data['location'],
                bio=user_data['bio'],
                experience_years=user_data['experience_years'],
                education=user_data['education'],
                certifications=user_data['certifications'],
                languages=user_data['languages'],
                is_verified=True,
                role='member'
            )
            user.set_password('123456')  # סיסמה אחידה לכל המשתמשים
            
            db.session.add(user)
            created_users.append(user)
        
        # שמירת כל המשתמשים
        db.session.commit()
        
        # יצירת פוסטים לכל משתמש
        post_templates = [
            {
                'title': 'מקרה מעניין מהמחלקה',
                'content': 'רוצה לשתף מקרה מעניין שטיפלתי בו השבוע. המטופל הגיע עם תסמינים לא ברורים...',
                'post_type': 'case'
            },
            {
                'title': 'שאלה מקצועית לעמיתים',
                'content': 'יש לי שאלה בנוגע לטיפול במטופל מורכב. מישהו נתקל במצב דומה?',
                'post_type': 'question'
            },
            {
                'title': 'עדכון על מחקר חדש',
                'content': 'קראתי מחקר מעניין שפורסם לאחרונה בתחום שלי. הנה התובנות העיקריות...',
                'post_type': 'research'
            }
        ]
        
        for user in created_users:
            # יצירת 1-2 פוסטים לכל משתמש
            num_posts = random.randint(1, 2)
            for i in range(num_posts):
                template = random.choice(post_templates)
                post = Post(
                    title=f"{template['title']} - {user.workplace}",
                    content=template['content'],
                    post_type=template['post_type'],
                    tags=f"{user.specialty}, {user.workplace}",
                    user_id=user.id,
                    created_at=datetime.utcnow() - timedelta(days=random.randint(1, 30))
                )
                db.session.add(post)
        
        db.session.commit()
        
        print(f"✅ נוצרו {len(created_users)} משתמשי דמה מבתי חולים שונים!")
        print("כל המשתמשים עם סיסמה: 123456")
        print("\nמשתמשים שנוצרו:")
        for user in created_users:
            print(f"- {user.full_name} ({user.email}) - {user.workplace}")
        
        print(f"\n✅ נוצרו גם פוסטים לכל המשתמשים!")
        print("עכשיו תוכלי לבדוק את החיפוש המתקדם!")

if __name__ == '__main__':
    create_hospital_users()
