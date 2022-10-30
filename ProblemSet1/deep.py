def great_answer(answer):
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        answer = "Yes"
        return answer
    else:
        answer = "No"
        return answer

user_answer = great_answer(input("What is the answer to the Great Question of Life, the Universe and Everything?\n"))
print(user_answer)