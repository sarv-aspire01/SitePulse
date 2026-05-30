import os
import requests
from dotenv import load_dotenv

from models.notification_message import NotificationMessage

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message: str) -> bool:

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram not configured")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }

    try:
        r = requests.post(url, json=payload, timeout=15)
        r.raise_for_status()
        return True

    except Exception as e:
        print(f"Telegram send failed: {e}")
        return False


def send_notification(notification: NotificationMessage) -> bool:

    message = f"{notification.title}\n\n{notification.body}"

    return send_telegram_message(message)