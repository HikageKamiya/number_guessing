import random

a = [1,3,5,7,9]

b = random.randint(0,9)
print("b = ", b)

while b in a:
     b = random.randint(0, 9)
     

print(b)