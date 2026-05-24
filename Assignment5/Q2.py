# rock paper scissor game

import random 

l1 = ["rock", "paper", "scissor"] 
while True:
    c = int(input('''Game Start......1 -> YES , 2 -> NO | Exit\n'''))  
    if c == 1:      
        uscore = 0
        cscore = 0
        
        for a in range(1,4):
            uch = 0   

            userinput = int(input('''\nRock /Paper /Scissor\n''')) 

            if userinput == 1:
                uch = "rock" 
            elif userinput == 2:
                uch = "paper"
            elif userinput == 3:
                uch = "scissor"
            else:
                print("invalid choice")
                
            cch = random.choice(l)
            print("Your choice ", uch, "Computer choice", cch) 

            if uch == cch:          
                print("Game Draw")
                uscore += 1
                cscore += 1 
            elif((uch == "rock" and cch == "scissor") or
                 (uch == "paper" and cch == "rock") or 
                 (uch == "scissor" and cch == "paper")):
                    uscore += 2          
                    print("You Win!!")      
            else:
             cscore += 2      
             print("Computer Win!!")    
             
            # according to winning score decides final winner
            if(uscore == cscore): 
                print("\nGame Drawn")
            elif(uscore > cscore):
                print("\nYou Won")    
            elif(cscore > uscore):   
                print("\nComputer Won")          
            else: 
                break 