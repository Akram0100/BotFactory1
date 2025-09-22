Telegram botini bosqichma-bosqich yaratish
Telegram bot yaratish: BotFather, token, polling/webhook va admin panel integratsiyasi
# Kirish
Telegram bot yaratish juda oson, lekin to'g'ri arxitektura va xavfsizlik bilan ishlash muhim.

## 1. BotFather va token
- @BotFather ga /newbot yuboring
- Tokenni oling va sir saqlang

## 2. Arxitektura
- Polling yoki Webhook
- Bizning loyihada markaziy `bot_manager` orqali polling

## 3. Xabar oqimi
- `update_id` deduplikatsiya
- Komanda va matn handlerlari

## 4. Xavfsizlik
- CSRF faqat HTTP formlar uchun
- Token .env yoki DB'da

## 5. Admin panel
- Start/Stop tugmalari
- Mijozlarga xabar yuborish

Yakun: Minimal prototipni ishlab, loglar va kuzatuv bilan mustahkamlang.
