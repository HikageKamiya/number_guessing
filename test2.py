import random

answer = "1234"
a = []
for i in range(4):
    a[i] = random.randint(0, 9)
    
print("a = ", a)
b = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [0]]


store = []

for i in range(len(answer)):
    print("i = ", i)
    if a[i] in b[i]:
        pass    