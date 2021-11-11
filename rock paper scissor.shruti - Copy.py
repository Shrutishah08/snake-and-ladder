import random
#rock paper scissors 
def gameWin(comp,you):
# if two values are same /equal , decclare a tie!    
    if comp==you:
        return None
# check for all possible conditions when computer chose s.       
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
# check for all possible conditions when computer chose p.
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
# check for all possible conditions when computer chose r.            
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True    

print("Computer turn: scissor(s) paper(p) or rock(r)?")
randNo= random.randint(1,3)    # it is a function used here,in which we can chose randomly any values to insert there. and randint() is a function.
if randNo==1:
    comp='s'
elif randNo==2:
    comp= 'p'
elif randNo==3:
    comp='r'      
you=input("your turn: scissor(s) paper(p) or rock(r)")
a= gameWin(comp,you)
print(f"Computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose!")