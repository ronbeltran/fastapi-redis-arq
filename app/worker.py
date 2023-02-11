from arq.connections import RedisSettings
from app.main import create_task

async def startup(ctx):
    pass

async def shutdown(ctx):
    pass

FUNCTIONS: list = [
    create_task,
]

class WorkerSettings:
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = RedisSettings()
    functions: list = FUNCTIONS
