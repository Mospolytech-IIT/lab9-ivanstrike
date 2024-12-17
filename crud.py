from sqlalchemy.orm import Session
from db_setup import User, Post

def get_users(db: Session):
    return db.query(User).all()

def get_posts(db: Session):
    return db.query(Post).all()

def create_user(db: Session, username: str, email: str, password: str):
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()

def create_post(db: Session, title: str, content: str, user_id: int):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()

def update_user_email(db: Session, user_id: int, username: str, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        db.commit()

def update_post_content(db: Session, post_id: int, title: str, content: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.content = content
        db.commit()

def delete_user_with_posts(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

def delete_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
