import random as ra
l=ra.randrange(1,100)
a=0
z=1
while a!=l:
    a=int(input("enter a guess between 1 and 100:"))  
    if a>l:
        print("lower")
    elif a<l:
        print("upper")
    elif a==l:
        print("bingo!",l,"was correct. you guessed after ",z,"tries")
    z=z+1
while 1:
    2+3