from handlers.users.start import register_start_handler
from handlers.admins.intro import register_admin_handlers
from handlers.admins.send_ads import register_send_ads_handler
from handlers.users.post import register_post_handler


async def launch_handlers(dispatcher):
    register_admin_handlers(dispatcher)
    register_start_handler(dispatcher)
    register_send_ads_handler(dispatcher)
    register_post_handler(dispatcher)
