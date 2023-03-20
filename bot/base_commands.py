from aiogram import Dispatcher
from aiogram import types


class BaseLogic:
    def __init__(self, dp: Dispatcher) -> None:
        self._register(dp)

    def _register(self, dp: Dispatcher) -> None:
        raise NotImplementedError


class Basic(BaseLogic):
    def _register(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.command_start, commands="start")
        dp.register_message_handler(self.command_help, commands="help")

    @staticmethod
    async def command_start(message: types.Message) -> None:
        text = "Здравствуй, пользователь!\nЯ, LP Bot, помогу подобрать для тебя задачи!"

        disclaimer = """Бот реализован для поиска задач.\n
Ресурс: [Codeforces](https://codeforces.com/problemset?order=BY_SOLVED_DESC).\n
📝Данный проект выполнен исключительно в учебных целях в рамках тестового задания.\n"""
        await message.reply(text)
        await message.answer(disclaimer, parse_mode="Markdown")

    @staticmethod
    async def command_help(message: types.Message) -> None:
        text = "За помощью к @Stanis_96"
        await message.reply(text)
