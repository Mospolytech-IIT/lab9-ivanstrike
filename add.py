from db_setup import SessionLocal, User, Post

def add_users():
    session = SessionLocal()
    try:
        users = [
            User(username="user1", email="user1@example.com", password="password1"),
            User(username="user2", email="user2@example.com", password="password2"),
            User(username="user3", email="user3@example.com", password="password3"),
        ]
        session.add_all(users)
        session.commit()
        print("Пользователи успешно добавлены!")
    finally:
        session.close()

        
def add_posts():
    session = SessionLocal()
    try:
        posts = [
            Post(title="Post 1", content="Content of Post 1", user_id=1),
            Post(title="Post 2", content="Content of Post 2", user_id=1),
            Post(title="Post 3", content="Content of Post 3", user_id=2),
        ]
        session.add_all(posts)
        session.commit()
        print("Посты успешно добавлены!")
    finally:
        session.close()

if __name__ == "__main__":
    add_users()
    add_posts()
