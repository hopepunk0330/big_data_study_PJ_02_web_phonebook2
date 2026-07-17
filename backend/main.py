from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from routers import auth, categories, contacts

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")

app.include_router(auth.router)
app.include_router(contacts.router)
app.include_router(categories.router)


@app.get("/")
def read_index():
    return FileResponse("../static/index.html")


def _validation_message(request: Request, errors: list) -> str:
    # 01문서 §4-1 필드별 형식 규칙에 맞춰 Pydantic 원시 영문 메시지를 한글로 치환한다.
    # 여러 필드가 동시에 위반돼도 첫 번째 오류만 노출한다(기존 프론트 extractDetail 동작 유지).
    first_error = errors[0]
    loc = first_error.get("loc", ())
    field = loc[-1] if loc else None
    path = request.url.path

    if field == "username":
        return "아이디는 영문 소문자·숫자 4~20자여야 합니다"
    if field in ("password", "new_password"):
        return "비밀번호는 4~20자여야 합니다"
    if field == "phone":
        return "전화번호 형식이 올바르지 않습니다(010으로 시작하는 11자리 숫자)"
    if field == "name":
        if path.startswith("/categories"):
            return "카테고리 이름은 1~10자여야 합니다"
        return "이름은 1~5자여야 합니다"
    return first_error.get("msg", "입력값이 올바르지 않습니다")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    message = _validation_message(request, exc.errors())
    return JSONResponse(status_code=422, content={"detail": message})
