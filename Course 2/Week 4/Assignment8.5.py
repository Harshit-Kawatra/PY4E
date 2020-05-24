fname=input("Enter File Name: ")
fh = open(fname)
count=0
lst=list()
for line in fh:
    if line.startswith("From:") : continue
    if not line.startswith("From") : continue
    count=count+1
    lst=line.split()
    print(lst[1])
print("There were", count, "lines in the file with From as the first word")
