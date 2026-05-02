"""
Run this script once to create the default admin account.
Usage: python create_admin.py
Run from the project root.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.database import SessionLocal, engine, Base
from backend.models import User
from backend.auth import get_password_hash

# --- EDIT THESE ---
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
# ------------------

Base.metadata.create_all(bind=engine)

db = SessionLocal()

existing = db.query(User).filter(User.username == ADMIN_USERNAME).first()
if existing:
    print(f"✅ Admin user '{ADMIN_USERNAME}' already exists.")
else:
    admin = User(
        username=ADMIN_USERNAME,
        hashed_password=get_password_hash(ADMIN_PASSWORD),
        role="admin",
        is_approved=True,
        government_id=None
    )
    db.add(admin)
    db.commit()
    print(f"✅ Admin user created!")

print(f"\n   Username : {ADMIN_USERNAME}")
print(f"   Password : {ADMIN_PASSWORD}")
print(f"\nYou can now log in at the frontend with these credentials.")
db.close()
