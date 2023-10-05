def filter_string(word):
    filtering_letters = [',', '.', ':', '!', '?']
    for filter_letter in filtering_letters: 
        if filter_letter in word: 
            word = word.replace(filter_letter, "")

    return word.upper()

while True:
    word_input = input("Please enter string : ")

    if word_input.lower() == "done" : break

    print(f"{filter_string(word_input)}")

print("Bye !")