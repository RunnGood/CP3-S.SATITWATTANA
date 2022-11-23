print("---Please Log-in---")
username=input("Username:")
password=input("Password:")

if username=="1234" and password=="1234":
        print("~~~ Welcome to No Money Shop ~~~ ")
        print("Product List :")
        print("-----------------------------------")
        print("No.  Item                : Price(THB)")
        print("1.   MAMA                : 5")
        print("2.   WAIWAI              : 10")
        print("3.   YAMYAM              : 15")
        print("4.   PUMPUI Sardine      : 20")
        print("-----------------------------------")
        selectedItem=int(input("Please select Item No. :"))
        print("-----------------------------------")
        if selectedItem==1:
                amountItem1 = int(input("MAMA    Amount:"))
                price1 = 5
                total1 = amountItem1 * price1
                print("MAMA    Total :",total1,"THB")
        elif selectedItem ==2:
                amountItem2 = int(input("WAIWAI  Amount:"))
                price2 = 10
                total2=amountItem2*price2
                print("WAIWAI  Total :", total2, "THB")
        elif selectedItem ==3:
                amountItem3 = int(input("YAMYAM  Amount:"))
                price3 = 15
                total3 = amountItem3 * price3
                print("YAMYAM  Total :", total3, "THB")
        elif selectedItem == 4:
                amountItem4 = int(input("PUMPUI Sardine Amount:"))
                price4 = 20
                total4 = amountItem4 * price4
                print("PUMPUI Sardine  Total :", total4, "THB")
        else:
                print("we don't have this item No.!!!")
else:
        print("!!!Please try Again!!!")

