import random
import time
a = list("          ")
global booleen


def win_condition(player_turn, i):    
    if (a[1] == a[2] == a[3] != " " or
        a[4] == a[5] == a[6] != " " or
        a[7] == a[8] == a[9] != " " or
        a[1] == a[4] == a[7] != " " or
        a[2] == a[5] == a[8] != " " or  
        a[3] == a[6] == a[9] != " " or  
        a[1] == a[5] == a[9] != " " or 
        a[3] == a[5] == a[7] != " "):
        player_turn = player_2 if player_turn == player_1 else player_1
        print(f"{player_turn} a gagné  en {i} tours !") 
        return True
        
    if i == 9:
        print("Match nul.")
        return True
    
    return False
def display_board():
    print("\n")
    print("\t     |     |")
    print(f"\t {a[7]}   |  {a[8]}  |  {a[9]}                7 | 8 | 9") 
    print('\t_____|_____|_____             ---|---|---')
    print("\t     |     |                   4 | 5 | 6")
    print(f"\t {a[4]}   |  {a[5]}  |  {a[6]}               ---|---|---")  
    print('\t_____|_____|_____              1 | 2 | 3')
    print("\t     |     |")
    print(f"\t {a[1]}   |  {a[2]}  |  {a[3]}") 
    print("\t     |     |")
    print("\n")

def game_logic():
  used_a = list()   
  i = 0
  victory = False
  player_turn=player_1
  turn = True
 
  while i < 9:
        display_board()
        print("tour de",player_turn)
        player_moove = input("Entrez la case souhaitée (1-9): ")

        if player_moove not in "1,2,3,4,5,6,7,8,9" or not player_moove:
            print("caractere non valide, entrez un caractere compris entre 12345679")
            continue
        
        k=int(player_moove)
       
        if str(k) in used_a:
         print("Case déjà utilisée.")
         continue
        
        if turn:  
            a[k] = "X"
            turn = False  
            player_turn=player_2
        else:  
            a[k] = "O"
            turn = True  
            player_turn=player_1
        used_a.append(str(k))  
        i += 1
        
        victory = win_condition(player_turn,i)
        
        if victory:
          display_board()
          break

def game_logic2():
    global booleen
    global used_a
    used_a = list()   
    i = 0
    victory = False
    global player_turn
    global turn
 
    while i < 9:
        display_board()
        print("tour de",player_turn)
        if booleen==False:
            player_moove = input("Entrez la case souhaitée (1-9): ")

            if player_moove not in "1,2,3,4,5,6,7,8,9" or not player_moove:
                print("caractere non valide, entrez un caractere compris entre 12345679")
                continue
            
            k=int(player_moove)
        
            if str(k) in used_a:
                print("Case déjà utilisée.")
                continue           
           
            a[k] = "x"
            turn = True  
            player_turn=player_2
            used_a.append(str(k)) 
            booleen=True
        else:
            security1()
            if booleen==True:
                security()
                if booleen==True:
                    deuxieme_coup()                      
                    if booleen==True:
                        second_shot()                  
                        if booleen==True:
                            third_shot()              
                            if booleen==True:
                                first_shot()
                            
            time.sleep(1)
            turn = False  
            player_turn=player_1
            
        i += 1
            
        victory = win_condition(player_turn,i)
        
        if victory:
          display_board()
          break
        

