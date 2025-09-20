import os
from datetime import datetime, timedelta
import sys

# Ensure project root is on sys.path so we can import 'app' when running from scripts/
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app, db
from models import User
from werkzeug.security import generate_password_hash


def main():
    email = os.environ.get("ADMIN_EMAIL")
    password = os.environ.get("ADMIN_PASSWORD")

    if not email or not password:
        print("ERROR: ADMIN_EMAIL yoki ADMIN_PASSWORD environment o'zgaruvchilari berilmagan")
        return 1

    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            user.password_hash = generate_password_hash(password)
            user.is_admin = True
            user.subscription_type = 'admin'
            db.session.commit()
            print(f"Updated existing admin user: {email}")
        else:
            username = email.split('@')[0] if '@' in email else email
            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password),
                language='uz',
                subscription_type='admin',
                is_admin=True,
                subscription_start_date=datetime.utcnow(),
                subscription_end_date=datetime.utcnow() + timedelta(days=365),
            )
            db.session.add(user)
            db.session.commit()
            print(f"Created new admin user: {email}")
    return 0


if __name__ == "__main__":
    exit(main())
