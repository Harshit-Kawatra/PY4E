'''7.2 Write a program that prompts for a file name, then opens that file
and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
 Do not use the sum() function or a variable named sum in your solution.'''

#Use file name mbox-short.txt as the file name
count=0
tot=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    s=line.find(':')
    a=line[s+1:]
    try:
        a=float(a)
    except:
        print("Cannot convert")
        quit()
    tot=tot+a
    count=count+1
avg=tot/count
print("Average spam confidence:",avg)
