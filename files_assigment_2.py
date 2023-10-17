count = 0

with open("mbox.txt", "r") as file:
    for line in file:
        if line.startswith("From:"):
            line = line.rstrip()        
            print(line.split("@")[1])
            count += 1

print(f"Total {count} hosts printed")   