def main():
    min_length = 6
    password = get_password()
    while len(password) < 6:
        password = input("Password too short. Please input a password that's at least 6 characters long: ")
    passwords_to_asteriks(password)


def get_password():
    password = input("Please input a password at least 6 characters long: ")
    return password


def passwords_to_asteriks(password):
    return print("*" * len(password))


main()
