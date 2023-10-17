#Assimgent 1 Week 6 File Managment

#Input file name with directory
file_input = input("Enter a file name : ")

#Try to open the file
#In case it can't it will just display an error message
try:
    with open(file_input, "r") as file:
        #Creates a for loop for each line and then prints it in uppercase
        for line in file : print(line.rstrip().upper())
except:
    #Error message
    print(f"The file {file_input} does not exist")   