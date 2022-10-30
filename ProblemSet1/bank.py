def bank_greeting(greeting): # return money
    if greeting == "hello"  or greeting == "hello!" or greeting.startswith("hello"):
        money = "0"
        return money
    elif greeting.startswith("h"):
        money = "20"
        return money
    else:
        money ="100"
        return money

user_greeting = bank_greeting(input("Enter the greetng\n")) # get money from function
print(user_greeting)
