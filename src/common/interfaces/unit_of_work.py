from __future__ import annotations

from abc import ABC, abstractmethod
from types import TracebackType
from typing import Generic, Optional, Type

from src.common.types import SessionType, TransactionType


class AbstractUnitOfWork(ABC, Generic[SessionType, TransactionType]):
    def __init__(self, session: SessionType) -> None:
        self.session = session
        self.transaction: Optional[TransactionType] = None

    async def __aenter__(self) -> AbstractUnitOfWork:
        await self.create_transaction()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

        await self.close_transaction()

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    @abstractmethod
    async def create_transaction(self) -> None:
        pass

    @abstractmethod
    async def close_transaction(self) -> None:
        pass
