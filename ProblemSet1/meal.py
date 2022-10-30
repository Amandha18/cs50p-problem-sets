def main():
    user_input = convert(input("What time is it? ")) # gets the time
    # user input is not the float time
    if user_input >= 7 and user_input <= 8:
        meal = "breakfast time"
    elif user_input >= 12 and user_input <= 13:
        meal = "lunch time"
    elif user_input >= 18 and user_input <= 19:
        meal = "dinner time"
    print(meal)

def convert(time):
    h, m = time.split(":")
    h, m = float(h), float(m)
    time = float(h + m/100)
    return time


if __name__ == "__main__":
    main()