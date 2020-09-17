from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages_list=[ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for elem in programming_languages_list:
        if elem.is_dynamic() == True:
            print(elem.name)
        else:
            pass

main()
