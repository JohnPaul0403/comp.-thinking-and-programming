#Lists Assignment 1

#Declaration of the list nums 
nums = [1, 2, 3, 4]

#This function uses the method remove to remove the first and the last element of the array
#It returns None
def chop(nums) -> None: 
    nums.remove(nums[0])
    nums.remove(nums[-1])
    return None

#Printing the list before and after calling the chop function
print(f"my list before call chop function => {nums}")
chop(nums)
print(f"my list after call chop  function => {nums}")

#Declaration the function middle 
#Returns a list without the first and last element of the input list
def middle(arr) : return arr[1:-1]

#Declaration of variables
my_list = [1,2,3,4]

#Printing the variable before calling the middle function
print(f"my list before call middle function => {my_list}")

#Saving the new list in a variable
new_list = middle(my_list)

#Printing the variable after calling the middle function
print(f"""my list after call middle function => {my_list}
new list after call middle function => {new_list}""")
