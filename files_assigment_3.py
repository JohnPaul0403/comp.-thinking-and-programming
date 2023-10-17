def get_spam_average(file):
    spam_confidence_values = []

    with open(file, "r") as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:") : spam_confidence_values.append(float(str(line).split()[1]))

    return sum(spam_confidence_values) / len(spam_confidence_values)

input_file = input("Enter a file name : ")

try:
    open(input_file)
    print(f"Average spam confidence : {get_spam_average(input_file)}")
except:
    print(f"File cannot be opened : {input_file}")
   