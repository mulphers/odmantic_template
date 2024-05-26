from typing import AsyncGenerator

from odmantic.engine import AIOEngine

from src.database.core.gateway import DatabaseGateway, database_gateway_factory
from src.database.core.unit_of_work import (OdmanticUnitOfWork,
                                            unit_of_work_factory)

__all__ = (
    'DatabaseGateway',
    'TransactionGateway',
    'OdmanticUnitOfWork',
    'database_gateway_factory',
    'unit_of_work_factory',
)


class TransactionGateway:
    def __init__(self, engine: AIOEngine) -> None:
        self.engine = engine

    async def __call__(self) -> AsyncGenerator[DatabaseGateway, None]:
        async with database_gateway_factory(unit_of_work_factory(self.engine.session())) as gateway:
            yield gateway
