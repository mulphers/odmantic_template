from typing import Any, Optional, Sequence, Type

from odmantic.engine import ModelType
from odmantic.session import AIOSession

from src.common.interfaces.repository import AbstractRepository


class OdmanticRepository(AbstractRepository[ModelType, AIOSession, bool]):
    model: Type[ModelType]

    async def create(self, data: dict[str, Any]) -> Optional[ModelType]:
        return await self.session.save(self.model(**data))

    async def select(self, *clauses: bool) -> Optional[ModelType]:
        return await self.session.find_one(self.model, *clauses)

    async def select_many(
            self,
            *clauses: bool,
            offset: Optional[int] = None,
            limit: Optional[int] = None
    ) -> Sequence[ModelType]:
        return await self.session.find(
            self.model,
            *clauses,
            skip=offset if offset else 0,
            limit=limit
        )

    async def update(self, *clauses: bool, data: dict[str, Any]) -> Optional[ModelType]:
        instance = await self.select(*clauses)

        if instance:
            for key, value in data.items():
                setattr(instance, key, value)

            return await self.session.save(instance)

        return None

    async def delete(self, *clauses: bool) -> Sequence[ModelType]:
        removed_users = await self.select_many(*clauses)

        await (removed_users_count := self.session.remove(self.model, *clauses))
        assert removed_users_count == len(removed_users)

        return removed_users
