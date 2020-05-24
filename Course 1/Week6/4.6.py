def computepay(h,r):
    return h*r

hrs = input("Enter Hours:")
rate=input("Enter rate:")
x=float(hrs)
y=float(rate)
z=x-40
w=1.5*y
if x<40:
    p=compputepay(x,y)
else:
    p=computepay(z,w)+computepay(40,y)

print("Pay",p)
