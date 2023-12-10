from handlers.users.start import register_start_handler


async def launch_handlers(dispatcher):
    register_start_handler(dispatcher)
