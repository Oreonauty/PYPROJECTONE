import os
#import numpy as np

from colorit import *
# Use this to ensure that ColorIt will be usable by certain command line interfaces
# Note: This clears the terminal
init_colorit()



#####  BOARD  #######
def empty_board():
    board_length = 14
    board_heigth = 14

    board = [[' ' for _ in range(0,board_length)] for _ in range(0,board_heigth)]

    # drawing the level
    count = 0
    for row in board:
        if count == 0:
            row[0:8] = ['X'] * 8
        elif count == 10:
            row[0:4] = ['X'] * 4
        if count < 10:
            row[0] = 'X'
            count +=1 
        elif count == 13: 
            row[3:board_length] = ['X'] * (board_length-3)
            count += 1
        else:
            row[3] = 'X'
            count += 1

    count = 0
    for row in board:
        if count < 4:
            row[7] = 'X'
            count +=1 
        elif count == 4: 
            row[7:board_length] = ['X'] * (board_length-7)
            count += 1
        elif count < 14:
            row[13] = 'X'
            count += 1
            
    return board
        
        


#####  FIGURE  #######

pos_fig_head_start = [1,5]

def set_figure(pos_fig_head):
    current_board = empty_board()
    
    current_board[pos_fig_head[0]] [pos_fig_head[1]] = 'O'

    current_board[pos_fig_head[0]+1] [pos_fig_head[1]-1] = '/'
    current_board[pos_fig_head[0]+1] [pos_fig_head[1]] = '|'
    current_board[pos_fig_head[0]+1] [pos_fig_head[1]+1] = '\\'

    current_board[pos_fig_head[0]+2] [pos_fig_head[1]-1] = '/'
    current_board[pos_fig_head[0]+2] [pos_fig_head[1]] = ' '
    current_board[pos_fig_head[0]+2] [pos_fig_head[1]+1] = '\\'
    
    return current_board
    


#####  MOVE  #######

def move_fig(pos_fig_head):
    new_pos_fig_head = [pos_fig_head[0],pos_fig_head[1]]
    print('\n To move the figure press: \n \n a --> left \n d --> right \n w --> up \n s --> down \n ')
    player_move = input()
    if player_move == 'q':
        return 'q'
    if player_move == 'a':
        new_pos_fig_head[1] = pos_fig_head[1] - 3
    if player_move == 'd':
        new_pos_fig_head[1] = pos_fig_head[1] + 3
    if player_move == 'w':
        new_pos_fig_head[0] = pos_fig_head[1] - 3
    if player_move == 's':
        new_pos_fig_head[0] = pos_fig_head[1] + 3
    return new_pos_fig_head
        
    
    


def drawField(pos_fig_head = pos_fig_head_start):
    os.system('cls')
    
    field = set_figure(pos_fig_head)
    
    for row in field:
        print(*row)

       
###########################################################
##      GAMEPLAY                                         ##
###########################################################

#print(color("This text is red", Colors.red))

drawField()

playing = True
Start = True
while playing == True:
    if Start == True:
        new_pos_fig_head = move_fig(pos_fig_head_start)
        if new_pos_fig_head == 'q':
            playing = False
        else:
            drawField(new_pos_fig_head)
            Start = False
    else:
        new_pos_fig_head = move_fig(new_pos_fig_head)
        if new_pos_fig_head == 'q':
            playing = False
        else:
            drawField(new_pos_fig_head)

