from aiogram import Dispatcher
from aiogram import types


async def set_default_commands(dp: Dispatcher) -> None:
    commands = [
        types.BotCommand("start", "Запустить / обновить бота"),
        types.BotCommand("filter_start", "Поиск задач"),
        types.BotCommand("help", "Помощь"),
    ]
    print("### The default COMMANDS setup has been completed")
    await dp.bot.set_my_commands(commands)


async def set_default_menu(dp: Dispatcher) -> None:
    menu = types.MenuButtonCommands()
    print("### The default MENU setup has been completed")
    await dp.bot.set_chat_menu_button(menu_button=menu)


async def on_startup(dp: Dispatcher) -> None:
    await set_default_commands(dp)
    await set_default_menu(dp)
