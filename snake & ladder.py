import random
import math

position=int(0)
while position!=100:
    
    x=random.randint(1,6)
    print('Number on dice:',x)
    position=position+x

    def snake():
        global position
        if position==17:
            print('New position:',position)
            position=7
            print('Eaten by Snake')
        elif position==54:
            print('New position:',position)
            position=34
            print('Eaten by Snake')
        elif position==62:
            print('New position:',position)
            position=19
            print('Eaten by Snake')
        elif position==64:
            print('New position:',position)
            position=60
            print('Eaten by Snake')
        elif position==87:
            print('New position:',position)
            position=36
            print('Eaten by Snake')
        elif position==92:
            print('New position:',position)
            position=73
            print('Eaten by Snake')
        elif position==95:
            print('New position:',position)
            position=75
            print('Eaten by Snake')
        elif position==98:
            print('New position:',position)
            position=79
            print('Eaten by Snake')
    snake()

    def ladder():
        global position
        if position==1:
            print('New position:',position)
            position=38
            print('Used ladder')
        elif position==4:
            print('New position:',position)
            position=14
            print('Used ladder')
        elif position==9:
            print('New position:',position)
            position=31
            print('Used ladder')
        elif position==21:
            print('New position:',position)
            position=42
            print('Used ladder')
        elif position==28:
            print('New position:',position)
            position=84
            print('Used ladder')
        elif position==51:
            print('New position:',position)
            position=67
            print('Used ladder')
        elif position==72:
            print('New position:',position)
            position=91
            print('Used ladder')
        elif position==80:
            print('New position:',position)
            position=99
            print('Used ladder')
    ladder()
            
    if position==100:
        print('New position:',position)
        print('You Won!!!')
        break
    elif position>=100:
        position=position-x
        print('Roll Again')

    print('New position:',position)
