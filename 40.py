f = open('pgm40.csv')
total = 0
for line in f:
    if "m" in line: 
        total +=1
f.close()
print (total)


