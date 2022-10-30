def main():
    sentence = str(input("Enter your sentence\n"))
    convert(sentence) # do not put the line 8 after this beacuse this is main an dwon't return th econverted value
    
def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    print(sentence)

main()

