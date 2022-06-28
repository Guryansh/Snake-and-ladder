import random
import math

p1=int(0)
p2=int(0)
x1=int()
x2=int()

while p1!=100 or p2!=100:
    def main(x):
        
        ask=str(input('Do you wanna roll the dice{Press Enter}:-'))
        if ask=='':
            x=random.randint(1,6)
            return x
        
    def dice(c,x,name):
        print('Dice rolled by ',name,':',x)
        c=c+x    
       
        if c>100:
            c=c-x
            print('Roll Again')
        snake={'7':17,'34':54,'19':62,'60':64,'36':87,'73':92,'75':95,'79':98}
        key_snake = list(snake.keys())
        val_snake = list(snake.values())
        if c in val_snake:
            print('New position of Player ',name,': ',c,sep='')
            print('Eaten by Snake')
            pS = val_snake.index(c)
            c=int(key_snake[pS])
            

        ladder={'38':1,'14':4,'31':9,'42':21,'84':28,'67':51,'91':72,'99':80}
        key_ladder = list(ladder.keys())
        val_ladder = list(ladder.values())
        if c in val_ladder:
            print('New position of Player ',name,': ',c,sep='')
            print('Climbed up Ladder')
            pL = val_ladder.index(c)
            c=int(key_ladder[pL])

        return c
        
    x1=main(x1)
    p1=dice(p1,x1,'p1')
    print('New position of Player 1:',p1,' \n')
    
    x2=main(x2)
    p2=dice(p2,x2,'p2')
    print('New position of Player 2:',p2,' \n')
    
    if p1==100 or p2==100:
        win=[k for k, w in locals().items() if w==100][0]
        print(win,'You Won!!!')
        break
