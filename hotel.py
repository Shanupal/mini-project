menu = {
    'pizza':40,
    'pasta' :10,
    'burger' : 30,
    'salad' :15,
    'coffee':100,
    'momo' :20,
}

print("welcome to sagar restaurant")
print("pizza: $40\n pasta:$10\n burger:$30\n salad:$15\n coffee:$100\n momo:$20")


order_total = 0

item_1 =input("enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your aoder")
else:
    print(f"ordered item {item_1} is not avaialable you")

another_order = input("Do you want to add another item? (yes/no)")

if another_order == "yes":
    item_2 = input("name of item you want to order:")
    order_total += menu[item_2]
    print(f"item {item_2} has been added to order")
else:
    print("ordered item {iten_2} is not avaialable")
# if another_order in menu:
#     order_total += menu[item_1]
#     print(f"item {item_1} has been added to order")
# else:
#     print("ordered item {iten_2} is not avaialable")
    
print(f"the total amount of itema to pay is {order_total}")
