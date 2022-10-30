
def perform_calc(x,y,z):
    if y == "+":
        calc = x + z
        return calc
    elif y == "-":
        calc = x - z
        return calc
    elif y == "*":
        calc = x * z
        return calc
    elif y == "/":
        if z == 0:
            calc = "Divide by Zero error"
        else:
            calc = x / z
        return calc
    else:
        calc = "Sign not idetified\n\tplease follow the format:\n\tx y z"
        return calc
    




equation = str(input("Expression: "))
x, y, z = equation.split()
x = int(x)
z = int(z)

calc = perform_calc(x,y,z) # calls the function and get calc
print(calc)