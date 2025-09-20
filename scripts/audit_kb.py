import os, sys

# Ensure project root is importable when running from scripts/
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app, db
from models import Bot, KnowledgeBase
from sqlalchemy import func

def audit():
    with app.app_context():
        bots = Bot.query.all()
        print(f"Bots: {len(bots)}")
        for b in bots:
            total = KnowledgeBase.query.filter_by(bot_id=b.id).count()
            rows = (
                db.session.query(KnowledgeBase.content_type, func.count("*"))
                .filter_by(bot_id=b.id)
                .group_by(KnowledgeBase.content_type)
                .all()
            )
            by_type = {k: int(v) for k, v in rows}
            print(f"- Bot #{b.id} '{b.name}' [{b.platform}] KB: total={total}, by_type={by_type}")
            e = KnowledgeBase.query.filter_by(bot_id=b.id).first()
            if e and e.content:
                preview = e.content[:180].replace("\n", " ")
                src = e.source_name or e.filename or "-"
                print(f"  • First entry: type={e.content_type}, source={src}, preview='{preview}'")
            else:
                print("  • No KB entries yet")

if __name__ == "__main__":
    audit()
