
def print_tic_tac_toe(a,b):
    print("\n")
    print ("\t     |     |")
    print (f"\t {a}   |  {b}  |  {a}")
    print('\t_____|_____|_____')
 
    print( "\t     |     |")
    print (f"\t {a}   |  {a}  |  {b}")
    print ('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print (f"\t {a}   |  {b}  |  {b}")
    print("\t     |     |")
    print("\n")

print_tic_tac_toe(input("joueur 1"),input("joueur 2"))