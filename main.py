def print_tic_tac_toe(a):
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

print_tic_tac_toe(input("joueur 1"),input("joueur 2"))