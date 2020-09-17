def main():
    user_emails_dict = {}
    user_email = "a"
    user_name = "a"
    user_name_list = []
    user_email = input("Email: ")
    while user_email != "":
        user_name_list = user_email.split("@")
        user_name_list = user_name_list[0].split(".")
        name = " ".join(user_name_list).title()
        print(f"Is your name {name}? (Y/n): ", end='')
        name_correct = input().upper()
        if name_correct == "Y":
            user_name = name
        else:
            user_name = input("Name: ")
        user_emails_dict.update({user_email:user_name})
        user_email = input("Email: ")
    for i in user_emails_dict:
        print(f"{user_emails_dict[i].title()} ({i})")
main()