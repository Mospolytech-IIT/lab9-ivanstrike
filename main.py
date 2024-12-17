from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db_setup import SessionLocal
from crud import*

app = FastAPI()

# Зависимость для работы с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return RedirectResponse("/users")

# Пользователи
@app.get("/users")
async def manage_users(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)
    return templates.TemplateResponse("manage_users.html", {"request": request, "users": users})

@app.post("/users")
async def add_user(
    username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)
):
    create_user(db, username, email, password)
    return RedirectResponse("/users", status_code=302)

@app.post("/users/{user_id}/edit")
async def edit_user(
    user_id: int, username: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)
):
    update_user_email(db, user_id, username, email)
    return RedirectResponse("/users", status_code=302)

@app.post("/users/{user_id}/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    delete_user_with_posts(db, user_id)
    return RedirectResponse("/users", status_code=302)

# Посты
@app.get("/posts")
async def manage_posts(request: Request, db: Session = Depends(get_db)):
    posts = get_posts(db)
    users = get_users(db)  # Для выбора автора поста
    return templates.TemplateResponse("manage_posts.html", {"request": request, "posts": posts, "users": users})

@app.post("/posts")
async def add_post(
    title: str = Form(...), content: str = Form(...), user_id: int = Form(...), db: Session = Depends(get_db)
):
    create_post(db, title, content, user_id)
    return RedirectResponse("/posts", status_code=302)

@app.post("/posts/{post_id}/edit")
async def edit_post(
    post_id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)
):
    update_post_content(db, post_id, title, content)
    return RedirectResponse("/posts", status_code=302)

@app.post("/posts/{post_id}/delete")
async def delete_post( post_id: int, db: Session = Depends(get_db) ):
    delete_post_by_id(db, post_id)
    return RedirectResponse("/posts", status_code=302)

