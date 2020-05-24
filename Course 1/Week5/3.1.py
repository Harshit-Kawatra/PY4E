hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate:")
r=float(rate)
rh=r*1.5
if h<=40:
    pay=h*r
elif h>40:
	x=h-40
	pay=40*r+x*rh
print(pay)
