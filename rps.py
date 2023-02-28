import random
import time
from colorama import Fore, Back, Style, init

width = 10
team_size = 5

playfield = [[' ' for i in range(width)] for x in range(width)]
players = []

def display(playfield):

    [stdout.write('|'.join([str(item) for item in row])+'\n') for row in playfield]
    
init()
from sys import stdout


'''

0 - Rock
1 - Paper
2 - Scissors

'''

class Obj:

    def __init__(self, grp):
        self.grp = grp
        self.pos = [-1, -1]

    def swap(self, new):
        self.grp = new

    def set_pos(self, x, y):
        self.pos = [x, y]

    def move_pos(self, xdir, ydir):
        self.pos = [xdir + self.pos[0], ydir + self.pos[1]]

    def get_new_pos(self, xdir, ydir):
        return [xdir + self.pos[0], ydir + self.pos[1]]
    
    def __str__(self):
        
        tmp = ''
        if self.grp == 0:
            tmp = Back.GREEN+'R'
        elif self.grp == 1:
            tmp =  Back.RED+'P'
        elif self.grp == 2:
            tmp = Back.BLUE+'S'
        return tmp+Style.RESET_ALL
def challenge(a, b):
    
    if a.grp == b.grp:
        return -1
    elif a.grp == 0:
        tup = (2,0,1)
    elif a.grp == 1:
        tup = (0,1,2)
    elif a.grp == 2:
        tup = (1,2,0)

    if tup.index(a.grp) > tup.index(b.grp):
        b.swap(a.grp)
        return 1
    else:
        a.swap(b.grp)
        return 0

def shuffle(a, playfield):

    x_direction = random.randint(-1,1)
    y_direction = random.randint(-1,1)
    
    x_old, y_old = a.pos
    x, y = a.get_new_pos(x_direction, y_direction)

    while x > len(playfield)-1 or x < 0 or y > len(playfield)-1 or y < 0:
        x_direction = random.randint(-1,1)
        y_direction = random.randint(-1,1)
        
        x, y = a.get_new_pos(x_direction, y_direction)
    try:
        if type(a) == type(playfield[x][y]):
            
            challenge(a, playfield[x][y])

        else:

            a.move_pos(x_direction, y_direction)
            update(playfield, a, 1, [x_old,y_old])
    except:
        print(x,y)
        print(playfield[x])

def update(playfield, a, existing=0, old=[]):
    
    x, y = a.pos
    playfield[x][y] = a

    if existing:
        playfield[old[0]][old[1]] = ' '

def main():
    
    # Display stats

    global team_size, width

    print('Field width:', width)
    print('Team size:', team_size)
    print('0 - Rock\n1 - Paper\n2 - Scissors\n')

    print('Game starting...\n')

    display(playfield)

    print('\n')

    # Setup groups

    for grp in range(3):
        for i in range(team_size):
            players.append(Obj(grp))

    # Assign positions without duplicates

    blacklist = []

    for i, player in enumerate(players):

        x_pos = random.randint(0, width-1)
        y_pos = random.randint(0, width-1)

        while (x_pos, y_pos) in blacklist:

            x_pos = random.randint(0, width-1)
            y_pos = random.randint(0, width-1)

        blacklist.append((x_pos, y_pos))

        players[i].set_pos(x_pos, y_pos)
        update(playfield, players[i])

    display(playfield)

    input('Enter to proceed...')
    print('Game starts in...')
    for i in range(3):
        print(3-i)
        time.sleep(1)
    print('GO!')

    while True:
        
        random.shuffle(players)
        for i, player in enumerate(players):

            shuffle(players[i], playfield)

        display(playfield)

        

        tmp = []
        [[tmp.append(str(item)) for item in row] for row in playfield]

        stats = [0,0,0]
        for item in tmp:
            if 'R' in item:
                stats[0] += 1
            elif 'P' in item:
                stats[1] += 1
            elif 'S' in item:
                stats[2] += 1
        print('Rock:', stats[0])
        print('Paper:', stats[1])
        print('Scissors:', stats[2])

        finished = False
        counter = 0
        winner = 0
        for i,v in enumerate(stats):
            if v == 0:
                counter += 1
            else:
                winner = i
        if counter >= 2:
            names = ['Rock', 'Paper', 'Scissors']
            print('{} wins!'.format(names[winner]))
            return
        time.sleep(1)

if __name__ == '__main__':
    main()