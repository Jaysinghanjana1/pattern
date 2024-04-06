n=int(input("enter the number"))
for i in range(n):
    for j in range(n):
        if(j<=i):
            print("*",end="")
        else:
            print("")