import random as rr
computer=rr.choice([-1,0,1])
you=input("choose snake\twater\tgun\n")
dict1={"snake":-1,"water":0,"gun":1}
dict2={-1:"snake",0:"water",1:"gun"}
print(f"you choose{dict2(you)}\ncomputer choose{dict2(computer)}")
if(computer==you):
    print("its draw!")
else:
    if(computer==-1 and you==0):
        print("you losse!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==1 and you==-1):
        print("you loose!")
    elif(computer==0 and you==1):
        print("you loose!")
    elif(computer==0 and you==-1):
        print("you win!") 
    else:
        print("invalid input")                       
