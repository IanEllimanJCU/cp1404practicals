import random
MIN = 1
MAX = 45
def main():
    quick_pick_amount = int(input("How many quick picks? "))
    for i in range(quick_pick_amount):
        quick_picks = [random.randint(MIN,MAX) for i in range(6)]
        quick_picks.sort()
        for elem in quick_picks:
            print(f"{elem:>2} ", end='')
        print("")

main()