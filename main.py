def game_logic(): 
    b = list()  
    tour = True  
    a = list(" 123456789") 
    i = 0  
    vic = False
    jou1=input("entrez le nom du premier joueur (symbole x):")
    jou2=input("entrer le nom du deuxieme joueur (symbole o):")
    m=jou1
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

        if vic:  
            break
        print("tour de ",m)
        h = input("Entrez la case souhaitée (1-9): ")

        if h not in "123456789":
            print("caractere non valide, entrez un caractere compris entre 12345679")
        else:
            k=int(h)
       
        if str(k) in b:
            print("Case déjà utilisée.")
        else:
            if tour:  
                a[k] = "x"
                tour = False  
                m=jou2
            else:  
                a[k] = "o"
                tour = True  
                m=jou1
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
            if m==jou1:
                m=jou2
            else:
                m=jou1 
            print("Victoire de ",m," !")
            vic = True

        elif i == 9:
            print("Match nul.")
            break

game_logic()

