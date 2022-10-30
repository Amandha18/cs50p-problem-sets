def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6: # check the length
        return False
    elif not s.isalnum(): # whether it conatins special characters
        return False
    elif not s[0].isalpha() and not s[1].isalpha(): # whether first two are alphabetic
        return False
    elif first_zero(s): # check if first number is 0
        return False    
    elif middle_numbers(s): # check if there are middle numbers
        return False
    return True

def first_zero(s):
    for char in s:
         if char.isdigit():
            if char == "0":
                return True
            return False

def middle_numbers(s):
    isNum = False
    letter_after = False
    for char in s:
        if char.isdigit():
            isNum = True
            digit_place = s.index(char) # find where the digit starts
            for j in s[digit_place:]: # check for letters that come after the digit
                if j.isalpha():
                    letter_after = True
            break

    if letter_after and isNum:
        return True
    return False

main()