def security1():
    global booleen
    if a[1]==a[2]=="o" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[4]==a[5]=="o" and a[6]==" ":
        a[6]="o"
        booleen=False
        used_a.append(str(6))
    elif a[7]==a[8]=="o" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[2]==a[3]=="o" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[5]==a[6]=="o" and a[4]==" ":
        a[4]="o"
        booleen=False
        used_a.append(str(4))
    elif a[8]==a[9]=="o" and a[7]==" ":
        a[7]="o"
        booleen==False
        used_a.append(str(7))
    elif a[1]==a[4]=="o" and a[7]==" ":
        a[7]="o"
        booleen=False
        used_a.append(str(7))
    elif a[4]==a[7]=="o" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[2]==a[5]=="o" and a[8]==" ":
        a[8]="o"
        booleen=False
        used_a.append(str(8))
    elif a[8]==a[5]=="o" and a[2]==" ":
        a[2]="o"
        booleen=False
        used_a.append(str(2))
    elif a[6]==a[9]=="o" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[6]==a[3]=="o" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[1]==a[3]=="o" and a[2]==" ":
        a[2]="o"
        booleen=False
        used_a.append(str(2))
    elif a[4]==a[6]=="o" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[7]==a[9]=="o" and a[8]==" ":
        a[8]="o"
        booleen=False
        used_a.append(str(8))
    elif a[1]==a[7]=="o" and a[4]==" ":
        a[4]="o"
        booleen=False
        used_a.append(str(4))
    elif a[2]==a[8]=="o" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[3]==a[9]=="o" and a[6]==" ":
        a[6]="o"
        booleen=False
        used_a.append(str(6))
    elif a[1]==a[5]=="o" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[9]==a[5]=="o" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[1]==a[9]=="o" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[7]==a[5]=="o" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[3]==a[5]=="o" and a[7]==" ":
        a[7]="o"
        booleen=False
        used_a.append(str(7))
    elif a[7]==a[3]=="o" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))

            



def security():
    global booleen
    if a[1]==a[2]=="x" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[4]==a[5]=="x" and a[6]==" ":
        a[6]="o"
        booleen=False
        used_a.append(str(6))
    elif a[7]==a[8]=="x" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[2]==a[3]=="x" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[5]==a[6]=="x" and a[4]==" ":
        a[4]="o"
        booleen=False
        used_a.append(str(4))
    elif a[8]==a[9]=="x" and a[7]==" ":
        a[7]="o"
        booleen==False
        used_a.append(str(7))
    elif a[1]==a[4]=="x" and a[7]==" ":
        a[7]="o"
        booleen=False
        used_a.append(str(7))
    elif a[4]==a[7]=="x" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[2]==a[5]=="x" and a[8]==" ":
        a[8]="o"
        booleen=False
        used_a.append(str(8))
    elif a[8]==a[5]=="x" and a[2]==" ":
        a[2]="o"
        booleen=False
        used_a.append(str(2))
    elif a[6]==a[9]=="x" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[6]==a[3]=="x" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[1]==a[3]=="x" and a[2]==" ":
        a[2]="o"
        booleen=False
        used_a.append(str(2))
    elif a[4]==a[6]=="x" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[7]==a[9]=="x" and a[8]==" ":
        a[8]="o"
        booleen=False
        used_a.append(str(8))
    elif a[1]==a[7]=="x" and a[4]==" ":
        a[4]="o"
        booleen=False
        used_a.append(str(4))
    elif a[2]==a[8]=="x" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[3]==a[9]=="x" and a[6]==" ":
        a[6]="o"
        booleen=False
        used_a.append(str(6))
    elif a[1]==a[5]=="x" and a[9]==" ":
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[9]==a[5]=="x" and a[1]==" ":
        a[1]="o"
        booleen=False
        used_a.append(str(1))
    elif a[1]==a[9]=="x" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))
    elif a[7]==a[5]=="x" and a[3]==" ":
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[3]==a[5]=="x" and a[7]==" ":
        a[7]="o"
        booleen=False
        used_a.append(str(7))
    elif a[7]==a[3]=="x" and a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))


