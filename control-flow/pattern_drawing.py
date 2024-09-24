#promp user for pattern size
size = int(input("Enter the size of the pattern: "))

#Initialize a counter for the while loop
row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row +=1