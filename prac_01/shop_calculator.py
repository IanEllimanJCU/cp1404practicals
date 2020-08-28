total_price=0
discount=0
num_of_items=int(input('Number of items: '))
while num_of_items < 0:
    print('Invalid number of items, please enter 0 or above')
    num_of_items = int(input('Number of items: '))
for i in range(0, num_of_items, 1):
    item_price=float(input('Price of item: '))
    total_price+=item_price
if total_price > 100:
    discount=0.1*total_price
print(f'Total price for 3 items is ${total_price-discount:.2f}')
exit()