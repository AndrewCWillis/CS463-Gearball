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



class side: 
    #the side class will contain all the information relative to one of the six sides of the cube
    def __init__(self, color, start_colors, start_orientations): 
        self.color = color #unique identifer, string
        self.gear_colors = np.array(start_colors)
        self.gear_orientations = np.array(start_orientations)

        self.North_Neighbor = None#now points to the other sides
        self.East_Neighbor = None
        self.South_Neighbor = None
        self.West_Neighbor = None
        self.Opp_Side = None

        self.North_Colors = None#points to the row of colors adjacent to the current side, which are displaced by rotation
        self.East_Colors = None
        self.South_Colors = None
        self.West_Colors = None

        self.North_Orientations = None#points to the orientations of the gears of neighboring sides
        self.East_Orientations = None
        self.South_Orientations = None
        self.West_Orientations = None

    def print_Side_Colors(self):
        for i in self.gear_colors:
            print(f"{str(i): >50}") 

    def print_Side_Orientations(self):
        for i in self.gear_orientations:
            print(f"{str(i): >37}") 
            
            
                
class gearball:
    def __init__(self, depth = 0, start_state = [
    [['G','G+(R_G)','G'],
     ['G+(O_G)','G*','G+(G_Y)'],
     ['G','G+(G_V)','G']], 
    [['R','R+(R_G)','R'],
      ['R+(R_Y)','R*','R+(R_O)'],
      ['R','R+(R_B)','R']],
    [['B','B+(R_B)','B'],
       ['B+(Y_B)','B*','B+(B_O)'],
       ['B','B+(B_V)','B']],
    [['O','O+(R_O)','O'],
        ['O+(B_O)','O*','O+(O_G)'],
        ['O','O+(O_V)','O']], 
    [['Y','Y+(R_Y)','Y'],
         ['Y+(G_Y)','Y*','Y+(Y_B)'],
         ['Y','Y+(Y_V)','Y']],
    [['V','V+(B_V)','V'],
          ['V+(Y_V)','V*','V+(O_V)'],
          ['V','V+(G_V)','V']] ], start_orient = np.zeros((6,3,3)), parent = None, previous = 'start state scramble'):
        #KWARGs for starting at default = solved state or some other provided state to facilitate solving program
        
        self.heur = 0.0 #looking at the next assigment
        self.depth = depth
        self.parent = parent
        self.previous_move = previous
        #4 gears will increment or decrement angle by 120 degrees
        
        self.G_side = side('Green', 
        np.array(start_state[0]),
        start_orient[0])
        self.R_side = side('Red', 
                  np.array(start_state[1]),
                   start_orient[1])
        self.B_side = side('Blue', 
                  np.array(start_state[2]),
                    start_orient[2])
        self.O_side = side('Orange', 
                  np.array(start_state[3]),
                    start_orient[3])
        self.Y_side = side('Yellow', 
                  np.array(start_state[4]),
                    start_orient[4])
        self.V_side = side('Violet', 
                  np.array(start_state[5]),
                    start_orient[5])
        self.all_sides = np.array([self.R_side,self.B_side,self.Y_side])
        '''
        [B_R, B_O, B_V, B_Y, R_G, R_O, R_Y, G_Y, Y_V, O_G, O_V, G_V] are the gears
        HAVE NOT FINISHED THE GEARS YET! There postion is fixed to the piece beside and below them, and that is how
        they are displayed textually. The last step is to track their angle.
        
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
        '''
        #Next, store pointers to these sides to define adjacency mapping to touching rows, or columns of the np.arrays
        #initializing the instance virables for each side necessary to implement rotations precisly 
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
       #one counter clockwise rotation is in this instance = 11 cw rotations (not 3 owing to the gear angles)
       for i in range(11):
           self.cw(side)
           self.cw(side.Opp_Side)#call on the opposite side too because they rotate in unison

    
    def cw(self, side):

        #FIRST, rotate the side which rotation is wrt
        #side.gear_colors = np.rot90(side.gear_colors, 3)#great but can not use because it screws with the pointers

        temp1 = side.gear_colors[:,0].copy()#save original contents of affected rows, columns
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
        #which are displaced by the rotation of the side
        
        temp1 = side.East_Colors.copy()#save original contents 
        temp2 = side.South_Colors.copy()
        temp3 = side.West_Colors.copy()
        temp4 = side.North_Colors.copy()

        temp5 = side.East_Orientations.copy()#save original contents 
        temp6 = side.South_Orientations.copy()
        temp7 = side.West_Orientations.copy()
        temp8 = side.North_Orientations.copy()
        
        #as an artifact of my layout, which assumes blue to be the center, some rows, columns must be inverted first:
        #that is because the bottom cell of one row, or column will become the first cell in the row,column it is displaced
        #to, thus we have to invert it in the following cases
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
        
        #last, orient the gears to be the correct angle after a rotation
        #4 gears will change angle during a single rotation
        #they increment 300 degrees

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
        
    
    
    def print_Puzzle_State(self):
        #this is the GUI component of the project, prints the contents of each sides array in an unfolded layout
        
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
        self.print_Puzzle_State()#print before and after
        last_side = -1#remember what last rotation was so we dont undo it
        last_dir = -1#remember what last rotation direction was so we dont undo it
        
        i = 0
        
        while i < number_moves:#for the number of moves requested
            which_side = np.random.randint(0,3)#pick a random side to rotate wrt
            #3 and not six because opposite sides rotate at the same time in same direction
            #thus Green=Blue Red=Violet Yellow=Orange, so 3 is just easier and exactly the same
            '''
            which_dir = np.random.randint(0,2)#pick random direction (2 choices: cw(1), or ccw(0))
            '''
            which_dir = 1
            if ((which_side == last_side) and (which_dir == last_dir)) or (which_side != last_side):#dissallows moves that undoes that previous one
                
                
                if which_dir == 0: #same as 3 clockwise rotations
                
                    self.ccw(self.all_sides[which_side])
                    
                    
                    print(str(i)+' AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CCW :')
                    self.print_Puzzle_State()
                    
                else:#clockwise rotation
                    self.cw(self.all_sides[which_side])
                    self.cw(self.all_sides[which_side].Opp_Side)
                    #call twice because both side and its opposite rotate in unison
                    print(str(i)+' AFTER, ' + self.all_sides[which_side].color +', ' +self.all_sides[which_side].Opp_Side.color+ ', CW :')
                    self.print_Puzzle_State()
                    
                i = i + 1 #increment
                
                last_side = which_side
                last_dir = which_dir
            else:
                print('random:'+str(self.all_sides[which_side].color)+', last:'+str(self.all_sides[last_side].color))
                print('random:'+str(which_dir)+', last:'+str(last_side))
                
            
