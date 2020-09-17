from prac_06.guitar_class import Guitar
def main():
    print("My guitars!")
    guitar_name = "a"
    guitars = []
#    guitar_name = input("Name: ")
#    if guitar_name != "":
#        while guitar_name != "":
#            guitar_year = input("Year: ")
#            guitar_cost = input("$")
#            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
#            guitar_name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    i=0
    for elem in guitars:
        i = i + 1
        print(f"Guitar {i}: {elem}")

main()