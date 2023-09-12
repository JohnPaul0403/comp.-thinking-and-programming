###-----------------------------Class Practice-----------------------------###

#-----------------------4-1----------------------#
print(int(3.141595)) #Python can covert from Floats to Integers
print(float(365)) #Python converts Integer into floats by adding .0 to the interger
print(str(50)) #Converts to a string
print(float(99) + 100) #Python can sum a float and a string returning a Float

my_string = "Hello " + "there" #Python can concatenate to strings
my_other_string = "{} {}".format("Hello", "world!") #The most efficient way

print(my_string)
print(my_other_string)

print(type(my_other_string))

#my_string = my_string + 1 It can't execute because they are different data types

my_string = "{x} {y}".format(x = my_string, y = 1)#Correct it by format function

print(my_string * 2)#Prints the string twice

#-----------------------4-2----------------------#

age = input('Enter your age : ') #Input from the user, returns a string
print(type(age)) #Returns a string
age = int(input('Enter your age : ')) #Returns a integer cause the formatter
print(type(age))#Returns an Integer

#-----------------------4-3----------------------#

width = 17
height = 12.0

print(type(width // 2))#Returns a integer
print(type(width / 2.0)) #Returns a float
print(type(height / 3)) #Returns a float
print(type(1 + 2 * 5)) #Returns a Integer

#-----------------------4-3----------------------#

name = input("Enter your name : ")

print("Welcome {}".format(name))
