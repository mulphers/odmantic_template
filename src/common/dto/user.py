from typing import Optional

from pydantic import BaseModel


# Must contain fields from src\database\models\user.py
class UserDTO(BaseModel):
    user_id: int
    username: str
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


# Must contain fields from src\database\models\user.py
class UserCreate(UserDTO):
    pass


# Must contain modifiable fields from src\database\models\user.py
class UserUpdate(BaseModel):
    username: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
