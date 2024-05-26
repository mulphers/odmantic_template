from typing import Annotated, Optional

from fast_depends import Depends, inject

from src.common.dto import UserCreate, UserDTO, UserUpdate
from src.common.markers import TransactionGatewayMarker
from src.database import DatabaseGateway

"""

To use the database, use the following functions:

- from typing import Annotated
- from fast_depends import Depends, inject
- from src.common.markers import TransactionGatewayMarker
- from src.database import DatabaseGateway

Use it this way:

```
@inject
async def you_handler_or_another(
    gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    # Your handler
    pass
```

"""


@inject
async def create_user(
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)],
        user_data: UserCreate
) -> Optional[UserDTO]:
    user_repository = gateway.user_repository()
    created_user = await user_repository.create_user(user_data)

    if created_user:
        return UserDTO(**created_user.model_dump())

    return None


@inject
async def find_user_by_id(
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)],
        user_id: int
) -> Optional[UserDTO]:
    user_repository = gateway.user_repository()
    found_user = await user_repository.select_user(user_id)

    if found_user:
        return UserDTO(**found_user.model_dump())

    return None


@inject
async def update_user(
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)],
        user_id: int,
        user_data: UserUpdate
) -> Optional[UserDTO]:
    user_repository = gateway.user_repository()
    updated_user = await user_repository.update_user(user_id, user_data)

    if updated_user:
        return UserDTO(**updated_user.model_dump())

    return None
