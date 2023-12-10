from aiogram import Dispatcher
import datetime
from aiogram import types
from database.connections import *


async def bot_start(message: types.Message):
    name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    join_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await add_user(user_id, name, username, join_date)
    await message.answer("Welcome")


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["start"])
