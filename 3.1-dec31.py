hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))

if hrs > 40:
   bonusPay = (hrs-40)*rate*1.5
   pay = 40*rate+bonusPay
else:
   pay = hrs*rate

print(pay)