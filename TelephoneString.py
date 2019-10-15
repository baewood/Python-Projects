#This program converts a string into numbers based on their location
#on a telephone pad. 

def getNumber(uL):
    if (uL == "a" or uL =="b" or uL == "c" or uL == "A" or uL == "B" or uL == "C"):
        return (2)
    elif (uL == "d" or uL == "e" or uL == "f" or uL == "D" or uL == "E" or uL == "F"):
        return (3)
    elif (uL == "g" or uL == "h" or uL == "i" or uL == "G" or uL == "H" or uL == "I"):
        return (4)
    elif (uL == "k" or uL == "l" or uL == "j" or uL == "K" or uL == "L" or uL == "J"):
        return (5)
    elif (uL == "m" or uL == "n" or uL == "o" or uL == "M" or uL == "N" or uL == "O"):
        return (6)
    elif (uL == "p" or uL == "q" or uL == "r" or uL == "s" or uL == "P" or uL == "Q" or uL == "R" or uL == "S"):
        return (7)
    elif (uL == "t" or uL == "u" or uL == "v" or uL == "T" or uL == "U" or uL == "V"):
        return (8)
    elif (uL == "w" or uL == "x" or uL == "y" or uL == "z" or uL == "W" or uL == "X" or uL == "Y" or uL == "Z"):
        return (9)
    else:
        return (0)
    
def main():
    sA = input("Enter string:")
    l = len(sA)

    print("The number is:")
    
    for x in range(l):
        a = sA[x]
        b = getNumber(a)

        if(b == 0):
            print(a,end="")
        else:
            print(b,end="")
        
    input("\nPress ENTER to exit.")

main()

