from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup

from service_parsing_data.utils import get_difficulty
from service_parsing_data.utils import get_topics

from .base_commands import BaseLogic


class FilterForm(StatesGroup):
    topic = State()
    search_terms = State()
    request = State()


class FilterTasks(BaseLogic):
    def _register(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.filter_start, commands="filter_start")
        dp.register_message_handler(self.filter_difficulty, state=FilterForm.topic)

    @staticmethod
    async def filter_start(message: types.Message) -> None:
        await FilterForm.topic.set()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        topics = get_topics().values_list("topic", flat=True)
        markup.add(*topics)

        await message.reply("Выбери тему задачи", reply_markup=markup)

    @staticmethod
    async def filter_difficulty(message: types.Message):
        topic = message.text
        difficulties = get_difficulty(topic)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        for difficulty in difficulties:
            markup.add(types.KeyboardButton(difficulty))
        await message.reply("Выбери сложность задачи", reply_markup=markup)
