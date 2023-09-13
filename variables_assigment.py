###-----------------------------Assigment-----------------------------###

#-----------------------5-1----------------------#
salary = lambda x, y: x*y

hours = int(input("Enter Hours : "))
rate = float(input("Enter Rate : "))

print("Salary : {}".format(salary(hours, rate)))

#-----------------------5-2----------------------#
farenheit = lambda x: (x * (9/5)) + 32

celsius = int(input("Enter Celsius Temperature : "))

print(farenheit(celsius))

#-----------------------5-3----------------------#
def hour_counter(seconds):
    hours = seconds/3600
    minutes = (hours - int(hours)) * 60
    seconds2 = (minutes - int(minutes)) * 60

    return "{x} seconds is {y} hours, {z} minutes, {a} seconds".format(x = seconds, y = int(hours), z = int(minutes), a = int(seconds2))

seconds = int(input("Enter seconds : "))

print(hour_counter(seconds))