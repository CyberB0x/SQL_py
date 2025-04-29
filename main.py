from app.user import add_user, view_users

def main():
    # Добавляем пользователя
    add_user("Иван Иванов", "ivan@mail.com")

    # Просматриваем всех пользователей
    view_users()

if __name__ == "__main__":
    main()
