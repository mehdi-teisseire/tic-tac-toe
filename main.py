b=list()
tour=True
a=list("         ")
i=0
vic=False
while i<9:
    print("\n")
    print ("\t     |     |")
    print (f"\t {a[0]}   |  {a[1]}  |  {a[2]}")
    print('\t_____|_____|_____')
    print( "\t     |     |")
    print (f"\t {a[3]}   |  {a[4]}  |  {a[5]}")
    print ('\t_____|_____|_____')
    print("\t     |     |")
    print (f"\t {a[6]}   |  {a[7]}  |  {a[8]}")
    print("\t     |     |")
    print("\n")
    c=list(" ")
    k=int(input("entrez la case souhaitée:"))
    if vic==True:
        break
    if list(str(k)) in b:
        print("deja utilisé")
    else:
        if tour==True :
            a[k]="x"
            tour=False
            c[0]=list(str(k))
            b+=c
            i+=1
        else:
            a[k]="o"
            tour=True
            c[0]=list(str(k))
            b+=c
            i+=1
    if a[0]==a[4]==a[8]!=" " or a[2]==a[4]==a[6]!=" " or a[0]==a[1]==a[2]!=" " or a[3]==a[4]==a[5]!=" " or a[6]==a[7]==a[8]!=" " or a[0]==a[3]==a[6]!=" " or a[1]==a[4]==a[7]!=" " or a[2]==a[5]==a[8]!=" ":
         print("victoire")
         vic=True
    elif i==9:
        print("fin de partie")
        break