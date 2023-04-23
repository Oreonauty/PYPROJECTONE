import os
#import numpy as np

#####  BOARD  #######

board_length = 25
board_heigth = 20

board = [[' ' for _ in range(board_length)] for _ in range(board_heigth)]

board[0] = ['X' for _ in range(board_length)]
board[board_heigth - 1] = ['X' for _ in range(board_length)]
for row in board:
    row[0] = 'X'
    row[board_length - 1] = 'X'


#####  FIGURE  #######

pos_fig_head_start = [5,5]

def set_figure(pos_fig_head):
    
    board[pos_fig_head[0]] [pos_fig_head[1]] = 'O'

    board[pos_fig_head[0]+1] [pos_fig_head[1]-1] = '/'
    board[pos_fig_head[0]+1] [pos_fig_head[1]] = '|'
    board[pos_fig_head[0]+1] [pos_fig_head[1]+1] = '\\'

    board[pos_fig_head[0]+2] [pos_fig_head[1]-1] = '/'
    board[pos_fig_head[0]+2] [pos_fig_head[1]] = ' '
    board[pos_fig_head[0]+2] [pos_fig_head[1]+1] = '\\'
    
def erase_figure(pos_fig_head):
    
    board[pos_fig_head[0]] [pos_fig_head[1]] = ' '

    board[pos_fig_head[0]+1] [pos_fig_head[1]-1] = ' '
    board[pos_fig_head[0]+1] [pos_fig_head[1]] = ' '
    board[pos_fig_head[0]+1] [pos_fig_head[1]+1] = ' '

    board[pos_fig_head[0]+2] [pos_fig_head[1]-1] = ' '
    board[pos_fig_head[0]+2] [pos_fig_head[1]] = ' '
    board[pos_fig_head[0]+2] [pos_fig_head[1]+1] = ' '    

#####  MOVE  #######

def move_fig(pos_fig_head):
    new_pos_fig_head = [pos_fig_head[0],pos_fig_head[1]]
    print('\n To move the figure press: \n \n a --> left \n d --> right \n w --> up \n s --> down \n ')
    player_move = input()
    if player_move == 'q':
        return 'q'
    if player_move == 'a':
        new_pos_fig_head[1] = pos_fig_head[1] - 1
    if player_move == 'd':
        new_pos_fig_head[1] = pos_fig_head[1] + 1
    if player_move == 'w':
        new_pos_fig_head[0] = pos_fig_head[1] - 1
    if player_move == 's':
        new_pos_fig_head[0] = pos_fig_head[1] + 1
    return new_pos_fig_head
        
    
    


def drawField(field, pos_fig_head, new_pos_fig_head):
    os.system('cls')
    erase_figure(pos_fig_head)
    set_figure(new_pos_fig_head)
    
    for row in field:
        print(*row)

       
###########################################################
##      GAMEPLAY                                         ##
###########################################################
pos_fig_head = pos_fig_head_start    
drawField(board, pos_fig_head = pos_fig_head_start, new_pos_fig_head = pos_fig_head_start)
playing = True
while playing == True:
    new_pos_fig_head = move_fig(pos_fig_head_start)
    if new_pos_fig_head == 'q':
        playing = False
    else:
        drawField(board, pos_fig_head, new_pos_fig_head)

