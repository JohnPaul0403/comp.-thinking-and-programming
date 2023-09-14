###-----------------------------Class Practice-----------------------------###

#-----------------------2-1----------------------#
print(type(None))
print(type(True))
xx = 1
print(type(xx))
temp = 98.6
print(type(temp))
print(type(1))
print(type(1.0))
print(type("Hello World!"))
print(type("-1.0"))
print(type(1+2)) #Class complex

print("""Hello World!
Hello World! 2
Hello World! 3
""")
      
print("\tHello")# Tab Action
print("Good \"Morning\"")
print("\\\\Hello")#Backlash

x, y = [10, 20]#Can be assigned as 2 variables, a list or a tuple

print("{} {}".format(x, y))

#-----------------------3-1----------------------#
#Id

print("id(2):", id(2))

prompt = "Enter speed of the car \n"
speed = input(prompt)
print(speed)
print(type(speed))
speed = int(speed)
speed + 5
print(speed)

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

my_string = "{x} + {y}".format(x = my_string, y = 1)#Correct it by format function

print(my_string * 2)#Prints the string twice

#-----------------------4-2----------------------#

age = input('Enter your age : ') #Input from the user, returns a string
print(type(age)) #Returns a string
age = int(input('Enter your age : ')) #Returns a integer cause the formatter
print(type(age))#Returns an Integer

#-----------------------4-3----------------------#

width = 17
height = 12.0

data = [width // 2, width / 2.0, height / 3, 1 + 2 * 5]

for i in data: print(i)
for i in data: print(type(i))

print(width // 2)
print(type(width // 2))#Returns a integer
print(width / 2.0)
print(type(width / 2.0)) #Returns a float
print(height / 3)
print(type(height / 3)) #Returns a float
print(1 + 2 * 5)
print(type(1 + 2 * 5)) #Returns a Integer

#-----------------------4-4----------------------#

name = input("Enter your name : ")

print("Welcome {}".format(name))

