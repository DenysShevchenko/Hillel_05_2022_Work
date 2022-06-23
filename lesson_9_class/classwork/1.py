from services import UsersService, get_user_data


def main():
    user_data = get_user_data()
    print(user_data)

    user_data = UsersService.get_user_data()
    print(user_data)


if __name__ == "__main__":
    main()
