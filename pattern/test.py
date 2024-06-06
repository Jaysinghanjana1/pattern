#print for a star 
n = int(input("enter the number to print a star:"))
for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end="")
    else:
        print("")