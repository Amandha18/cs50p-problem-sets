grocery_list = []
grocery_dict = {}

while True:
    try:
        # get input and uppercase it
        item = input()
        item = item.upper()

        # put it into grocery list and sort
        grocery_list.append(item)
        grocery_list.sort()

    except EOFError:
        # arrange it into a dictionary
        for item in grocery_list:
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1
        # output the grocery list
        for i in grocery_dict:
            print(f"{grocery_dict[i]} {i}")
        break

    else:
        continue

        

