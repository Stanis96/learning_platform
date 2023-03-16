import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TELEGRAM_BOT_TOKEN

from .base_commands import Basic
from .start_commands import on_startup
from .task_commands import FilterTasks


TELEGRAM_BOT_TOKEN = TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def run_bot() -> None:
    print("### Bot started")
    Basic(dp)
    FilterTasks(dp)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
