def main():
    user_emails_dict = {}
    user_email = "a"
    user_name = "a"
    user_name_list = []
    user_email = input("Email: ")
    while user_email != "":
        user_name = user_email.split("@")
        print(user_name)
        user_name = user_name[0].split(".")
        print(f"Is your name ", end='')
        length_user_name = len(user_name)
        for i in :
            print(f"{user_name[i].title()}")
        print("? (Y/n) ", end='')
        name_correct = input().upper()
        if name_correct == "Y":
            user_name = user_name[0] + " " + user_name[1]
        else:
            user_name = input("Name: ")
        user_emails_dict.update({user_email: user_name})
        print(user_emails_dict)
        user_email = input("Email: ")
    for i in user_emails_dict:
        print(f"{user_emails_dict[i].title()} ({i})")

main()


"""        if "." in user_name_list[0]:
            user_name_list = user_name_list[0].split(".")
            print(f"Is your name ", end='')
            for i in user_name_list:
                print(f"{i.title()}", end='')
                if i != user_name_list:
                    print(" ", end='')
            print("? (Y/n) ", end='')
            name_correct = input().upper()
            if name_correct == "Y":
                user_name = user_name_list[0] + " " + user_name_list[1]
            else:
                user_name = input("Name: ")
            user_emails_dict.update({user_email:user_name})
            print(user_emails_dict)
            user_email = input("Email: ")
        else:
            print(f"Is your name {user_name_list[0].title()}", end='')
            print("? (Y/n) ", end='')
            name_correct = input().upper()
            if name_correct == "Y":
                user_name = user_name_list[0]
            else:
                user_name = input("Name: ")
            user_emails_dict.update({user_email:user_name})
            print(user_emails_dict)
            user_email = input("Email: ")"""