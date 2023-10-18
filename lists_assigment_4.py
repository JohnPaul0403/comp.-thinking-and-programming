#Lists Assignment 1

#This function recives and array of integers as input
#It returns the average of the elements in the array rounded by 2 decimals
#In case there's only 1 element and it's iquals to 0 it just returns 0
def get_average(arr):
    if len(arr) == 1 and arr[0] == 0: return 0
    return round(sum(arr)/len(arr), 2)

#Main function
def main():
    #Variable decalaration
    nums = []

    #Instructions for the user
    print("Typing 'done' will exit the program")

    #Start of the program
    while True:
        input_number = input("Please enter an integer : ")

        if input_number == "done" : break

        try:
            input_number = int(input_number)
        except ValueError:
            print("Please enter a valid number")
            continue

        nums.append(input_number)
        print(f"{nums} , average = {get_average(nums)}")
    
    print("---------- Bye !! --------------")

main()