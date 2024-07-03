from .echo import echo_router
from .start import start_router
from .help import help_router


def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(echo_router)
