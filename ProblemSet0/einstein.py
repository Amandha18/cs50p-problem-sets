from ast import Constant


mass = int(input("Enter the mass(kg): "))
speed_of_light = 300000000
energy = mass*speed_of_light**2
energy = f"{energy:,}" # 1000 seperator
print("E = {} J".format(energy))