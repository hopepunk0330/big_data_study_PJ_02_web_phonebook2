from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


def get_current_user(
    session_id: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
) -> models.User:
    if session_id:
        user = crud.get_user_by_session(db, session_id)
        if user:
            return user
    raise HTTPException(401, "로그인이 필요합니다")


@router.post("/signup", response_model=schemas.UserOut, status_code=201)
def signup(data: schemas.SignupIn, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, data.username):
        raise HTTPException(409, "이미 사용 중인 아이디입니다")
    return crud.create_user(db, data.username, data.password)


@router.post("/login", response_model=schemas.MessageOut)
def login(data: schemas.LoginIn, response: Response, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(401, "아이디 또는 비밀번호가 올바르지 않습니다")
    session_id = crud.create_login_session(db, user.id)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        samesite="lax",
    )
    return {"message": "로그인 성공"}


@router.post("/logout", response_model=schemas.MessageOut)
def logout(
    response: Response,
    session_id: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
):
    if session_id:
        crud.delete_login_session(db, session_id)
    response.delete_cookie("session_id")
    return {"message": "로그아웃 되었습니다"}


@router.get("/me", response_model=schemas.UserOut)
def me(user: models.User = Depends(get_current_user)):
    return user


@router.post("/find-password", response_model=schemas.FindPasswordOut)
def find_password(data: schemas.FindPasswordIn, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, data.username)
    if not user:
        raise HTTPException(404, "존재하지 않는 아이디입니다")
    return {"username": user.username}


@router.patch("/password", response_model=schemas.MessageOut)
def reset_password(data: schemas.ResetPasswordIn, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, data.username)
    if not user:
        raise HTTPException(404, "존재하지 않는 아이디입니다")
    crud.reset_password(db, user, data.new_password)
    return {"message": "비밀번호가 변경되었습니다"}
