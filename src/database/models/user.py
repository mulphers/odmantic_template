from odmantic import Field, Model


class User(Model):
    user_id: int = Field(
        primary_field=True,
        index=True,
        unique=True
    )
    username: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
