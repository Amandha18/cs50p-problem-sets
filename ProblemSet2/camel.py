camel_case = input("camelCase: ")
new_word = camel_case[0].lower()

for letter in camel_case[1:]:
    if letter.isupper() == True:   # remember brackets!!!!!!!!!!!!!
        new_word = new_word + "_"
    new_word = new_word + (letter.lower())
print("snake_case: ",new_word)
