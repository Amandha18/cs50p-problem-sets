nutrition = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 110,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
    "Grapes" : 90,
    "Honeydew Melon" : 50,
    "Kiwifruit" : 90,
    "Lemon" : 15
}

fruit = input("Item: ")
fruit = fruit.title()
print("Calories:",nutrition[fruit])