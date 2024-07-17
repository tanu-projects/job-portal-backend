import motor.motor_asyncio
from beanie import init_beanie

from ..conf import DATABASE_URL
from ..model import LoggingModel
from ..model.user import Token, UserDocument, EmailConfigDocument

client = None


async def init_db():
    print("Initializing database")
    global client
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(
        database=client.jobportal,
        document_models=[
            UserDocument,
            Token,
            LoggingModel,
            EmailConfigDocument
        ],
    )


async def stop_db():
    print("Stopping database...")
    global client
    if client:
        client.close()
