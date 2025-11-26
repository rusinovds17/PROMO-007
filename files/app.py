# app.py — FastAPI + aiogram v3 (webhook)
import os
from fastapi import FastAPI, Request, HTTPException
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# импортируем твой код и готовую функцию навешивания хендлеров
import promopro_v311y as botcode

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")          # например, https://bot.example.com
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # любая случайная строка

if not (BOT_TOKEN and BASE_URL and WEBHOOK_SECRET):
    raise RuntimeError("Нужны переменные: BOT_TOKEN, BASE_URL, WEBHOOK_SECRET")

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()
botcode.setup_handlers(dp)  # используем твои хендлеры

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post(f"/webhook/{{secret}}")
async def telegram_webhook(secret: str, request: Request):
    # простой секрет в URL (можно добавить проверку заголовка X-Telegram-Bot-Api-Secret-Token)
    if secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="bad secret")
    update = types.Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    # регистрируем вебхук в Telegram
    await bot.set_webhook(
        url=f"{BASE_URL}/webhook/{WEBHOOK_SECRET}",
        secret_token=WEBHOOK_SECRET,
        drop_pending_updates=True,
    )

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
