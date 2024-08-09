import random

answer = str(random.randint(1000,9999))
#print(answer)
tries = 0
continue_flag = True

def no_guess():
    user_input = str(input("Enter your guess: "))
    result = []
    global tries
    global continue_flag
    if user_input == "answer":
        print(answer)
    else:
        if len(user_input) != len(answer):
            print("Please enter at least and not more than 4 numbers.")
        else:    
            if user_input == answer:
                print(f"You got it right!!\nIt took you {tries} tries!")
                continue_flag = False
            else:
                for i in range(len(answer)):
                    if user_input[i] == answer[i]:
                        result.append("O")
                    elif (user_input[i] in answer) and i != i-1:
                        result.append("T")
                    elif user_input[i] not in answer:
                        result.append("X")
                        
    tries += 1
    print(result)
            
while continue_flag == True:
    no_guess()