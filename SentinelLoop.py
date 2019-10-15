
# Input a set of numbers (integers) terminated by the value -999.
# Calculate the average, the largest and smallest value in the set of numbers.


def main():
    
    counter = 0
    total = 0
    val = 0 
    average = 0.0
    largest = None
    smallest = None

    val = int(input("Enter a value, or -999 to terminate:"))
    
    while (val != -999):
        counter += 1
        total = total + val
        if largest is None or val > largest:
            largest = val
        if smallest is None or val < smallest:
            smallest = val

        val = int(input("Enter a value, or -999 to terminate:"))

    
    average = total / counter
    print("Average = %4.2f" % ( average))

    print("Largest value = %4.2f" % ( largest))

    print("Smallest value = %4.2f" % ( smallest))


    input("Press ENTER to exit.")

main()
