#Q1
'''n=int(input("Enter Lines You Want to Read from last:"))
with open('test.txt','r') as f:
    cc=f.readlines()[-n:]
    for line in cc:
        print(line)'''

#Q2
'''with open("test.txt","r") as f:
    f.read()
    print(f.tell())'''

#Q3
'''with open('test.txt', 'r') as f1:
    with open('Copy2.py', 'w') as f2:
        for line in f1:
            f2.write(line)'''

#Q4
'''with open('test.txt') as fh1, open('copy.py') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)'''


#Q5
'''import random
afile = open("Random.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 9))
    afile.write(line)
    print(line)
afile.close()

f1=open("Random.txt","r")
lines=f1.read()
for l in  lines:
    words=l.split()
    print(words)
f1.close()

f2=open("Random.txt","r")
line=f2.read()
data=sorted(line)
print(data)
f3=open("SortData.txt","w")
f3.write(str(data))
f3.close()
f2.close()'''
