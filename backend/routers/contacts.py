from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import get_db
from routers.auth import get_current_user

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("", response_model=schemas.ContactOut, status_code=201)
def add_contact(
    data: schemas.ContactCreate,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not crud.get_my_category(db, user.id, data.category_id):
        raise HTTPException(404, "해당 카테고리가 없습니다")
    if crud.find_contact_by_phone(db, user.id, data.phone):
        raise HTTPException(409, "이미 등록된 전화번호입니다")
    return crud.create_contact(db, user.id, data)


@router.get("", response_model=schemas.ContactListOut)
def list_contacts(
    name: str | None = None,
    category_id: int | None = None,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    items = crud.list_contacts(db, user.id, name=name, category_id=category_id)
    return {"total": len(items), "items": items}


@router.patch("/{contact_id}", response_model=schemas.ContactOut)
def update_contact(
    contact_id: int,
    data: schemas.ContactUpdate,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    contact = crud.get_my_contact(db, user.id, contact_id)
    if not contact:
        raise HTTPException(404, "해당 연락처가 없습니다")

    changes = data.model_dump(exclude_unset=True)
    if "category_id" in changes and not crud.get_my_category(db, user.id, changes["category_id"]):
        raise HTTPException(404, "해당 카테고리가 없습니다")
    if "phone" in changes:
        duplicate = crud.find_contact_by_phone(db, user.id, changes["phone"])
        if duplicate and duplicate.id != contact.id:
            raise HTTPException(409, "이미 등록된 전화번호입니다")

    return crud.update_contact(db, contact, changes)


@router.delete("/{contact_id}", status_code=204)
def delete_contact(
    contact_id: int,
    user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    contact = crud.get_my_contact(db, user.id, contact_id)
    if not contact:
        raise HTTPException(404, "해당 연락처가 없습니다")
    crud.delete_contact(db, contact)
