from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id
        for admin in ADMINS:
            if int(user_id) == int(admin):
                return True
            else:
                return False

