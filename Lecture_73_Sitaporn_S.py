systemMenu={"A":10,"B":20,"C":30,"D":40}
menuList=[]


def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])

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
        menuList.append([menuName,systemMenu[menuName]])
showBill()
totalBill()
# print(menuList[0][1])
