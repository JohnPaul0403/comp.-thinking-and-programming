while True: 
    word_input = input("Enter two letters: ")
    if word_input.lower() == "done" or word_input == "" : break

    word_input = word_input.split(" ")

    try : 
        list(map(lambda x : int(x), word_input))
        word_input = []
    except : pass

    if len(word_input) <= 1 : continue

    print("{} comes first".format(sorted(word_input)[0]))

print("-- bye!")