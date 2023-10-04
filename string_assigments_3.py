word_input = input("Please enter string : ")
upper_letter = list(filter(lambda x : x.isupper(), word_input))
lower_letter = list(filter(lambda x : x.islower(), word_input))
numbers = list(filter(lambda x : x.isdigit(), word_input))
non_alpha = list(filter(lambda x : not x.isalnum(), word_input))

print("""- Uppercase letters : {}
- Lowercase letters : {}
- Numbers : {}
- Other characters : {}
""".format(len(upper_letter), len(lower_letter), len(numbers), len(non_alpha)))