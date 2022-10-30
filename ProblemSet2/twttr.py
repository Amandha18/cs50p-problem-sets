def main():
    word = input("Enter the word: ")
    shorten(word)

def shorten(word):
    vowel = "aeiouAEIOU"
    vowel_list  = list(vowel)
    #cleaned = ["" if char in vowel_list else char for char in word] # char is like i. it is a variable here

    cleaned = [""]
    for char in word:
        if char in vowel:
            cleaned = cleaned + [""] 
        else:
            cleaned = cleaned + [char]

    result = "".join(cleaned)
    print(result)

if __name__ == "__main__":
    main()