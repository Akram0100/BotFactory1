import os, sys
from datetime import datetime, timedelta
# Ensure project root is importable when running from scripts/
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from app import app, db
from models import User, Bot, KnowledgeBase, BotCustomer, ChatHistory

KEYS = [
    'SESSION_SECRET','DATABASE_URL','GOOGLE_API_KEY','SUPPORT_PHONE','SUPPORT_TELEGRAM',
    'SMTP_HOST','SMTP_PORT','SMTP_USER','SMTP_PASSWORD','FROM_EMAIL',
    'ESKIZ_EMAIL','ESKIZ_PASSWORD','PLAYMOBILE_LOGIN','PLAYMOBILE_PASSWORD'
]

def mask(v: str):
    if not v:
        return '—'
    v = str(v)
    if len(v) <= 4:
        return '*' * len(v)
    return v[:2] + '***' + v[-2:]


def env_report():
    print('ENV CHECK:')
    for k in KEYS:
        val = os.environ.get(k)
        status = 'OK' if val else 'MISSING'
        print(f" - {k}: {status}{' ('+mask(val)+')' if val else ''}")
    print()


def db_kb_report():
    with app.app_context():
        bots = Bot.query.all()
        print(f"BOTS: {len(bots)}")
        for b in bots:
            total = KnowledgeBase.query.filter_by(bot_id=b.id).count()
            by_type = {}
            for ct in ['product','image','file','text']:
                by_type[ct] = KnowledgeBase.query.filter_by(bot_id=b.id, content_type=ct).count()
            print(f" - Bot #{b.id} '{b.name}' [{b.platform}] active={b.is_active} KB total={total} types={by_type}")
        print()


def users_customers_report():
    with app.app_context():
        total_users = User.query.count()
        t_users_tg = User.query.filter(User.telegram_id.isnot(None)).count()
        paid_users = User.query.filter(User.subscription_type.in_(['starter','basic','premium'])).count()
        free_users = User.query.filter(User.subscription_type=='free').count()
        print(f"USERS: total={total_users}, telegram_id={t_users_tg}, paid={paid_users}, free={free_users}")
        cust_tg = BotCustomer.query.filter_by(platform='telegram').count()
        cust_ig = BotCustomer.query.filter_by(platform='instagram').count()
        cust_wa = BotCustomer.query.filter_by(platform='whatsapp').count()
        print(f"BOT CUSTOMERS: tg={cust_tg}, ig={cust_ig}, wa={cust_wa}")
        print()


def segment_counts():
    with app.app_context():
        now = datetime.utcnow()
        # trial_14 approx
        trial = User.query.filter(User.subscription_type=='free').count()
        cutoff30 = now - timedelta(days=30)
        active_user_subq = db.session.query(ChatHistory.user_telegram_id).filter(ChatHistory.created_at>=cutoff30).subquery()
        active_users_30d = User.query.filter(User.telegram_id.isnot(None), User.telegram_id.in_(active_user_subq)).count()
        paid = User.query.filter(User.subscription_type.in_(['starter','basic','premium'])).count()
        unpaid = User.query.filter(User.subscription_type=='free').count()
        # customers active 30d
        cust_active_30d = BotCustomer.query.filter(BotCustomer.last_interaction>=cutoff30).count()
        print('SEGMENTS:')
        print(f" - trial_14 (approx free): {trial}")
        print(f" - active_30d (platform users): {active_users_30d}")
        print(f" - active_30d (bot customers): {cust_active_30d}")
        print(f" - paid: {paid}")
        print(f" - unpaid: {unpaid}")
        print()


def bot_tokens_report():
    with app.app_context():
        bots = Bot.query.all()
        print('BOT TOKENS:')
        for b in bots:
            has_tg = bool(b.telegram_token)
            has_ig = bool(b.instagram_token)
            has_wa = bool(b.whatsapp_token and b.whatsapp_phone_id)
            print(f" - Bot #{b.id} '{b.name}': TG={has_tg}, IG={has_ig}, WA={has_wa}, active={b.is_active}")
        print()

if __name__ == '__main__':
    env_report()
    db_kb_report()
    users_customers_report()
    segment_counts()
    bot_tokens_report()
