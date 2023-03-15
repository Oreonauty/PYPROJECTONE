import os
import numpy as np


arr_field = np.chararray((15,20))

arr_field[:,:] = ''
arr_field[0,:] = '++'
arr_field[14,:] = '_+'


def drawField(field):
    os.system('cls')
    
    for row in field:
        temp = ''
        for val in row:
            temp += str(val)
        print (temp)

       
    
drawField(arr_field)
#print(arr_field)
