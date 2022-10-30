def main():
    dollars = dollars_to_float(input("How much was the meal? ")) # d 
    # the whole thing returns d to dollars
    percent = percent_to_float(input("What percentage would you like to tip? ")) # p
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") # rounding the tip for 2 decimals/floating points


def dollars_to_float(d):
    d = float(str(d)[1:])
    return d



def percent_to_float(p):
    p = float(str(p)[:-1])
    p = (p/100)
    return p


main()