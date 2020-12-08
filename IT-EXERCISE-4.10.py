
mpp = 0.12 / 12

pp = float(input("Enter the purchase price: "))

dp = pp * .1
orig = pp - dp
payment = orig * 0.05

print("Month", "Orig. Bal.", "Monthly Interest", "Principal", "Payment", "New Bal.")

month = 0
while orig > payment:
    month += 1

    interest = orig * mpp
    principal = payment - interest
    newBalance = orig - principal

    print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, orig, interest, principal, payment, newBalance))

    orig = newBalance

payment = orig
interest = 0
principal = payment
month = month + 1
newBalance = 0
print("%-1d%10.2f%12.2f%12.2f%7.2f%9.2f" % (month, orig, interest, principal, payment, newBalance))
