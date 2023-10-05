#Assigment 4 strings

def filter_string(word):
#Funtion to filter the string with specific characters state above
    filtering_letters = [',', '.', ':', '!', '?']
    #for loop to iterte over the characters to filter
    for filter_letter in filtering_letters: 
        if filter_letter in word: 
            word = word.replace(filter_letter, "")

    return word.upper()

#While loop for the user
while True:
    word_input = input("Please enter string : ")

    if word_input.lower() == "done" : break

    print(f"{filter_string(word_input)}")

print("Bye !")