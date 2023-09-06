def sum(n1, n2):
    return n1 + n2

def rest(n1, n2):
    return n1 - n2

def main():
    n1 = int(input ("First number: "))
    while True:
        n = input("Sum (1) / Rest(2) / Quit (Q)")

        if n == "Q" :
            break
        
        if n == "1" :
            n2 = int(input ("Number 2: "))
            n1 = sum(n1, n2)
            print(n1)

        if n == "2":
            n2 = int(input ("Number 2: "))
            n1 = rest(n1, n2)
            print(n1)

main()