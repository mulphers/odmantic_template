import asyncio

from fast_depends import dependency_provider

from src.common.markers import TransactionGatewayMarker
from src.core.settings import load_settings
from src.database import TransactionGateway
from src.database.core.connection import create_engine


async def main() -> None:
    settings = load_settings()

    database_engine = create_engine(
        host=settings.db.host,
        port=settings.db.port
    )

    dependency_provider.override(TransactionGatewayMarker, TransactionGateway(database_engine))


if __name__ == '__main__':
    asyncio.run(main())
