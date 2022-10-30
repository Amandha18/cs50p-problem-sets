menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
sum = 0
while True:
    try: # test the code for error
        item = input("Item: ")
        item = item.title()
        for i in menu:
            if item == i:
                sum += menu[item]
                print(f"Total: ${sum}")
            else:
                continue
    except EOFError: # handles when there is this error
        print()
        break
    else: # when there is no error
        continue

