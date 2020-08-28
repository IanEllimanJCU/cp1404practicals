def main():
        min_length = 6
        password = input("Please input a password that's at least 6 characters long: ")
        while len(password) < 6:
            password = input("Password too short. Please input a password that's at least 6 characters long: ")
        print("*" * len(password))
main()