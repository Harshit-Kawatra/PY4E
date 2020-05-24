import re
fname=input("Enter file name")
fh=open(fname)
sum=0
for line in fh:
    for x in re.findall('[0-9]+',line):
        sum=sum+int(x)

print(sum)
