#String asigment 3

word_input = input("Please enter string : ")

#Filtering the values of the string
upper_letter = list(filter(lambda x : x.isupper(), word_input))
lower_letter = list(filter(lambda x : x.islower(), word_input))
numbers = list(filter(lambda x : x.isdigit(), word_input))
non_alpha = list(filter(lambda x : not x.isalnum(), word_input))

#Priting the len of each list
print("""- Uppercase letters : {}
- Lowercase letters : {}
- Numbers : {}
- Other characters : {}
""".format(len(upper_letter), len(lower_letter), len(numbers), len(non_alpha)))