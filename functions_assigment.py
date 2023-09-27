def sum_int(nums):
    i = len(nums) - 1
    sum = 0
    if i > 0:
        sum = nums[i] + sum_int(nums[0:i-1])
    return sum

def grade_calculator(score):
    grades = ["F", "D", "C", "B", "A"]
    score = 59 if score < 60 else score
    n = 0
    for i in range(60, 100, 10):
        if score < i:
            return grades[n]
        n += 1
        
    return "A"

def compute_pay(hours, rate):
    if hours > 40:
        extra_pay = (hours - 40) * rate * 1.5
        pay = 40*rate + extra_pay
        return pay
    else:
        return hours * rate

def num_divide3(num):
    nums = []
    for i in range(1, num):
        if i % 3 == 0:
            nums.append(i)
    
    return nums

def main():
    score = input("Enter Score: ")
    try:
        score = int(score)
    except: 
        score = - 1
    
    if score < 0 or score > 100:
        print("Error, please enter numeric input between 0 and 100")
    print("Grade is {}".format(grade_calculator(score)))

   
    hours = input("Enter hours: ")
    rate = input("Enter rate: ")
    try:
        hours = int(hours)
        rate = float(rate)
    except:
        hours = 0
        rate = 0
        print("Incorrect value")
    print("Salary: {}".format(compute_pay(hours, rate)))

    while True:
        num = input("Enter a positive integer : ")
        if num.lower() == "done":
            print("bye !!")
            break
        try:
            num = int(num)
        except:
            num = 0

        if num <= 0:
            print("Please enter a positive number")
            continue

        print("numbers divisible by 3 among numbers from 1 to {} : {}".format(num, len(num_divide3(num))))



if __name__ == "__main__":
    main()
    