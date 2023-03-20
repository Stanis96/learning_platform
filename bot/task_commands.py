import asyncio

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup

from service_parsing_data.models import Tasks
from service_parsing_data.utils import get_difficulty
from service_parsing_data.utils import get_topics

from .base_commands import BaseLogic


class FilterForm(StatesGroup):
    topic = State()
    difficulty = State()


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
    async def filter_difficulty(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data["topic"] = message.text
            await FilterForm.next()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            difficulties = get_difficulty(data["topic"])
            for difficulty in difficulties:
                markup.add(types.KeyboardButton(difficulty))
            await message.reply("Выбери сложность задачи", reply_markup=markup)

    @staticmethod
    async def filter_result(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data["difficulty"] = message.text
            await FilterForm.next()
            markup = types.ReplyKeyboardRemove()
            topic_request = f"Тема задач: {data['topic']}\n"
            difficulty_request = f"Сложность задач: {data['difficulty']}"
            answer_text = "\n\nВот задачи, которые мне удалось найти по вашему запросу:"
            text = topic_request + difficulty_request + answer_text
            await message.reply(text, reply_markup=markup)
            tasks = Tasks.objects.filter(
                topic__topic=data["topic"], difficulty=int(data["difficulty"])
            ).order_by("count_solved")[:10]
            count = Tasks.objects.filter(
                topic__topic=data["topic"], difficulty=int(data["difficulty"])
            ).count()

            if not tasks.exists():
                await message.reply("По вашему запросу задач нет.")
            else:
                for task in tasks:
                    await message.reply(
                        f"Номер: {task.number}\nНазвание: {task.title}\nСсылка: {task.link}\n"
                        f"Количество решивших задачу: {task.count_solved}"
                    )

                if count > 10:
                    await message.reply(
                        f"Также, еще доступные задачи по вашему запросу: {count - 10}.\n"
                        f" Хотите получить их?"
                    )
            await state.finish()
