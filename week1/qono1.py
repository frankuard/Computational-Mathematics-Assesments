hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the rate per hour:")
r = float(rate)

if h<40:
    pay = r * h
    print(f"The hourly rate of {r} for {h} hours is {pay:.2f}")



else:
    pay1 = 40 * r
    
    h1 = h - 40 
    r = r*1.5
    pay2 = r * h1
    
    pay = pay1 + pay2
    print(f"The hourly rate of {r} for {h} hours is {pay:.2f}")