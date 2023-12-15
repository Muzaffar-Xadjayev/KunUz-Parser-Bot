from playhouse.shortcuts import model_to_dict
from data.config import ADMINS
from loader import bot
from .models import User


async def add_user(user_id, full_name, username, join_date):
    if not User.select().where(User.telegram_id == user_id).exists():
        User.create(
            telegram_id=user_id,
            full_name=full_name,
            username=username,
            join_date=join_date
        )
        c = User.select()
        count = [model_to_dict(item) for item in c]
        msg = f"<a href='tg://user?id={user_id}'>{full_name}</a> bazaga qo'shildi. " \
              f"Bazada {len(count)} ta foydalanuvchi bor"
        for admin in ADMINS:
            await bot.send_message(admin, msg)


async def get_all_users():
    us = User.select()
    user = [model_to_dict(item) for item in us]
    return user
