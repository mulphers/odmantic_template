from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


def create_engine(host: str, port: int) -> AIOEngine:
    return AIOEngine(
        client=AsyncIOMotorClient(
            host=host,
            port=port,
            directConnection=True
        )
    )
