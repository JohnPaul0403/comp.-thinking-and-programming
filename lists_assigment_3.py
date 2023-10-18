#Lists Assignment 1

#Variable declaration
n = 0

#Opening the file in read mode
with open("mbox.txt", "r") as file:
    for line in file:
        #Seeks if the line starts with 'From' and not with 'From:'
        if line.startswith("From:") : continue
        if line.startswith("From"):
            print(line.split()[1])
            n += 1

#Outputs the amount of lines printed
print(f"Total {n} lines were printed")