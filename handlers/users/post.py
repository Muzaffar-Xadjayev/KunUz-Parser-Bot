from aiogram import types, Dispatcher
from filters.check_admin import IsAdmin
from utils.misc.get_posts import posts


async def get_posts(message: types.Message):
    news = posts("https://kun.uz/news/category/jahon")
    for n in news:
        await message.answer_photo(n["img"],
                                   caption=f"Title: {n['title']}\n\n"
                                           f"<em>{n['date'][:200]}</em>")


def register_post_handler(dp: Dispatcher):
    dp.register_message_handler(get_posts, IsAdmin(), commands=["posts"])
