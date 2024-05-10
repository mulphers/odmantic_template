from typing import Optional, Sequence, Type

from src.common.dto.user import UserCreate, UserUpdate
from src.database.models.user import User
from src.database.repositories.odmantic_repository import OdmanticRepository


class UserRepository(OdmanticRepository[User]):
    model: Type[User] = User

    async def create_user(self, user: UserCreate) -> Optional[User]:
        return await self.create(data=user.model_dump(exclude_none=True))

    async def select_user(self, user_id: int) -> Optional[User]:
        return await self.select(self.model.user_id == user_id)

    async def select_admins(
            self,
            offset: Optional[int] = None,
            limit: Optional[int] = None
    ) -> Sequence[User]:
        return await self.select_many(
            self.model.is_admin is True,
            offset=offset,
            limit=limit
        )

    async def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        return await self.update(self.model.user_id == user_id, data=user.model_dump(exclude_none=True))

    async def delete_user(self, user_id: int) -> Sequence[User]:
        return await self.delete(self.model.user_id == user_id)
