#Lists Assignment 1

#Variable declaration
unique_words_list = []

#Opening the file in read mode
with open("romeo.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if not word in unique_words_list:
                unique_words_list.append(word)

#Print the unique sorted words
print(sorted(unique_words_list))