def first_shot():
    global booleen
    if a[1]!="x" and a[4]!="x" and a[7]!="x" and a[8]!="x" and a[9]!="x" and a[1]!="o" and a[4]!="o" and a[7]!="o" and a[8]!="o" and a[9]!="o" :
        n_random =random.randint(0,1)
        if n_random==1:
            a[1]="o"
            booleen=False
            used_a.append(str(1))
        else:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
    elif a[3]!="x" and a[6]!="x" and a[7]!="x" and a[8]!="x" and a[9]!="x" and a[3]!="o" and a[6]!="o" and a[7]!="o" and a[8]!="o" and a[9]!="o" :
            n_random =random.randint(0,1)
            if n_random==1:
                a[7]="o"
                booleen=False
                used_a.append(str(7))
            else:
                a[3]="o"
                booleen=False
                used_a.append(str(3))
    elif a[1]!="x" and a[3]!="x" and a[2]!="x" and a[6]!="x" and a[9]!="x" and a[1]!="o" and a[3]!="o" and a[2]!="o" and a[6]!="o" and a[9]!="o" :
            n_random =random.randint(0,1)
            if n_random==1:
                a[1]="o"
                booleen=False
                used_a.append(str(1))
            else:
                a[9]="o"
                booleen=False
                used_a.append(str(9))
    elif a[1]!="x" and a[4]!="x" and a[7]!="x" and a[2]!="x" and a[3]!="x" and a[1]!="o" and a[4]!="o" and a[7]!="o" and a[2]!="o" and a[3]!="o" :
        n_random =random.randint(0,1)
        if n_random==1:
            a[3]="o"
            booleen=False
            used_a.append(str(3))
        else:
            a[7]="o"
            booleen=False
            used_a.append(str(7))
    elif a[5]==" ":
        a[5]="o"
        booleen=False
        used_a.append(str(5))

def second_shot():
    global booleen
    if a[9]=="o" and a[1]==" ":
        a[1]=="o"
        booleen=False
        used_a.append(str(1))
    elif a[1]=="o" and a[9]==" ":
        a[9]=="o"
        booleen=False
        used_a.append(str(9))
    elif a[7]=="o" and a[3]==" ":
        a[3]=="o"
        booleen=False
        used_a.append(str(3))
    elif a[3]=="o" and a[7]==" ":
        a[7]=="o"
        booleen=False
        used_a.append(str(7))

def third_shot():
    global booleen
    if a[9]=="o"==a[1] and a[2]==a[6]==a[3]==" ":
        a[3]=="o"
        booleen=False
        used_a.append(str(3))
    elif a[1]=="o"==a[9] and a[7]==a[1]==a[8]==" ":
        a[7]=="o"
        booleen=False
        used_a.append(str(7))
    elif a[7]=="o"==a[3] and a[9]==a[8]==a[6]==" ":
        a[9]=="o"
        booleen=False
        used_a.append(str(9))
    elif "o"==a[3]==a[7] and a[1]==a[2]==a[4]==" ":
        a[1]=="o"   
        booleen=False
        used_a.append(str(1))


