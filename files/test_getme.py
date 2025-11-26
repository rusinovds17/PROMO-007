import os, asyncio
from aiogram import Bot
try:
    from dotenv import load_dotenv
    load_dotenv()  # подтянет BOT_TOKEN из .env, если он есть
except Exception:
    pass

async def main():
    token = os.getenv("BOT_TOKEN") or "ВСТАВЬТЕ_ТОКЕН_ЗДЕСЬ"
    print("TOKEN preview:", repr(token)[:30], "len=", len(token))
    bot = Bot(token=token)
    me = await bot.get_me()  # если токен неверный — упадёт здесь с 401
    print(f"OK: @{me.username} (id={me.id})")

asyncio.run(main())
