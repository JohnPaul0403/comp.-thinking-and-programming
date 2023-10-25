#Note from the class 
import random

x = 3
y = 3

print(x is y)#True
nums = [2,3,4,5,6,7]

print(x in nums)#Also true because 3 is in nums

y = 0

print(x < 2 and x/y > 2)#Python in conditions will not have errors by dividing by zero

nums = []

for i in range(10) : nums.append(random.randint(0, 100))

for score in nums: print("Passed") if score >= 70 else print("Failure")

print(list(map(lambda x : float(x), nums)))

friends = ["Joe", "Emi", "Json"]

list(map(lambda x : print("Happy new year: {}".format(x)), friends))


if x > 100:
    if x < 1000:
        pass

def hey(x) : 
    if x == 1000:
        print("X is equal to 1000")
        return
    elif x > 1000:
        print("X is greater to 1000")
        return
    
    if x > 100 and x < 1000:
        print("Greaer than 100 and lower than 1000")
        return
  
    if x == 100:
        print("x equl to 100")
        return
    
    return "x is lower than 100"

try:
    age = int(input("Give me your age: "))
except:
    print("Incorrect value")
else:
    if age <= 18:
        print("Minors are prohibited")
    else:
        print("Welcome")

number = int(input("Display a multiplication table of number? "))

for i in range(1, 9) : print("{} x {} = {}".format(number, i, number*i))