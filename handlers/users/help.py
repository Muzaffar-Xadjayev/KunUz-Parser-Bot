from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def help_user(message: types.Message):
    msg = f"Help Commmunity\n" \
          f"This bot can parse news from news site."

    await message.reply(msg)

