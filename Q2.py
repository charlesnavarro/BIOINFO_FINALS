#BIOINFO MIDTERM Q1
import numpy


#tacggtat
f = open("1-AY278489.2.txt", "r")
if f.mode == 'r':
    x = (f.read()).lower()
#ggacgtacg
f = open("2-AY394997.1.txt", "r")
if f.mode == 'r':
    y = (f.read()).lower()
print(x, y)

score = 0
total = 0
miss = 0


# if(len(x)>len(y)):
#     g = 1 * (len(y) - len(x))
# elif(len(y)> len(x)):
#     g = 1 * (len(x) - len(y))
# elif(len(x) == len(y)):
#     g = 0


for i in range(0, len(y)+1):
        #NOT A BASE CASE
        if(i != 0):
            # score = getScore(i, j, g)
            # scoreTable[i][j] = score
            if(x[i-1] == "a" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "a" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "a" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "a" and y[i-1] == "a"):
                total = total + 1
            if (x[i-1] == "c" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "c" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "c" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "c" and y[i-1] == "c"):
                total = total + 1
            if (x[i-1] == "t" and y[i-1] == "g"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "t" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "t" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "t" and y[i-1] == "t"):
                total = total + 1
            if (x[i-1] == "g" and y[i-1] == "a"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "g" and y[i-1] == "c"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "g" and y[i-1] == "t"):
                miss = miss + 1
                total = total + 1
            if (x[i-1] == "g" and y[i-1] == "g"):
                total = total + 1

fraction = miss / total
print(miss)
print(total)
print(fraction)
