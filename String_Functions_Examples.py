# Name: Brittany Wood
# Date: 11/2/2018
# Description: String Functions Program A & B


def twice(strA):
    strAA = strA + " " + strA
    return strAA

def countVowels(strA):
    count = 0
    l = len(strA)
    for x in range(l):
        if strA[x] in "AEIOUaeiou":
             count = count + 1
    return count
         
def upperAll(strA):
    if strA[ : ].lower():
        return strA[ : ].upper()

def lowerAll(strA):
    if strA[ : ].upper():
        return strA[ : ].lower()

def countChar(strA, ch):
    count = 0
    l = len(strA)
    for x in range(l):
        if ch == "o" in strA[x]:
             count = count + 1
    return count

#___________    

def main():
    
    A = input("Please enter a sentence:")
    B = "o"

    print("This counts your string twice: %3s" % (twice(A)))

    print("\nYour string has the following number of vowels: %3d" % (countVowels(A)))

    print("\nYour sentence in all caps: %3s" % (upperAll(A)))

    print("\nYour sentence in all lowercase: %3s" % (lowerAll(A)))

    print("\nThe amount of times the character, O, appears in the string: %3d" % (countChar(A, B)))

    input("Press ENTER to exit.")

main()
