player_name_1=input("entrez le nom du premier joueur (symbole x):")
player_name_2=input("entrer le nom du deuxieme joueur (symbole o):")
player_1 =player_name_1+"(x)"
player_2 =player_name_2+"(o)"
a = list("          ")
score_1 = 0
score_2 = 0 

def win_condition(player_turn, i):       
    if (a[1] == a[2] == a[3] != " " or  
        a[4] == a[5] == a[6] != " " or 
        a[7] == a[8] == a[9] != " " or 
        a[1] == a[4] == a[7] != " " or  
        a[2] == a[5] == a[8] != " " or  
        a[3] == a[6] == a[9] != " " or  
        a[1] == a[5] == a[9] != " " or 
        a[3] == a[5] == a[7] != " "): 
        print(f"{player_turn} a gagné !") 
        return True
        

    if i == 9:
        print("Match nul.")
        return True
    
    return False


            


    

def game_logic(): 
 b = list()  
 turn = True  
 i = 0  
 victory = False
 player_turn=player_1

 while i <= 9:
        print("\n")
        print("\t     |     |")
        print(f"\t {a[7]}   |  {a[8]}  |  {a[9]}                7 | 8 | 9") 
        print('\t_____|_____|_____              --|---|---')
        print("\t     |     |                   4 | 5 | 6")
        print(f"\t {a[4]}   |  {a[5]}  |  {a[6]}                --|---|---")  
        print('\t_____|_____|_____              1 | 2 | 3')
        print("\t     |     |")
        print(f"\t {a[1]}   |  {a[2]}  |  {a[3]}") 
        print("\t     |     |")
        print("\n")

       
        print("tour de",player_turn)
        player_moove = input("Entrez la case souhaitée (1-9): ")

        if player_moove not in "1,2,3,4,5,6,7,8,9" or not player_moove:
            print("caractere non valide, entrez un caractere compris entre 12345679")
        else:
            k=int(player_moove)
       
            if str(k) in b:
                print("Case déjà utilisée.")
            else:
                if turn:  
                    a[k] = "X"
                    turn = False  
                    player_turn=player_1
                else:  
                    a[k] = "O"
                    turn = True  
                    player_turn=player_2
                b.append(str(k))  
                i += 1 
                victory = win_condition(player_turn,i)
                if victory:
                    print("\n")
                    print("\t     |     |")
                    print(f"\t {a[7]}   |  {a[8]}  |  {a[9]}") 
                    print('\t_____|_____|_____')
                    print("\t     |     |")
                    print(f"\t {a[4]}   |  {a[5]}  |  {a[6]}")  
                    print('\t_____|_____|_____')
                    print("\t     |     |")
                    print(f"\t {a[1]}   |  {a[2]}  |  {a[3]}") 
                    print("\t     |     |")
                    print("\n")
                    break
game_logic()

