def computepay(h, r):
    if(h >  40):
        return (h-40)*(r*1.5)+40*r
    else:
        return h*r

hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate per hour: "))

p = computepay(hrs, rate)
print("Pay", p)