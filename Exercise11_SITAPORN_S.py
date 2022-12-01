heightInput=int(input("height="))

for row in range(heightInput):
        for x in range(heightInput-row-1):
            print(" ",end="")
        for y in range(2*row+1):
             print("*",end="")

        print()

















