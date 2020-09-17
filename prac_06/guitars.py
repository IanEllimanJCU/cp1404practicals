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
    for i, guitar in enumerate(guitars, 0):
        if guitar.is_vintage == True:
            vintage_status = "(vintage)"
        else:
            vintage_status = ""
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}) : worth ${guitar.cost:10,.2f} {vintage_status}")

main()