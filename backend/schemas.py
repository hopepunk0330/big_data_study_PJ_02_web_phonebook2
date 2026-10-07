from pydantic import BaseModel, Field


class SignupIn(BaseModel):
    username: str = Field(min_length=4, max_length=20, pattern=r"^[a-z0-9]+$")
    password: str = Field(min_length=4, max_length=20)


class LoginIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    # password_hash는 절대 포함하지 않는다 (03 문서 FN-003)


class FindPasswordIn(BaseModel):
    username: str = Field(min_length=4, max_length=20, pattern=r"^[a-z0-9]+$")


class FindPasswordOut(BaseModel):
    username: str


class ResetPasswordIn(BaseModel):
    username: str = Field(min_length=4, max_length=20, pattern=r"^[a-z0-9]+$")
    new_password: str = Field(min_length=4, max_length=20)


class MessageOut(BaseModel):
    message: str


class ContactCreate(BaseModel):
    name: str = Field(min_length=1, max_length=5)
    phone: str = Field(pattern=r"^010\d{8}$")
    addr: str = ""
    category_id: int


class ContactUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=5)
    phone: str | None = Field(default=None, pattern=r"^010\d{8}$")
    addr: str | None = None
    category_id: int | None = None


class ContactOut(BaseModel):
    id: int
    name: str
    phone: str
    addr: str
    category_id: int
    category_name: str


class ContactListOut(BaseModel):
    total: int
    items: list[ContactOut]


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=10)


class CategoryUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=10)


class CategoryOut(BaseModel):
    id: int
    name: str
