from __future__ import annotations

from types import TracebackType
from typing import Optional, Type

from src.common.interfaces.unit_of_work import AbstractUnitOfWork
from src.database.repositories.user_repository import UserRepository


class DatabaseGateway:
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow

    async def __aenter__(self) -> DatabaseGateway:
        await self.uow.__aenter__()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        await self.uow.__aexit__(exc_type, exc_val, exc_tb)

    def user_repository(self) -> UserRepository:
        return UserRepository(session=self.uow.session)


def database_gateway_factory(uow: AbstractUnitOfWork) -> DatabaseGateway:
    return DatabaseGateway(uow=uow)
