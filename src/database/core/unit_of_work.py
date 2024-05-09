from odmantic.session import AIOSession, AIOTransaction

from src.common.interfaces.unit_of_work import AbstractUnitOfWork


class OdmanticUnitOfWork(AbstractUnitOfWork[AIOSession, AIOTransaction]):
    async def commit(self) -> None:
        if self.transaction:
            await self.transaction.commit()

    async def rollback(self) -> None:
        if self.transaction:
            await self.transaction.abort()

    async def create_transaction(self) -> None:
        await self.session.start()
        self.transaction = self.session.transaction()
        await self.transaction.start()

    async def close_transaction(self) -> None:
        if self.transaction:
            await self.transaction.__aexit__(None, None, None)
            self.transaction = None
            await self.session.end()


def unit_of_work_factory(session: AIOSession) -> OdmanticUnitOfWork:
    return OdmanticUnitOfWork(session=session)
