# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:23:56 2022

Author: Andrew C. Willis 
Class: CS 463G, Assignment 1
"""
import numpy as np
import pandas as pd

class special_gears:
    def __init__(self):
        #should have attribute for:
        #ID: unique 
        #Colors: 2 colors
        #Location: 2 sides 
        #Angle: starts at zero, perpindicular movements will increment or decrement by 60 degrees
        '''
        
        two cases:
            - when it rotation is parrelel to its current position, one neighbor changes and the other stays fixed
            - when it rotattion is perpindicular to its current position, neigbhors do not change and gear rotates +/- 120
        
        thus with command of ('side', cw/ccw), all gears pointed to by that side should shuffle neigbhor one in cw or ccw direction
        
            
        special_gears =  
        
				['_' 'RG' '_']
				['RY' 'R*' 'RO']
				['_' 'RB' '_']


['_' 'RY' '_']     ['_' 'RB' '_']	['_' 'RO' '_']	     ['_' 'RG' '_']
['GY' 'Y*' 'YB']   ['YB' 'B*' 'BO']	['BO' 'O*' 'OG']	['OG' 'G*' 'GY']
['_' 'YV' '_']	   ['_' 'BV' '_']	['_' 'OV' '_']	    ['_' 'GV' '_']


				['_' 'BV' '_']
				['YV' 'V*' 'OV']
				['_' 'GV' '_']
                
        I observed that the special gear pieces move always with the peices directly up or down from them. THus they are 
        represented in the same string in the same np.array cell
        
        
        '''
        #There are 12 of these gears in total
        #One perpendicular rotation should move 4 of these gears, +/- 120? degrees (depending on up or down rotation)
        #In such a rotation the other 4 are idle
        #
        pass
class side: 
    def __init__(self, color, start_state): 
        self.color = color
        self.gear_colors = np.array(start_state)
        self.North_Neighbor = None
        self.East_Neighbor = None
        self.South_Neighbor = None
        self.West_Neighbor = None
        self.Opp_Side = None
        #there are six total sides
        #each side will have 3 vertical neighbors, and 3 hortizontal neighbors
        #Thus, should have attribute for:
            
        #Color: unique identifier (Red, Green, Blue, Orange, Yellow, Violet) (derived from fixed *center* square)
        #North_Neighbor: 1 pointers to class side
        #East_Neighbor: 1 pointers to class side
        #South_Neighbor: 1 pointers to class side
        #West_Neighbor: 1 pointers to class side
            #is this an issue because N,S,E,W depends on how the cube is oriented?
            #Can i assume a true, fixed orientation of cube (up is same for all sides)
            
        #Side_colors (state): 2D list (3x3) that shows the state of the gear colors in their position
            #Such as this: 
        '''
                side_colors = [
                    
                          [['R','R','R'],
                           ['R','R*','R'],
                           ['R','R','R']],
                          
                          [['G','G','G'],
                           ['G','G*','G'],
                           ['G','G','G']],
                          
                          [['B','B','B'],
                           ['B','B*','B'],
                           ['B','B','B']],
                          
                          [['O','O','O'],
                           ['O','O*','O'],
                           ['O','O','O']],
                          
                          [['Y','Y','Y'],
                           ['Y','Y*','Y'],
                           ['Y','Y','Y']],
                          
                          [['V','V','V'],
                           ['V','V*','V'],
                           ['V','V','V']]
                    ]
                
                BUT will only have ONE SINGLE 3x3 list of chars (colors)
        '''
                #This Representation INCLUDES the *central*, fixed gear/square 
                #BUT, this representation EXCLUDES the cardinal, bichromatic gears which are more complicated
                
              
        
        #Special Gears: These are shared between neigbhoring sides (direct neigbhors), so they should point to the same 
            #Special Gear object
            # each side has one special gear at the N,S,E,W position and is shared with that neighbor (N,S,E,W)
    def print_Side_State(self):
        for i in self.gear_colors:
            print(f"{str(i): >50}") 
            
            
                
class gearball:
    def __init__(self):
        # Should have attributes for:
        # Sides: 1D list of class sides of length 6
        # Methods for:
            #movements
            #randomization
        '''
				['_' 'RG' '_']
				['RY' 'R*' 'RO']
				['_' 'RB' '_']


['_' 'RY' '_']     ['_' 'RB' '_']	['_' 'RO' '_']	     ['_' 'RG' '_']
['GY' 'Y*' 'YB']   ['YB' 'B*' 'BO']	['BO' 'O*' 'OG']	['OG' 'G*' 'GY']
['_' 'YV' '_']	   ['_' 'BV' '_']	['_' 'OV' '_']	    ['_' 'GV' '_']


				['_' 'BV' '_']
				['YV' 'V*' 'OV']
				['_' 'GV' '_']
        
        
        '''
        self.solved = True
        self.G_side = side('Green', 
        np.array([['G','G+(R_G)','G'],
         ['G+(O_G)','G*','G+(G_Y)'],
         ['G','G+(G_V)','G']]))
        self.R_side = side('Red', 
                  np.array([['R','R+(R_G)','R'],
                   ['R+(R_Y)','R*','R+(R_O)'],
                   ['R','R+(R_B)','R']]))
        self.B_side = side('Blue', 
                  np.array([['B','B+(R_B)','B'],
                   ['B+(Y_B)','B*','B+(B_O)'],
                   ['B','B+(B_V)','B']]))
        self.O_side = side('Orange', 
                  np.array([['O','O+(R_O)','O'],
                   ['O+(B_O)','O*','O+(O_G)'],
                   ['O','O+(O_V)','O']]))
        self.Y_side = side('Yellow', 
                  np.array([['Y','Y+(R_Y)','Y'],
                   ['Y+(G_Y)','Y*','Y+(Y_B)'],
                   ['Y','Y+(Y_V)','Y']]))
        self.V_side = side('Violet', 
                  np.array([['V','V+(B_V)','V'],
                   ['V+(Y_V)','V*','V+(O_V)'],
                   ['V','V+(G_V)','V']]))
        self.all_sides = np.array([self.G_side,self.R_side,self.B_side,self.O_side,self.Y_side,self.V_side])
        #Next, store pointers to these sides to define adjacency mapping to touching rows, or columns
        #Blue:
        self.B_side.North_Neighbor = self.R_side.gear_colors[2]
        self.B_side.South_Neighbor = self.V_side.gear_colors[0]
        self.B_side.East_Neighbor = self.O_side.gear_colors[:,0]
        self.B_side.West_Neighbor = self.Y_side.gear_colors[:,2]
        self.B_side.Opp_Side = self.G_side
        #Orange:
        self.O_side.North_Neighbor = self.R_side.gear_colors[:,2]
        self.O_side.South_Neighbor = self.V_side.gear_colors[:,2]
        self.O_side.East_Neighbor = self.G_side.gear_colors[:,0]
        self.O_side.West_Neighbor = self.B_side.gear_colors[:,2]
        self.O_side.Opp_Side = self.Y_side
        #Yellow:
        self.Y_side.North_Neighbor = self.R_side.gear_colors[:,0]
        self.Y_side.South_Neighbor = self.V_side.gear_colors[:,0]
        self.Y_side.East_Neighbor = self.B_side.gear_colors[:,0]
        self.Y_side.West_Neighbor = self.G_side.gear_colors[:,2]
        self.Y_side.Opp_Side = self.O_side
        #Green:
        self.G_side.North_Neighbor = self.R_side.gear_colors[0]
        self.G_side.South_Neighbor = self.V_side.gear_colors[2]
        self.G_side.East_Neighbor = self.Y_side.gear_colors[:,0]
        self.G_side.West_Neighbor = self.O_side.gear_colors[:,2]
        self.G_side.Opp_Side = self.B_side
        #Red:
        self.R_side.North_Neighbor = self.G_side.gear_colors[0]
        self.R_side.South_Neighbor = self.B_side.gear_colors[0]
        self.R_side.East_Neighbor = self.O_side.gear_colors[0]
        self.R_side.West_Neighbor = self.Y_side.gear_colors[0]
        self.R_side.Opp_Side = self.V_side
        #Violet:
        self.V_side.North_Neighbor = self.B_side.gear_colors[2]
        self.V_side.South_Neighbor = self.G_side.gear_colors[2]
        self.V_side.East_Neighbor = self.O_side.gear_colors[2]
        self.V_side.West_Neighbor = self.Y_side.gear_colors[2]
        self.V_side.Opp_Side = self.R_side
        

        
    def copy(self, to, fro):
        for i, cell in enumerate(fro):
            to[i] = cell
           
    def ccw(self, side):
       #make this just call clock wise 3 times
       pass

    
    def cw(self, side):
        #side should be a pointer to the side determined in the toggle function
        
        '''
        Here call a method that will rotate the actual side (first row> last column; last column > bottom row; 
                                                             bottom row> first column; simulateanously)
        
        '''
        #FIRST, rotate the side which rotation is wrt
        #side.gear_colors = np.rot90(side.gear_colors, 3)#great but can not use because it screws with the pointers

        temp1 = side.gear_colors[:,0].copy()#save original contents 
        temp2 = side.gear_colors[0].copy()
        temp3 = side.gear_colors[:,2].copy()
        temp4 = side.gear_colors[2].copy()
        
        self.copy(side.gear_colors[:,2], temp2)#first row> last column
        self.copy(side.gear_colors[2], temp3[::-1])#last column > last row
        self.copy(side.gear_colors[:,0], temp4)#last row > first column
        self.copy(side.gear_colors[0], temp1[::-1])#first coulmn > first row
        
        #LAST, rotate the adjacent, connected rows and columns of neighboring sides
        
        temp1 = side.East_Neighbor.copy()#save original contents 
        temp2 = side.South_Neighbor.copy()
        temp3 = side.West_Neighbor.copy()
        temp4 = side.North_Neighbor.copy()
        
        #as an artifact of my layout, which assumes blue to be the center, some rows, columns must be inverted first:
        if side.color == 'Blue':
            temp1 = temp1[::-1]
            temp3 = temp3[::-1]
        if side.color == 'Yellow':
            temp2 = temp2[::-1]
            temp3 = temp3[::-1]
        if side.color == 'Orange':
            temp1 = temp1[::-1]
            temp4 = temp4[::-1]
        if side.color == 'Green':
            temp4 = temp4[::-1]
            temp2 = temp2[::-1]
        
        self.copy(side.East_Neighbor, temp4)
        self.copy(side.South_Neighbor, temp1)
        self.copy(side.West_Neighbor, temp2)
        self.copy(side.North_Neighbor, temp3)
        
        '''
        temp1 = side.East_Neighbor.copy()
        #print(temp1)
        self.copy(side.East_Neighbor, side.North_Neighbor)
        
        temp2 = side.South_Neighbor.copy()
        #print(temp2)
        self.copy(side.South_Neighbor, temp1)
        
        temp1 = side.West_Neighbor.copy()
        #print(temp1)
        self.copy(side.West_Neighbor, temp2)
        
        self.copy(side.North_Neighbor, temp1)
        '''
        
        
    
    def toggle(self, side, direction):
        #side is one of the 6 sides
        #twisting the (Red, Green, Blue, Orange, Yellow, or Violet) side has the effect of moving the (rightmost?) column 
        # of the West-> ITS own northern neighbor, NOrth-> ITS own eastern neigbhor, 
        # East-> ITS southern neighbor, South-> ITS own western neighbor
        # then rotate the correct special gears +/- 60 degrees (clockwise vs counterclockwise)
        '''
        
            MUST ROTATE THE OPPOSITE SIDE THE SAME DIRECTION (CLOCKWISE) NEXT
            hopefully is just a call to side.opposite (should add that parameter)
            so call cw or ccw on (side) then on (side.opposite)
        '''
        pass
    
    
    def print_Puzzle_State(self):

        self.R_side.print_Side_State()
        print('\n')

        for i in range(0,3):
            print(f"{str(self.Y_side.gear_colors[i]): <30}{str(self.B_side.gear_colors[i]): <30}{str(self.O_side.gear_colors[i]): <30}{str(self.G_side.gear_colors[i]): <30}")
        print('\n')
        self.V_side.print_Side_State()
        print('\n\n')
        
        
    def scramble(self, number_moves):
        print('Start State of Gear Ball:\n')
        self.print_Puzzle_State()
        for i in range(0, number_moves):
            which_side = np.random.randint(6)#pick a random side to rotate wrt
            which_dir = np.random.randint(2)#pick random direction (2 choices: cw, or ccw)
            if which_dir == 0: #same as 3 clockwise rotations
                '''
                    change to make it call ccw function, and it will just call cw 3 times, this is ugly
                '''
                self.cw(self.all_sides[which_side])
                self.cw(self.all_sides[which_side].Opp_Side)
                
                self.cw(self.all_sides[which_side])
                self.cw(self.all_sides[which_side].Opp_Side)
                
                self.cw(self.all_sides[which_side])
                self.cw(self.all_sides[which_side].Opp_Side)
                
                print('AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CCW :')
                self.print_Puzzle_State()
            else:
                self.cw(self.all_sides[which_side])
                self.cw(self.all_sides[which_side].Opp_Side)
                print('AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CW :')
                self.print_Puzzle_State()

def main():# I think she wants this to be its own script
    #initialize the gear ball
    puzzle = gearball()
    invalid = True
    
    while invalid:
        inp = input('Please Select One of the Following Operations to Perform:\n'+
                '1. Scramble the Gear Ball  by N- rotations (Respond 1) \n'+
                '2. Provide the Side to Move(Red, Yellow, Blue, Orange, Green, or Violet), & the Direction (CW, or CCW) (Respond 2)\n')
    
        if inp == '1':
            print('You Want to Scramble.')
            num_moves = input('Please Provide an (Integer) Number of Moves to Scramble the Gear Ball:\n')
            puzzle.scramble(int(num_moves)) 
            invalid = False
        elif inp == '2':
            print('You Want to Move a Side')
            
            invalid = False
        else:
            print('PLEASE SELECT A VALID OPTION!!! (1 or 2)')
    
    
 
    
    '''
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.Y_side)
    puzzle.cw(puzzle.Y_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.Y_side)
    puzzle.cw(puzzle.Y_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.Y_side)
    puzzle.cw(puzzle.Y_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.print_Puzzle_State()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.print_Puzzle_State()    '''
    

    
  

if __name__ == "__main__":
    main()
