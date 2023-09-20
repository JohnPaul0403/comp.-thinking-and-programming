#Assigment for week 1 
#In this case is a program with the 3 assigments
#You can choose between the 3 options or quit the program

import os

def first_assigment(hours, rate):
    if hours > 40:
        extra_pay = (hours - 40) * rate * 1.5
        pay = 40*rate + extra_pay
        return pay
    else:
        return hours * rate
    

def grade_calculator(score):
    rounded_score = int(score / 10)
    if rounded_score <=5:
        rounded_score = 5
        
    puntuations = {
        10: "A",
        9 : "A",
        8 : "B",
        7 : "C",
        6 : "D",
        5 : "F",
    }

    return puntuations[rounded_score] 
    
def average_nums():
    nums = []
    while True:
        num = input("Enter a number: ")
        if num.lower() == "done":
            break

        try:
            num = int(num)
            nums.append(num)
        except:
            print("Enter a valid number")
            continue

    print("Sum of input numbers : ", sum(nums))
    print("number of input : ", len(nums))
    
    average = 0
    try :
        average = sum(nums) / len(nums)
    except:
        average = 0

    return average
        
def main():
    while True:
        os.system('clear')
        print("""Assigment week 3
              
    1. First Assigment
    2. Second Assigment
    3. Third Assigment
    0. Quit
    """)
        n = input("Select an option (Number of the option): ")
        try:
            n = int(n)
        except:
            n = -1
        if n == 1:
            os.system('clear')
            hours = input("Enter hours: ")
            rate = input("Enter rate: ")
            try:
                hours = int(hours)
                rate = int(rate)
            except:
                hours = 0
                rate = 0
                print("Incorrect value")
            print("Salary: {}".format(first_assigment(hours, rate)))
            input("Press enter to continue")
        elif n == 2:
            os.system('clear')
            score = input("Enter score between 0-100: ")
            try:
                score = int(score)
            except:
                score = -1
            
            if score < 0 or score > 100 :
                print("Error, please enter numeric input between 0 and 100")
            else:
                print("Grade is {}".format(grade_calculator(score)))

            input("Press enter to continue")
        elif n ==3:
            os.system('clear')
            print("Average of input numbers : {}".format(average_nums()))
            input("Press enter to continue")
        elif n == 0:
            print("See you soon..")
            break
        else:
            os.system('clear')
            print("Incorrect value")
            input("Press enter to continue")
    
if __name__ == "__main__" :
    main()

