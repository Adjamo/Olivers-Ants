import os
import time
import random
from colorama import Fore, Back, Style

'''

    Olivers Ants. A celular automata in the vein of Conways game of life
    Dedicated to John Conway.
    Copyright (C) 2020 Adam Oliver

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

def col_(foo):
  if(foo > 19):
    return 0
  elif(foo == -1):
    return 19
  else:
    return foo

def row_(bar):
  if(bar > 79):
    return 0
  elif(bar == -1):
    return 79
  else:
    return bar

def ad_step(next):

  active = 0

  for player in dave:

    # if player direction is up
    if(player[2]==0): # animals direction (red,green,...)
      
      #no collision
      if(next[col_(player[3]-1)][row_(player[4])] != player[1] and
         next[col_(player[3]-1)][row_(player[4])] != player[0] + 10
         ): # 

        # move player
        next[col_(player[3]-1)][row_(player[4])] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[3] = col_(player[3]-1)
        active += 1
      else:
        #change direction
        player[2] = 1

    # if player direction is down
    if(player[2]==1): # animals direction

      #no collision
      if(next[col_(player[3]+1)][row_(player[4])] != player[1] and
         next[col_(player[3]+1)][row_(player[4])] != player[0] + 10
      ): # 

        next[col_(player[3]+1)][row_(player[4])] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[3] = col_(player[3]+1)
        active += 1
      else:
        #change direction
        player[2] = 3

    # if player direction is left
    if(player[2]==2): # animals direction
      
      #no collision
      if(next[col_(player[3])][row_(player[4]-1)] != player[1] and
         next[col_(player[3])][row_(player[4]-1)] != player[0] + 10
      ): # 

        next[col_(player[3])][row_(player[4]-1)] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[4] = row_(player[4]-1)
        active += 1
      else:
        #change direction
        player[2] = 0

    # if player direction is right
    if(player[2]==3): # animals direction

      #no collision
      if(next[col_(player[3])][row_(player[4]+1)] != player[1] and
         next[col_(player[3])][row_(player[4]+1)] != player[0] + 10
      ): # 

        next[col_(player[3])][row_(player[4]+1)] = player[0]
        next[col_(player[3])][row_(player[4])] = player[0]+10 # make an 'X'
        player[4] = row_(player[4]+1)
        active += 1
      else:
        #change direction
        player[2] = 2


  return next, active


def print_grid(grid):

  #os.system('cls' if os.name == 'nt' else 'clear')

  for row in grid:
    for e in row:
            
      if(e==1):print(Fore.LIGHTGREEN_EX + '1', end='') # end='' removes newline
      if(e==2):print(Fore.LIGHTBLACK_EX + '2', end='') # 
      if(e==3):print(Fore.BLACK + '3', end='') # 
      if(e==4):print(Fore.GREEN + '4', end='') # 
            
      if(e==11):print(Fore.LIGHTGREEN_EX + '%', end='') # 
      if(e==12):print(Fore.LIGHTBLACK_EX + '#', end='') # 
      if(e==13):print(Fore.BLACK + '@', end='') # 
      if(e==14):print(Fore.GREEN + '&', end='') # 

      if(e==5):print(Fore.RED + '5', end='') # 
      if(e==6):print(Fore.CYAN + '6', end='') # 

      if(e==15):print(Fore.RED + '*', end='') # 
      if(e==16):print(Fore.CYAN + '!', end='') # 

      if(e==0):print(' ', end='') # end='' removes newline
            
    print()
    
def game(grid):

  steps = 0
  old = []

  while True:

    global dave

    new_grid, active = ad_step(grid)
    
    print()
    print()
    print_grid(new_grid)
    print(Fore.WHITE + 'Generation: ' + str(steps) )
    print(Fore.WHITE + 'Active Pieces: ' + str(active) )
    steps += 1
    time.sleep(0.1)


# initialaise variables
global dave
# what dave looks like
# dave = [1/2/3/4,@/#/%/&,direction,x coord,y coord]
# e.g. dave = [[1,14,0,1,1],[2,11,1,2,2],[3,12,2,3,3],[4,13,3,4,4]]
dave = []
# start with a random map
  
grid = [[0 for i in range(80)] for j in range(20)]

# range of 15 ends quickly
# range of 20 ends 4,000 to 27,000 generations
# range of 25 ends 80,000 generations
# range of 30 500,000 + no end

for var_name in range(25):# change this number for fun!
  for me in range(4):# number of colours

    ran_x = random.randint(0, 19)
    ran_y = random.randint(0, 79)

    grid[ran_x][ran_y] = me+1
    
    if(me == 0):# 1 cant beat 2
      dave.append( [me+1,12,me,ran_x,ran_y] )
    if(me == 1):# 2 cant beat 3
      dave.append( [me+1,13,me,ran_x,ran_y] )
    if(me == 2):# 3 cant beat 4
      dave.append( [me+1,14,me,ran_x,ran_y] )
    if(me == 3):# 4 cant beat 1
      dave.append( [me+1,11,me,ran_x,ran_y] ) # add more if you want more colours (req coding!)

new_number = game(grid)

if(new_number > number): # keep the record
  number = new_number



