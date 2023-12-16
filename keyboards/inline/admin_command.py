from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def admin_command():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="👥 Users", callback_data="admin:get_users")
    btn2 = InlineKeyboardButton(text="📨 Send Ads", callback_data="admin:send_ads")
    keyboard.add(btn1, btn2)
    return keyboard


async def cancel_btn():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton(text="🔙 Back", callback_data="cancel_state")
    keyboard.add(btn)
    return keyboard
