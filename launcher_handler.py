from handlers.users.start import register_start_handler
from handlers.admins.intro import register_admin_handlers


async def launch_handlers(dispatcher):
    register_admin_handlers(dispatcher)
    register_start_handler(dispatcher)
