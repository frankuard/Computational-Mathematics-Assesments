def myPow(x,n):
    XpowerN= 1
    counter = 0
    while counter< n:
        XpowerN *= x
        counter +=1
        
    return XpowerN

print(myPow(2,3))

