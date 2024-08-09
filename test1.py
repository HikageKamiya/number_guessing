import random

num = random.randrange(1000, 9999)

n = int(input('Guess the 4 digit number:'))

if (n == num):
    print('You are the god of rngs!')
else:
    ctr = 0
    while(n != num):
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)
        correct = []
        
        for i in range(0, 4):
            if (n[i] == num[i]):
                
                count += 1
                correct.append(n[i])
                
            else:
                continue
            
        if (count < 4) and (count != 0):
            print(f'You got {count} digit(s) correct!')
        
            n = int(input('Keep gussing: '))
        
        elif(count == 0):
            print('You got none of the numbers correct.')
        
            n = int(input('Keep gussing: '))
    
    if n == num:
        print(f'It took you {ctr} times to win the game!') 