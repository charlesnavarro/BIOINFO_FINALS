#BIOINFO MIDTERM Q1
import numpy


'''
Sij = max
max = Si-1, j-1 + M[X[i],Y[j]]
    = Si-1, j+gap
    = Si, j-1+gap

'''

#tacggtat
f = open("string1.txt", "r")
if f.mode == 'r':
    x = (f.read())
#ggacgtacg
f = open("string2.txt", "r")
if f.mode == 'r':
    y = (f.read())
print(x, y)
#gap = d

match = input("what score would you like for a match?")
type(match)
match = int(match)

mismatch = input("What score would you like for a mismatch?")
type(mismatch)
mismatch = int(mismatch)

gap = input("What gap penalty would you like?")
type(gap)
gap = int(gap)

matrix = numpy.zeros(shape=(4, 4), dtype=int)
for m in range(4):
    for m1 in range(4):
        if(m == m1):
            matrix[m][m1] = match
        if(m != m1):
            matrix[m][m1] = mismatch

print(matrix)

def getMax (m1, m2, m3):
    max = m1
    if(m2 > m1):
        max = m2
    if(m2 > m3):
        if (m2 > max):
            max = m2
    if(m3 > m1):
        if(m3 > max):
            max = m3
    if(m3 > m2):
        if (m3 > max):
            max = m3
    return max

def getScore (i, j, g):
    m1 = 0
    m2 = 0
    m3 = 0
    max = 0
    print(i-1, j-1)
    m2 = scoreTable[i][j - 1] + g
    m3 = scoreTable[i - 1][j] + g
    #a compared to all
    if (x[j-1] == 'a' and y[i-1] == 'a'):
        m1 = scoreTable[i - 1][j - 1] + matrix[0][0]
        print("aa")
    elif (x[j-1] == 'a' and y[i-1] == 'c'):
        m1 = scoreTable[i - 1][j - 1] + matrix[0][1]
        print("ac")
    elif (x[j-1] == 'a' and y[i-1] == 't'):
        m1 = scoreTable[i - 1][j - 1] + matrix[0][2]
        print("at")
    elif (x[j-1] == 'a' and y[i-1] == 'g'):
        m1 = scoreTable[i - 1][j - 1] + matrix[0][3]
        print("ag")
    #c paired to all
    elif (x[j-1] == 'c' and y[i-1] == 'a'):
        m1 = scoreTable[i - 1][j - 1] + matrix[1][0]
        print("ca")
    elif (x[j-1] == 'c' and y[i-1] == 'c'):
        m1 = scoreTable[i - 1][j - 1] + matrix[1][1]
        print("cc")
    elif (x[j-1] == 'c' and y[i-1] == 't'):
        m1 = scoreTable[i - 1][j - 1] + matrix[1][2]
        print("ct")
    elif (x[j-1] == 'c' and y[i-1] == 'g'):
        m1 = scoreTable[i - 1][j - 1] + matrix[1][3]
        print("cg")
    #t compared to all
    elif (x[j-1] == 't' and y[i-1] == 'a'):
        m1 = scoreTable[i - 1][j - 1] + matrix[2][0]
        print("ta")
    elif (x[j-1] == 't' and y[i-1] == 'c'):
        m1 = scoreTable[i - 1][j - 1] + matrix[2][1]
        print("tc")
    elif (x[j-1] == 't' and y[i-1] == 't'):
        m1 = scoreTable[i - 1][j - 1] + matrix[2][2]
        print("tt")
    elif (x[j-1] == 't' and y[i-1] == 'g'):
        print("tg")
        m1 = scoreTable[i - 1][j - 1] + matrix[2][3]
    #g compared to all
    elif (x[j-1] == 'g' and y[i-1] == 'a'):
        m1 = scoreTable[i - 1][j - 1] + matrix[3][0]
        print("ga")
    elif (x[j-1] == 'g' and y[i-1] == 'c'):
        m1 = scoreTable[i - 1][j - 1] + matrix[3][1]
        print("gc")
    elif (x[j-1] == 'g' and y[i-1] == 't'):
        m1 = scoreTable[i - 1][j - 1] + matrix[3][2]
        print("gt")
    elif (x[j-1] == 'g' and y[i-1] == 'g'):
        m1 = scoreTable[i - 1][j - 1] + matrix[3][3]
        print("gg")

    max = getMax(m1, m2, m3)

    # if ((i == 3 and j == 4) or (i == 9 and j == 6)):
    #     print(m2, m3, max)
    #     print("HERE")
    print(i, j, g)
    print(m1, m2, m3, max)
    return max

score = 0
total = 0
miss = 0
scoreTable = numpy.zeros(shape=(len(y)+1, len(x)+1), dtype=int)
#            r  c
# scoreTable[0][1] = 1

if(len(x)>len(y)):
    g = gap * (len(y) - len(x))
elif(len(y)> len(x)):
    g = gap * (len(x) - len(y))
elif(len(x) == len(y)):
    g = 0
print(g)

for i in range(0, len(y)+1):
    for j in range(0, len(x)+1):
        #NOT A BASE CASE
        if(i != 0 and j != 0):
            score = getScore(i, j, g)
            scoreTable[i][j] = score
            if(x[j-1] == "a" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "a" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "a" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "a" and y[i-1] == "a"):
                total = total + 1
            if (x[j-1] == "c" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "c" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "c" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "c" and y[i-1] == "c"):
                total = total + 1
            if (x[j-1] == "t" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "t" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "t" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "t" and y[i-1] == "t"):
                total = total + 1
            if (x[j-1] == "g" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "g" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "g" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[j-1] == "g" and y[i-1] == "g"):
                total = total + 1
        #BASE CASE
        if(i == 0):
            scoreTable[i][j] = j * g
        #BASE CASE
        elif(j == 0):
            scoreTable[i][j] = i * g
        print(scoreTable, "\n")
fraction = miss / total
print(miss)
print(total)
print(fraction)
