#Strings assigment 2

string_input = input("Enter a string: ")
print("Input string = {}".format(string_input))

n = 1

while n <= len(string_input): 
    print(string_input[-n])
    n += 1