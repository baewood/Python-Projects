#This program takes in a genome string and extracts the gene.

#A gene is a substring of a genome that starts after a triple
#ATG and ends before a triple TAG, TAA, or TGA. The length of a gene
#string is a multiple of 3 and the gene does not contain any of the triples
#ATG, TAG, TAA, and TGA.

def main():
    strA = input("Enter a genome string: ") #Must start with TAGx3
    #must end with x3 TAG, TAA or TGA
    

    x = 0
    found = 0
    start = -1
    
    num = len(strA)
    for x in range(num-2):
        gene = strA[x:x+3]

        if gene == "ATG":
            start = x + 3
        elif gene == "TAG" \
         or gene == "TAA" \
         or gene == "TGA":
            genome = strA[start:x]
            if len(genome) %3 == 0:
                found = 1

            print("\n One genome is: %2s" % (gene))
            start = -1

    if found == 0:
        print("No gene found.")


main()

