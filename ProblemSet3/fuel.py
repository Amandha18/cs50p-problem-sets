fuel = input("Fraction: ")
try:
    fuel = fuel.split("/")
    fuel[0], fuel[1] = int(fuel[0]), int(fuel[1])
    percentage = (fuel[0]/fuel[1])*100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(round(percentage),"%",sep="")
except ZeroDivisionError:
    print("cannot divide by zero")
except (ValueError, IndexError):
    print("Please Enter a fraction\n\tex: #/#")