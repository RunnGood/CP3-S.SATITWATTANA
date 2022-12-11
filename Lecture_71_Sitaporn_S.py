menuList=[]
priceList=[]

def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
def totalBill():
    # for number in range(len(priceList)):
        print("Total :",sum(priceList))

while True:
    menuName=input("Please Enter Menu :")
    if menuName.lower()== "exit":
        break
    else:
        menuPrice=int(input("Price:"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
totalBill()