def deuxieme_coup():
    global booleen
    if a[1]=="o" and a[2]==a[3]==" ":
        # n_random =randint(0,1)
        # if n_random==1:
        #     a[2]="o"
        # else:
        a[3]="o"
        booleen=False
        used_a.append(str(3))
    elif a[4]=="o" and a[6]==" "==a[5]:
        # n_random =randint(0,1)
        # if n_random==1:
        #     a[5]="o"
        # else:
        a[6]="o"
        booleen=False
        used_a.append(str(6))
    elif a[7]=="o" and a[9]==" "==a[8]:
        # n_random =randint(0,1)
        # if n_random==1:
        #     a[7]="o"
        # else:
        a[9]="o"
        booleen=False
        used_a.append(str(9))
    elif a[2]=="o" and a[1]==" "==a[3]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[3]="o"
            booleen=False
            used_a.append(str(3))
        else:
            a[1]="o"
            booleen=False
            used_a.append(str(1))
    elif a[5]=="o" and a[4]==" "==a[6]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[6]="o"
            booleen=False
            used_a.append(str(6))
        else:
            a[4]="o"
            booleen=False
            used_a.append(str(4))
    elif a[8]=="o" and a[7]==" "==a[9]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
        else:
            a[7]="o"
            booleen=False
            used_a.append(str(7))
    elif a[1]=="o" and a[7]==" "==a[4]:
        # n_random =randint(0,1)
        # if n_random==1:
        #     a[4]="o"
        # else:
        a[7]="o"
        booleen=False
        used_a.append(str(7))
    elif a[4]=="o" and a[1]==" "==a[7]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[7]="o"
            booleen=False
            used_a.append(str(7))
        else:
            a[1]="o"
            booleen=False
            used_a.append(str(1))
    elif a[2]=="o" and a[8]==" "==a[5]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[5]="o"
            booleen=False
            used_a.append(str(5))
        else:
            a[8]="o"
            booleen=False
            used_a.append(str(8))
    elif a[8]=="o" and a[2]==" "==a[5]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[5]="o"
            booleen=False
            used_a.append(str(5))
        else:
            a[2]="o"
            booleen=False
            used_a.append(str(2))
    elif a[6]=="o" and a[3]==" "==a[9]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
        else:
            a[3]="o"
            booleen=False
            used_a.append(str(3))
    elif a[9]=="o" and a[6]==" "==a[3]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[3]="o"
            booleen=False
            used_a.append(str(3))
        else:
            a[6]="o"
            booleen=False
            used_a.append(str(9))
    elif a[4]=="o" and a[5]==" "==a[6] :
        n_random =random.randint(0,1)
        if n_random==1:
            a[6]="o"
            booleen=False
            used_a.append(str(6))
        else:
            a[5]="o"
            booleen=False
            used_a.append(str(5))
    elif a[7]=="o" and a[8]==" "==a[9]:
            a[9]="o"
            booleen=False
            used_a.append(str(9))

    elif a[3]=="o" and a[6]==" "==a[9]:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
       
    elif a[1]=="o" and a[9]==" "==a[5]:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
    elif a[9]=="o" and a[1]==" "==a[5]:
            a[1]="o"
            booleen=False
            used_a.append(str(1))
    elif a[7]=="o" and a[3]==" "==a[5]:
            a[3]="o"
            booleen=False
            used_a.append(str(3))
    elif a[3]=="o" and a[7]==" "==a[5]:
        # n_random =randint(0,1)
        # if n_random==1:
        #     a[5]="o"
        # else:
            a[7]="o"
            booleen=False
            used_a.append(str(7))
    elif a[3]=="o" and a[2]==" "==a[1]:
        a[1]=="o"
        booleen=False
        used_a.append(str(1))
    elif a[6]=="o" and a[4]==" "==a[5]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[5]="o"
            booleen=False
            used_a.append(str(5))
        else:
            a[4]="o"
            booleen=False
            used_a.append(str(4))
    elif a[5]=="o" and a[8]==" "==a[2]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[8]="o"
            booleen=False
            used_a.append(str(8))
        else:
            a[4]="o"
            booleen=False
            used_a.append(str(4))
    elif a[5]=="o" and a[1]==" "==a[9]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[1]="o"
            booleen=False
            used_a.append(str(1))
        else:
            a[9]="o"
            booleen=False
            used_a.append(str(9))
    elif a[5]=="o" and a[7]==" "==a[3]:
        n_random =random.randint(0,1)
        if n_random==1:
            a[7]="o"
            booleen=False
            used_a.append(str(7))
        else:
            a[3]="o"
            booleen=False
            used_a.append(str(3))

mode=int(input("entrez le nombre de joueur (1 ou 2):"))

if mode==2:
    player_name_1=input("entrez le nom du premier joueur (symbole x):")
    player_name_2=input("entrer le nom du deuxieme joueur (symbole o):")
    player_1 =player_name_1+"(x)"
    player_2 =player_name_2+"(o)"
    player_turn=player_2
    game_logic()
elif mode==1:
    
    player_name_1=input("entrez le nom du premier joueur (symbole x):")
    player_name_2="le robot"
    first_player=input("Voulez-vous jouer en premier (o ou n):")
    player_1 =player_name_1+"(x)"
    player_2 =player_name_2+"(o)"
    player_turn=player_2
    if first_player=="o":
        booleen=False
        player_turn=player_1
    else:
        booleen= True
   
    game_logic2()
