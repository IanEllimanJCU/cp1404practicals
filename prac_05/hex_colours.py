COLOUR_CODE = {"maroon": "#b03060", "orchid": "#da70d6", "pink": "#ffc0cb", "salmon": "#fa8072",
                "thistle": "#d8bfd8", "violet": "#ee82ee", "wheat": "#f5deb3", "linen": "#faf0e6",
                "lavender": "#e6e6fa", "brown": "#a52a2a"}
def main():
    print(f"Colours available to print are ", end='')
    for i in COLOUR_CODE:
        if i != "brown":
            print(f"{i}, ", end='')
    print("and brown")
    colour_choice = input("Please enter your colour choice: ").lower()
    while colour_choice != "":
        print_colour_code(colour_choice)
        colour_choice = input("Please enter your colour choice: ").lower()
    exit()

def print_colour_code(colour_choice):
    for i in COLOUR_CODE:
        if colour_choice in i:
            print(COLOUR_CODE[colour_choice])
main()