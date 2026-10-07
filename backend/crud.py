import secrets

from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas
from security import hash_password, verify_password

DEFAULT_CATEGORY_NAMES = ["가족", "친구", "기타"]


# ── 사용자 ────────────────────────────────────────────────────────────────


def get_user_by_username(db: Session, username: str) -> models.User | None:
    return db.scalar(select(models.User).where(models.User.username == username))


def create_user(db: Session, username: str, password: str) -> models.User:
    user = models.User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.flush()
    for name in DEFAULT_CATEGORY_NAMES:
        db.add(models.Category(user_id=user.id, name=name))
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str) -> models.User | None:
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


def reset_password(db: Session, user: models.User, new_password: str) -> None:
    user.password_hash = hash_password(new_password)
    db.query(models.LoginSession).filter(models.LoginSession.user_id == user.id).delete()
    db.commit()


# ── 세션 ─────────────────────────────────────────────────────────────────


def create_login_session(db: Session, user_id: int) -> str:
    session_id = secrets.token_hex(32)
    db.add(models.LoginSession(session_id=session_id, user_id=user_id))
    db.commit()
    return session_id


def get_user_by_session(db: Session, session_id: str) -> models.User | None:
    session = db.get(models.LoginSession, session_id)
    if not session:
        return None
    return db.get(models.User, session.user_id)


def delete_login_session(db: Session, session_id: str) -> None:
    session = db.get(models.LoginSession, session_id)
    if session:
        db.delete(session)
        db.commit()


# ── 카테고리 ──────────────────────────────────────────────────────────────


def list_categories(db: Session, user_id: int) -> list[models.Category]:
    return list(
        db.scalars(select(models.Category).where(models.Category.user_id == user_id))
    )


def get_my_category(db: Session, user_id: int, category_id: int) -> models.Category | None:
    return db.scalar(
        select(models.Category).where(
            models.Category.id == category_id, models.Category.user_id == user_id
        )
    )


def find_category_by_name(db: Session, user_id: int, name: str) -> models.Category | None:
    return db.scalar(
        select(models.Category).where(
            models.Category.user_id == user_id, models.Category.name == name
        )
    )


def create_category(db: Session, user_id: int, name: str) -> models.Category:
    category = models.Category(user_id=user_id, name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(db: Session, category: models.Category, name: str) -> models.Category:
    category.name = name
    db.commit()
    db.refresh(category)
    return category


def count_contacts_in_category(db: Session, user_id: int, category_id: int) -> int:
    return (
        db.query(models.Contact)
        .filter(models.Contact.user_id == user_id, models.Contact.category_id == category_id)
        .count()
    )


def delete_category(db: Session, category: models.Category) -> None:
    db.delete(category)
    db.commit()


# ── 연락처 ────────────────────────────────────────────────────────────────


def _to_contact_out(contact: models.Contact, category_name: str) -> dict:
    return {
        "id": contact.id,
        "name": contact.name,
        "phone": contact.phone,
        "addr": contact.addr,
        "category_id": contact.category_id,
        "category_name": category_name,
    }


def _serialize_contact(db: Session, contact: models.Contact) -> dict:
    category = db.get(models.Category, contact.category_id)
    category_name = category.name if category else ""
    return _to_contact_out(contact, category_name)


def list_contacts(
    db: Session, user_id: int, name: str | None = None, category_id: int | None = None
) -> list[dict]:
    query = (
        select(models.Contact, models.Category.name)
        .join(models.Category, models.Contact.category_id == models.Category.id)
        .where(models.Contact.user_id == user_id)
    )
    if name:
        query = query.where(models.Contact.name == name)
    if category_id is not None:
        query = query.where(models.Contact.category_id == category_id)
    rows = db.execute(query).all()
    return [_to_contact_out(contact, category_name) for contact, category_name in rows]


def get_my_contact(db: Session, user_id: int, contact_id: int) -> models.Contact | None:
    return db.scalar(
        select(models.Contact).where(
            models.Contact.id == contact_id, models.Contact.user_id == user_id
        )
    )


def find_contact_by_phone(db: Session, user_id: int, phone: str) -> models.Contact | None:
    return db.scalar(
        select(models.Contact).where(
            models.Contact.user_id == user_id, models.Contact.phone == phone
        )
    )


def create_contact(db: Session, user_id: int, data: schemas.ContactCreate) -> dict:
    contact = models.Contact(
        user_id=user_id,
        category_id=data.category_id,
        name=data.name,
        phone=data.phone,
        addr=data.addr,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _serialize_contact(db, contact)


def update_contact(db: Session, contact: models.Contact, data: dict) -> dict:
    for field, value in data.items():
        setattr(contact, field, value)
    db.commit()
    db.refresh(contact)
    return _serialize_contact(db, contact)


def delete_contact(db: Session, contact: models.Contact) -> None:
    db.delete(contact)
    db.commit()
