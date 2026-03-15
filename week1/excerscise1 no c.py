def SumDigits(n):
    String = str(n)
    letters= String.split()
    add = sum(int(letters))
    return add

print(SumDigits(325))