from aiogram import types
from aiogram import Dispatcher
from keyboards.inline.admin_command import admin_command
from database.connections import *


async def intro_admin(message: types.Message):
    btn = await admin_command()
    await message.answer(f"Xush kelibsiz {message.from_user.first_name} – ADMIN", reply_markup=btn)


async def get_users(call: types.CallbackQuery):
    await call.answer()
    user = await get_all_users()
    await call.message.edit_text(f"There're {len(user)} users in DataBase")


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(intro_admin, commands=["admin"])
    dp.register_callback_query_handler(get_users, text="admin:get_users")
