import random

answer_gen = []
answer = ""
for i in range(4):
    answer += str(random.randint(0, 9))
#answer = str(random.randint(1000,9999))
print(f"Answer = {answer}")

tries = 0
continue_flag = True
bot_chg = ["True", "True", "True", "True"]
bot_input = ""
bot_list = []
bot_wrong = -1

botbot = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
          ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
          ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
          ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]] # numbers available
for i in range(len(answer)):
    bot_list.append(random.randint(0,9))
    
bot_try = [] # try this number

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
    
    result = ["a","a","a","a"]
    
    bot_list_store = bot_list   # save answer
            
    bot_input = ""
    
    for i in range(len(answer)):
        bot_input += str(bot_list[i])
    #print(f"bot_input = {bot_input}\nbot_list = {bot_list}")
    
    if bot_input == "answer":
        print(answer)
    else:
        if bot_input == answer:
            print(f"You lost!!\nIt took you {tries} tries to lose!.")
            continue_flag = False
        else:
            for i in range(len(answer)):
                if bot_input[i] == answer[i]:
                    result[i] = "O"
                else:
                    if (bot_input[i] in answer):
                        result[i] = "T"
                    elif bot_input[i] not in answer:
                        result[i] = "X"
                        
    print(f"Bot: {result}")
    for i in range(len(answer)):
        if result[i] == "T":    # right num but wrong place
            botbot[i].remove(bot_input[i])
            bot_try = bot_input[i]  # try this number here for other places
        elif result[i] == "X":  # wrong num
            bot_wrong = bot_input[i]
            for j in range(4):
                if bot_wrong in botbot[j]:
                    botbot[j].remove(bot_wrong)
    #print(f"Bot: {botbot}")
    
    bot_list = bot_guesser(result, botbot, bot_try, bot_input)
                    
    
    

def bot_guesser(bot_result, botbot, bot_try, bot_input):
    bot_list = ["b", "b", "b", "b"]
    
    for i in range(len(answer)):
        if bot_result[i] == "O":    #right num
            bot_list[i] = bot_input[i]
        elif bot_result[i] == "X":  # wrong num
            if(bot_try in botbot[i]):
                bot_list[i] = bot_try
            else:
                if len(botbot[i])-1 > 1:
                    bot_list[i] = botbot[i][random.randint(1, len(botbot[i])-1)]
                else:
                    bot_list[i] = botbot[i][0]
        elif bot_result[i] == "T":  #right num but wrong place
            if(bot_try in botbot):
                bot_list[i] = bot_try
            else:
                if len(botbot[i])-1 > 1:
                    bot_list[i] = botbot[i][random.randint(1, len(botbot[i])-1)]
                else:
                    bot_list[i] = botbot[i][0]
            
    return bot_list
        
            
while continue_flag == True:
    player_guess()
    bot_guess()