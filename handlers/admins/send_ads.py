import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from states.Admin import AdminAds
import builtins
from keyboards.inline.admin_command import cancel_btn
from database.connections import *
from loader import bot


async def send_ads(call: types.CallbackQuery):
    await call.answer()
    btn = await cancel_btn()
    await call.message.edit_text("Send Message", reply_markup=btn)
    await AdminAds.text.set()


async def send_msg(msg: types.Message, state: FSMContext):
    users = await get_all_users()
    text_caption = msg.caption
    text_type = msg.content_type
    text = msg.html_text
    rep_btn = msg.reply_markup

    send_user = 0
    send_error = 0
    for user in users:
        user_id = user["telegram_id"]
        try:
            if text_type == 'sticker':
                return
            elif text_type == 'text':
                await bot.send_message(chat_id=user_id, text=text, reply_markup=rep_btn)
                await asyncio.sleep(0.05)
            elif text_type == 'video':
                await bot.send_video(user_id, msg.video.file_id, caption=text_caption, reply_markup=rep_btn)
                await asyncio.sleep(0.05)
            elif text_type == 'photo':
                await bot.send_photo(user_id, msg.photo[-1].file_id, caption=text_caption, reply_markup=rep_btn)
                await asyncio.sleep(0.05)
            elif text_type == 'audio':
                await bot.send_audio(user_id, msg.audio, reply_markup=rep_btn)
                await asyncio.sleep(0.05)
            elif text_type == 'location':
                lat = msg.location['latitude']
                lon = msg.location['longitude']
                await bot.send_location(chat_id=user_id, latitude=lat, longitude=lon, reply_markup=rep_btn)
                await asyncio.sleep(0.05)
            send_user += 1
        except BotBlocked:
            send_error += 1
            continue
    if send_user == 0:
        await bot.send_message(msg.from_user.id, 'Xech kimga yuborilmadi')
    else:
        await bot.send_message(msg.from_user.id,
                               f"Send: <b>{send_user + send_error}</b> for user\n"
                               f"Active Users: <b>{send_user}</b>\n"
                               f"Banned Users: <b>{send_error}</b>\n")
    await state.finish()


def register_send_ads_handler(dp: Dispatcher):
    dp.register_callback_query_handler(send_ads, text="admin:send_ads")
    dp.register_message_handler(send_msg, state=AdminAds.text,
                                content_types=["text", "video", "audio", "photo", "location"])
