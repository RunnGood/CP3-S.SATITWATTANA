def vatCalulator(totalprice):
    result=totalprice+(totalprice*7/100)
    return result
print(vatCalulator(int(input())))

