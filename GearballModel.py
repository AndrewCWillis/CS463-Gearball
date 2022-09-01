# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:23:56 2022
Last Updated on Sunday Aug 22 10:02:00 2022
Author: Andrew C. Willis 
Contributor: Anthony Wirts
Class: CS 463G, Assignment 1
"""
import numpy as np
from numpy.lib.nanfunctions import nancumprod
import pandas as pd


class side: 
    def __init__(self, color, start_colors, start_orientations): 
        self.color = color
        self.gear_colors = np.array(start_colors)
        self.gear_orientations = np.array(start_orientations)

        self.North_Neighbor = None#now points to the other sides
        self.East_Neighbor = None
        self.South_Neighbor = None
        self.West_Neighbor = None
        self.Opp_Side = None

        self.North_Colors = None#points to the row of colors adjacent to the current side
        self.East_Colors = None
        self.South_Colors = None
        self.West_Colors = None

        self.North_Orientations = None#points to the orientations of the gears of neighboring sides
        self.East_Orientations = None
        self.South_Orientations = None
        self.West_Orientations = None

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
                
                #This Representation INCLUDES the *central*, fixed gear/square 
                #BUT, this representation EXCLUDES the cardinal, bichromatic gears which are more complicated

                #side orientations = [[0,x,0],
                                     [x,0,x],
                                     [0,x,0]]

                The x's indicate the orientation of the gears where x equals some multiple of 60 degrees rotation in relation to the two adjacent colors it's attached to
                The 0's don't change and are simply placeholders for displaying a square array
         ''' 
        
        #Special Gears: These are shared between neigbhoring sides (direct neigbhors), so they should point to the same 
            #Special Gear object
            # each side has one special gear at the N,S,E,W position and is shared with that neighbor (N,S,E,W)
    def print_Side_Colors(self):
        for i in self.gear_colors:
            print(f"{str(i): >50}") 

    def print_Side_Orientations(self):
        for i in self.gear_orientations:
            print(f"{str(i): >37}") 
            
            
                
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
        self.special_gear = [0,0,0,0,0,0,0,0,0,0] #log the angle they are at. after certian side moves, 
        #4 gears will increment or decrement angle by 120 degrees
        
        '''
        [B_R, B_O, B_V, B_Y, R_G, R_O, R_Y, G_Y, Y_V, O_G, O_V, G_V] are the gears
        HAVE NOT FINISHED THE GEARS YET! There postion is fixed to the piece beside and below them, and that is how
        they are displayed textually. The last step is to track their angle.
        
        They will increment or decrement by 120 degrees. There are 4 gears on each hemisphere of the cube, if you slice 
        into thirds.
        '''
        self.G_side = side('Green', 
        np.array([['G','G+(R_G)','G'],
         ['G+(O_G)','G*','G+(G_Y)'],
         ['G','G+(G_V)','G']]),
        np.zeros((3,3), dtype=int))
        self.R_side = side('Red', 
                  np.array([['R','R+(R_G)','R'],
                   ['R+(R_Y)','R*','R+(R_O)'],
                   ['R','R+(R_B)','R']]),
                   np.zeros((3,3), dtype=int))
        self.B_side = side('Blue', 
                  np.array([['B','B+(R_B)','B'],
                   ['B+(Y_B)','B*','B+(B_O)'],
                   ['B','B+(B_V)','B']]),
                    np.zeros((3,3), dtype=int))
        self.O_side = side('Orange', 
                  np.array([['O','O+(R_O)','O'],
                   ['O+(B_O)','O*','O+(O_G)'],
                   ['O','O+(O_V)','O']]),
                    np.zeros((3,3), dtype=int))
        self.Y_side = side('Yellow', 
                  np.array([['Y','Y+(R_Y)','Y'],
                   ['Y+(G_Y)','Y*','Y+(Y_B)'],
                   ['Y','Y+(Y_V)','Y']]),
                    np.zeros((3,3), dtype=int))
        self.V_side = side('Violet', 
                  np.array([['V','V+(B_V)','V'],
                   ['V+(Y_V)','V*','V+(O_V)'],
                   ['V','V+(G_V)','V']]),
                    np.zeros((3,3), dtype=int))
        self.all_sides = np.array([self.R_side,self.B_side,self.Y_side])
        
        #Next, store pointers to these sides to define adjacency mapping to touching rows, or columns of the np.arrays
        #Blue:
        self.B_side.North_Colors = self.R_side.gear_colors[2]
        self.B_side.South_Colors = self.V_side.gear_colors[0]
        self.B_side.East_Colors = self.O_side.gear_colors[:,0]
        self.B_side.West_Colors = self.Y_side.gear_colors[:,2]
        self.B_side.North_Orientations = self.R_side.gear_orientations[2]
        self.B_side.South_Orientations = self.V_side.gear_orientations[0]
        self.B_side.East_Orientations = self.O_side.gear_orientations[:,0]
        self.B_side.West_Orientations = self.Y_side.gear_orientations[:,2]
        self.B_side.North_Neighbor = self.R_side
        self.B_side.South_Neighbor = self.V_side
        self.B_side.East_Neighbor = self.O_side
        self.B_side.West_Neighbor = self.Y_side
        self.B_side.Opp_Side = self.G_side
        #Orange:
        self.O_side.North_Colors = self.R_side.gear_colors[:,2]
        self.O_side.South_Colors = self.V_side.gear_colors[:,2]
        self.O_side.East_Colors = self.G_side.gear_colors[:,0]
        self.O_side.West_Colors = self.B_side.gear_colors[:,2]
        self.O_side.North_Orientations = self.R_side.gear_orientations[:,2]
        self.O_side.South_Orientations = self.V_side.gear_orientations[:,2]
        self.O_side.East_Orientations = self.G_side.gear_orientations[:,0]
        self.O_side.West_Orientations = self.B_side.gear_orientations[:,2]
        self.O_side.North_Neighbor = self.R_side
        self.O_side.South_Neighbor = self.V_side
        self.O_side.East_Neighbor = self.G_side
        self.O_side.West_Neighbor = self.B_side
        self.O_side.Opp_Side = self.Y_side
        #Yellow:
        self.Y_side.North_Colors = self.R_side.gear_colors[:,0]
        self.Y_side.South_Colors = self.V_side.gear_colors[:,0]
        self.Y_side.East_Colors = self.B_side.gear_colors[:,0]
        self.Y_side.West_Colors = self.G_side.gear_colors[:,2]
        self.Y_side.North_Orientations = self.R_side.gear_orientations[:,0]
        self.Y_side.South_Orientations = self.V_side.gear_orientations[:,0]
        self.Y_side.East_Orientations = self.B_side.gear_orientations[:,0]
        self.Y_side.West_Orientations = self.G_side.gear_orientations[:,2]
        self.Y_side.North_Neighbor = self.R_side
        self.Y_side.South_Neighbor = self.V_side
        self.Y_side.East_Neighbor = self.B_side
        self.Y_side.West_Neighbor = self.G_side
        self.Y_side.Opp_Side = self.O_side
        #Green:
        self.G_side.North_Colors = self.R_side.gear_colors[0]
        self.G_side.South_Colors = self.V_side.gear_colors[2]
        self.G_side.East_Colors = self.Y_side.gear_colors[:,0]
        self.G_side.West_Colors = self.O_side.gear_colors[:,2]
        self.G_side.North_Orientations = self.R_side.gear_orientations[0]
        self.G_side.South_Orientations = self.V_side.gear_orientations[2]
        self.G_side.East_Orientations = self.Y_side.gear_orientations[:,0]
        self.G_side.West_Orientations = self.O_side.gear_orientations[:,2]
        self.G_side.North_Neighbor = self.R_side
        self.G_side.South_Neighbor = self.V_side
        self.G_side.East_Neighbor = self.Y_side
        self.G_side.West_Neighbor = self.O_side
        self.G_side.Opp_Side = self.B_side
        #Red:
        self.R_side.North_Colors = self.G_side.gear_colors[0]
        self.R_side.South_Colors = self.B_side.gear_colors[0]
        self.R_side.East_Colors = self.O_side.gear_colors[0]
        self.R_side.West_Colors = self.Y_side.gear_colors[0]
        self.R_side.North_Orientations = self.G_side.gear_orientations[0]
        self.R_side.South_Orientations = self.B_side.gear_orientations[0]
        self.R_side.East_Orientations = self.O_side.gear_orientations[0]
        self.R_side.West_Orientations = self.Y_side.gear_orientations[0]
        self.R_side.North_Neighbor = self.G_side
        self.R_side.South_Neighbor = self.B_side
        self.R_side.East_Neighbor = self.O_side
        self.R_side.West_Neighbor = self.Y_side
        self.R_side.Opp_Side = self.V_side
        #Violet:
        self.V_side.North_Colors = self.B_side.gear_colors[2]
        self.V_side.South_Colors = self.G_side.gear_colors[2]
        self.V_side.East_Colors = self.O_side.gear_colors[2]
        self.V_side.West_Colors = self.Y_side.gear_colors[2]
        self.V_side.North_Orientations = self.B_side.gear_orientations[2]
        self.V_side.South_Orientations = self.G_side.gear_orientations[2]
        self.V_side.East_Orientations = self.O_side.gear_orientations[2]
        self.V_side.West_Orientations = self.Y_side.gear_orientations[2]
        self.V_side.North_Neighbor = self.B_side
        self.V_side.South_Neighbor = self.G_side
        self.V_side.East_Neighbor = self.O_side
        self.V_side.West_Neighbor = self.Y_side
        self.V_side.Opp_Side = self.R_side
        
        #Might have to give similar pointers to the cell which contains the 4 gears that need to update for each side
        #will be less verbose because (Green, Blue), (Red, Violet), (Yellow, Orange) will point to the same ones

        
    def copy(self, to, fro):
        for i, cell in enumerate(fro):
            to[i] = cell
           
    def ccw(self, side):
       #make this just call clock wise 3 times
       for i in range(11):
           self.cw(side)
           self.cw(side.Opp_Side)

    
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

        temp5 = side.gear_orientations[:,0].copy()#save original contents 
        temp6 = side.gear_orientations[0].copy()
        temp7 = side.gear_orientations[:,2].copy()
        temp8 = side.gear_orientations[2].copy()
        
        self.copy(side.gear_colors[:,2], temp2)#first row> last column
        self.copy(side.gear_colors[2], temp3[::-1])#last column > last row
        self.copy(side.gear_colors[:,0], temp4)#last row > first column
        self.copy(side.gear_colors[0], temp1[::-1])#first coulmn > first row

        self.copy(side.gear_orientations[:,2], temp6)#first row> last column
        self.copy(side.gear_orientations[2], temp7[::-1])#last column > last row
        self.copy(side.gear_orientations[:,0], temp8)#last row > first column
        self.copy(side.gear_orientations[0], temp5[::-1])#first coulmn > first row
        
        #LAST, rotate the adjacent, connected rows and columns of neighboring sides
        
        temp1 = side.East_Colors.copy()#save original contents 
        temp2 = side.South_Colors.copy()
        temp3 = side.West_Colors.copy()
        temp4 = side.North_Colors.copy()

        temp5 = side.East_Orientations.copy()#save original contents 
        temp6 = side.South_Orientations.copy()
        temp7 = side.West_Orientations.copy()
        temp8 = side.North_Orientations.copy()
        
        #as an artifact of my layout, which assumes blue to be the center, some rows, columns must be inverted first:
        if side.color == 'Blue':
            temp1 = temp1[::-1]
            temp3 = temp3[::-1]
            temp5 = temp5[::-1]
            temp7 = temp7[::-1]
        if side.color == 'Yellow':
            temp2 = temp2[::-1]
            temp3 = temp3[::-1]
            temp6 = temp6[::-1]
            temp7 = temp7[::-1]
        if side.color == 'Orange':
            temp1 = temp1[::-1]
            temp4 = temp4[::-1]
            temp5 = temp5[::-1]
            temp8 = temp8[::-1]
        if side.color == 'Green':
            temp4 = temp4[::-1]
            temp2 = temp2[::-1]
            temp8 = temp8[::-1]
            temp6 = temp6[::-1]
        
        self.copy(side.East_Colors, temp4)
        self.copy(side.South_Colors, temp1)
        self.copy(side.West_Colors, temp2)
        self.copy(side.North_Colors, temp3)

        self.copy(side.East_Orientations, temp8)
        self.copy(side.South_Orientations, temp5)
        self.copy(side.West_Orientations, temp6)
        self.copy(side.North_Orientations, temp7)
        
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

        if side.North_Neighbor.South_Neighbor == side or side.North_Neighbor.North_Neighbor == side:
            side.North_Neighbor.gear_orientations[1][0] = (side.North_Neighbor.gear_orientations[1][0] + 30) % 360
            side.North_Neighbor.gear_orientations[1][2] = (side.North_Neighbor.gear_orientations[1][2] + 30) % 360
        else:
            side.North_Neighbor.gear_orientations[0][1] = (side.North_Neighbor.gear_orientations[0][1] + 30) % 360
            side.North_Neighbor.gear_orientations[2][1] = (side.North_Neighbor.gear_orientations[2][1] + 30) % 360

        if side.South_Neighbor.South_Neighbor == side or side.South_Neighbor.North_Neighbor == side:
            side.South_Neighbor.gear_orientations[1][0] = (side.South_Neighbor.gear_orientations[1][0] + 30) % 360
            side.South_Neighbor.gear_orientations[1][2] = (side.South_Neighbor.gear_orientations[1][2] + 30) % 360
        else:
            side.South_Neighbor.gear_orientations[0][1] = (side.South_Neighbor.gear_orientations[0][1] + 30) % 360
            side.South_Neighbor.gear_orientations[2][1] = (side.South_Neighbor.gear_orientations[2][1] + 30) % 360

        if side.East_Neighbor.South_Neighbor == side or side.East_Neighbor.North_Neighbor == side:
            side.East_Neighbor.gear_orientations[1][0] = (side.East_Neighbor.gear_orientations[1][0] + 30) % 360
            side.East_Neighbor.gear_orientations[1][2] = (side.East_Neighbor.gear_orientations[1][2] + 30) % 360
        else:
            side.East_Neighbor.gear_orientations[0][1] = (side.East_Neighbor.gear_orientations[0][1] + 30) % 360
            side.East_Neighbor.gear_orientations[2][1] = (side.East_Neighbor.gear_orientations[2][1] + 30) % 360

        if side.West_Neighbor.South_Neighbor == side or side.West_Neighbor.North_Neighbor == side:
            side.West_Neighbor.gear_orientations[1][0] = (side.West_Neighbor.gear_orientations[1][0] + 30) % 360
            side.West_Neighbor.gear_orientations[1][2] = (side.West_Neighbor.gear_orientations[1][2] + 30) % 360
        else:
            side.West_Neighbor.gear_orientations[0][1] = (side.West_Neighbor.gear_orientations[0][1] + 30) % 360
            side.West_Neighbor.gear_orientations[2][1] = (side.West_Neighbor.gear_orientations[2][1] + 30) % 360
        
        
    
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

        self.R_side.print_Side_Colors()
        print('\n')

        for i in range(0,3):
            print(f"{str(self.Y_side.gear_colors[i]): <30}{str(self.B_side.gear_colors[i]): <30}{str(self.O_side.gear_colors[i]): <30}{str(self.G_side.gear_colors[i]): <30}")
        print('\n')
        self.V_side.print_Side_Colors()
        print('\n\n')

        self.R_side.print_Side_Orientations()
        print('\n')

        for i in range(0,3):
            print(f"{str(self.Y_side.gear_orientations[i]): <30}{str(self.B_side.gear_orientations[i]): <30}{str(self.O_side.gear_orientations[i]): <30}{str(self.G_side.gear_orientations[i]): <30}")
        print('\n')
        self.V_side.print_Side_Orientations()
        print('\n\n')
        
        
    def scramble(self, number_moves):
        print('\nStart State of Gear Ball:\n')
        self.print_Puzzle_State()
        last_side = -1
        last_dir = -1
        i = 0
        
        while i < number_moves:
            which_side = np.random.randint(0,3)#pick a random side to rotate wrt
            which_dir = np.random.randint(0,2)#pick random direction (2 choices: cw, or ccw)
            
            if ((which_side == last_side) and (which_dir == last_dir)) or (which_side != last_side):#dissallows moves that undoes that previous one
                
            #doesnt work all the way yet
                
                # for instance, Green CCW follow by Blue CW is allowed but shouldnt be
                # because the gears enforce that when Blue moves, Green moves the same direction, vice versa
                
                if which_dir == 0: #same as 3 clockwise rotations
                
                    self.ccw(self.all_sides[which_side])
                    
                    
                    print(str(i)+' AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CCW :')
                    self.print_Puzzle_State()
                    
                else:
                    self.cw(self.all_sides[which_side])
                    self.cw(self.all_sides[which_side].Opp_Side)
                    print(str(i)+' AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CW :')
                    self.print_Puzzle_State()
                    
                i = i + 1
                
                last_side = which_side
                last_dir = which_dir
            else:
                print('random:'+str(self.all_sides[which_side].color)+', last:'+str(self.all_sides[last_side].color))
                print('random:'+str(which_dir)+', last:'+str(last_side))
                
            
