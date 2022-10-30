import inflect

p = inflect.engine()
name = "none"
name_list = []
while name = "Aa":
    try:
        name = input("Name: ")
        name = name.title()
        name_list.append(name)

    except EOFError: 
        print("Adieu, adieu, to",p.join(name_list))
        exit()