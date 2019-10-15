#This project takes a file and determines its reading level.
#The file included in one that I used. You can use any file but it must
#be saved in the same folder as your code.


def readingLevel(index):
    fhand = open("shakespeare-romeo-48.txt","r")
    bigString = fhand.read()
    countLove = 0
    word = len(bigString.split())
    syllable = 0

    # The Flesch index says 0-30 is a College reading level.
    # 50 - 60 is High School
    # 90 - 100 is Fourth Grade

    for word in bigString.split():
        for vowel in "AEIOUaeiou":
            syllable += word.count(vowel)
        for ending in "es","ed","e":
            if word.endswith(ending):
                syllable -= 1
            if word.endswith("le"):
                syllable += 1

    sentence = bigString.count(".") + bigString.count("!") + bigString.count("?") + bigString.count(":")
    sents = int(sentence)
    
    G = round((0.39 * len(bigString.split()) / sents + (11.8 * int(syllable)) / len(bigString.split()) - 15.59))

    if G >=0 and G <=30:
        print("The text is at a college reading level.")
    elif G >= 50 and G <=60:
        print("The text is at a high school reading level.")
    else:
        print("The text is at a fourth grade reading level.")

        #Addition to the reading level equation to fit specs given by my professor during this project's construction.

    for x in range(len(bigString)):
        if bigString[x] in "loveLOVE":
            countLove += 1

    print("The amount of times the word love appears in Romeo & Juliet: ", countLove)

    fhand.close()

def main():
    a = readingLevel(index)
    print(readingLevel(a))

    
    input("Press ENTER to exit.")

main()
