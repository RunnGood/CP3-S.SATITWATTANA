menuList=[]


def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number])

def totalBill():
    x = 0
    for number in range(len(menuList)):
        x+=menuList[number][1]
    print("Total :",x)


while True:
    menuName=input("Please Enter Menu :")
    if menuName.lower()== "exit":
        break
    else:
        menuPrice=int(input("Price:"))
        menuList.append([menuName,menuPrice])
showBill()
totalBill()
# print(menuList[0][1])
