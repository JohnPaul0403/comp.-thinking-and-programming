#Assigment 1 Strings

while True: 
    word_input = input("Enter two words: ")
    if word_input.lower() == "done" or word_input == "" : break

    #Splits and correct the word input
    word_input = word_input.strip().split(" ")

    try : 
        #Check is the word have any integers, in case of it reset the list
        list(map(lambda x : int(x), word_input))
        word_input = []
    except : pass

    #If the len of the input if less or iqual to 1, it will pass and not print
    if len(word_input) <= 1 : continue

    print("{} comes first".format(sorted(word_input)[0]))

print("-- bye!")