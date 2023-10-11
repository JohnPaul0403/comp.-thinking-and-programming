file_input = input("Enter a file name : ")
try:
    with open(file_input, "r") as file:
        for line in file : print(line.upper())
except:
    raise FileNotFoundError(f"The file {file_input} does not exist")

count = 0

with open("mbox.txt", "r") as file:
    for line in file:
        if line.startswith("From:"):
            line = line.rstrip()        
            print(line.split("@")[1])
            count += 1

print(f"Total {count} hosts printed")

def get_spam_average(file):
    try:
        open(file)
    except:
        raise FileNotFoundError(f"The file {file} does not exist")
        return

    spam_confidence_values = []

    with open(file, "r") as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:") : spam_confidence_values.append(str(line).split()[1])

    return sum(list(map(lambda x: float(x), spam_confidence_values))) / len(spam_confidence_values)

input_file = input("Enter a file name : ")

print(f"Average spam confidence : {get_spam_average(input_file)}")
