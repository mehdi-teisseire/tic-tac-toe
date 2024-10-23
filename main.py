player_1=input("entrez le nom du premier joueur (symbole x):")
player_2=input("entrer le nom du deuxieme joueur (symbole o):")

def game_logic(): 
 b = list()  
 turn = True  
 a = list(" 123456789") 
 i = 0  
 victory = False
 player_turn=player_1

 while i < 9:
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

        if victory:  
            break
        print("tour de ",player_turn)
        player_moove = input("Entrez la case souhaitée (1-9): ")

        if player_moove not in "123456789":
            print("caractere non valide, entrez un caractere compris entre 12345679")
        else:
            k=int(player_moove)
       
        if str(k) in b:
            print("Case déjà utilisée.")
        else:
            if turn:  
                a[k] = "x"
                turn = False  
                player_turn=player_1
            else:  
                a[k] = "o"
                turn = True  
                player_turn=player_2
            b.append(str(k))  
            i += 1  

        
        if (a[1] == a[2] == a[3] != " " or  
            a[4] == a[5] == a[6] != " " or 
            a[7] == a[8] == a[9] != " " or 
            a[1] == a[4] == a[7] != " " or  
            a[2] == a[5] == a[8] != " " or  
            a[3] == a[6] == a[9] != " " or  
            a[1] == a[5] == a[9] != " " or 
            a[3] == a[5] == a[7] != " "):  
            if player_turn==player_1:
                player_turn=player_2
            else:
                player_turn=player_1 
            print("Victoire de ",player_turn," !")
            victory = True

        elif i == 9:
            print("Match nul.")
            break

def gamestart(n):
    for i in range(n):

gamestart(int(input("nombre de games")))