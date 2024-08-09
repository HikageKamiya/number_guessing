import random

answer = str(random.randint(1000,9999))

tries = 0
continue_flag = True
bot_chg = ["True", "True", "True", "True"]
bot_input = ""
bot_list = []
botbot = []
for i in range(len(answer)):
    bot_list.append(random.randint(0,9))
bot_try = [[],
           [],
           [],
           []]

def player_guess():
    player_input = str(input("Enter your guess: "))
    result = []
    global tries
    global continue_flag
    if player_input == "answer":
        print(answer)
    else:
        if len(player_input) != len(answer):
            print("Please enter at least and not more than 4 numbers.")
        else:    
            if player_input == answer:
                print(f"You won!!\nIt took you {tries} tries!")
                continue_flag = False
            else:
                for i in range(len(answer)):
                    if player_input[i] == answer[i]:
                        result.append("O")
                    elif (player_input[i] in answer):
                        result.append("T")
                    elif player_input[i] not in answer:
                        result.append("X")
                        
    tries += 1
    print(f"You: {result}\n")
    
def bot_guess():
    global bot_list
    global bot_chg
    global continue_flag
    global bot_input
    global bot_try
    global botbot
    
    result = []
    
    bot_list_store = bot_list       
            
    bot_input = ""
    
    for i in range(len(answer)):
        bot_input += str(bot_list[i])
    print(f"bot_input = {bot_input}\nbot_list = {bot_list}")
    
    if bot_input == "answer":
        print(answer)
    else:
        if bot_input == answer:
            print(f"You lost!!\nIt took you {tries} tries to lose!.")
            continue_flag = False
        else:
            for i in range(len(answer)):
                if bot_input[i] == answer[i]:
                    result.append("O")
                else:
                    if (bot_input[i] in answer):
                        result.append("T")
                    elif bot_input[i] not in answer:
                        result.append("X")
                        
    print(f"Bot: {result}")
    for i in range(len(answer)):
        if result[i] == "O":
            bot_chg[i] = "False"
        elif result[i] == "T":
            bot_try[i].append(bot_input[i])
            bot_chg[i] = "try"
        elif result[i] == "X":
            bot_try[i].append(bot_input[i])
            bot_chg[i] = "True"
            botbot.append(bot_input[i])
            
    for i in range(len(answer)):
        if bot_chg[i] == "True":    # need to change the num
            bot_list[i] = random.randint(0,9)   # X
            while bot_list[i] in botbot:
                bot_list[i] = random.randint(0,9)
        elif bot_chg[i] == "False":     # the num is correct
            bot_list[i] = bot_list_store[i] # O
        elif bot_chg[i] == "try":       # try other slots
            bot_list[i] = random.randint(0,9)   # T
            while ((bot_list[i] in bot_try[i]) or (bot_list[i] in botbot)):
                bot_list[i] = random.randint(0,9)
                
    print(f"bot try = {bot_try}")
    print(f"botbot = {botbot}")
    print("\n")
            
        
            
while continue_flag == True:
    player_guess()
    bot_guess()