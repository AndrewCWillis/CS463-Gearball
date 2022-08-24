# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:23:56 2022

Author: Andrew C. Willis 
Class: CS 463G, Assignment 1
"""
import numpy as np

class special_gears:
    def __init__(self):
        #should have attribute for:
        #ID: unique number ID (0-8)
        #Colors: 2 colors
        #Location: 2 sides 
        #Angle: starts at zero, perpindicular movements will increment or decrement by 60 degrees
        #There are 8? of these gears in total
        #One perpendicular rotation should move 4 of these gears, +/- 60 degrees (depending on up or down rotation)
        #In such a rotation the other 4 are idle
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
                
                #My suspicion is that it should work like a rubiks cube, but you have to add bells and whistles for those cardinal gears
                #which are shared between sides and rotate x-degrees when the movement direction is perpindicular
        
        #Special Gears: These are shared between neigbhoring sides (direct neigbhors), so they should point to the same 
            #Special Gear object
            # each side has one special gear at the N,S,E,W position and is shared with that neighbor (N,S,E,W)
    def print_Side_State(self):
        for i in self.gear_colors:
            print('\t\t\t\t'+str(i))
            
            
                
class gearball:
    def __init__(self):
        # Should have attributes for:
        # Sides: 1D list of class sides of length 6
        # Methods for:
            #movements
            #randomization
        self.G_side = side('Green', 
        np.array([['G','G','G'],
         ['G','G*','G'],
         ['G','G','G']]))
        self.R_side = side('Red', 
                  np.array([['R','R','R'],
                   ['R','R*','R'],
                   ['R','R','R']]))
        self.B_side = side('Blue', 
                  np.array([['B','B','B'],
                   ['B','B*','B'],
                   ['B','B','B']]))
        self.O_side = side('Orange', 
                  np.array([['O','O','O'],
                   ['O','O*','O'],
                   ['O','O','O']]))
        self.Y_side = side('Yellow', 
                  np.array([['Y','Y','Y'],
                   ['Y','Y*','Y'],
                   ['Y','Y','Y']]))
        self.V_side = side('Violet', 
                  np.array([['V','V','V'],
                   ['V','V*','V'],
                   ['V','V','V']]))
        #Next, store pointers to these sides to define adjacency mapping to touching rows, columns
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
        #side should be a pointer to the side determined in the toggle function
        print('BEFORE:')
        self.print_Puzzle_State()
        #side should be a pointer to the side determined in the toggle function
        
       
        #FIRST, rotate the side which rotation is wrt
        #side.gear_colors = np.rot90(side.gear_colors)#great but can not use because it screws with the pointers
        temp1 = side.gear_colors[:,0].copy()#save original contents 
        temp2 = side.gear_colors[0].copy()
        temp3 = side.gear_colors[:,2].copy()
        temp4 = side.gear_colors[2].copy()
        
        self.copy(side.gear_colors[:,0], temp2[::-1])#first row> first column
        self.copy(side.gear_colors[2], temp1)
        self.copy(side.gear_colors[:,2], temp4[::-1])
        self.copy(side.gear_colors[0], temp3)
        
        #LAST, rotate the adjacent, connected rows and columns of neighboring sides
        temp1 = side.West_Neighbor.copy()
        #print(temp1)
        self.copy(side.West_Neighbor, side.North_Neighbor)
        
        temp2 = side.South_Neighbor.copy()
        #print(temp2)
        self.copy(side.South_Neighbor, temp1)
        
        temp1 = side.East_Neighbor.copy()
        #print(temp1)
        self.copy(side.East_Neighbor, temp2)
        
        self.copy(side.North_Neighbor, temp1)

        print('AFTER:')
        self.print_Puzzle_State()
    
    def cw(self, side):
        print('BEFORE:')
        self.print_Puzzle_State()
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

        print('AFTER:')
        self.print_Puzzle_State()
        
        
    
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
            print(str(self.Y_side.gear_colors[i])+'\t'+str(self.B_side.gear_colors[i])+'\t'+str(self.O_side.gear_colors[i])+'\t'+str(self.G_side.gear_colors[i]))
        print('\n')
        self.V_side.print_Side_State()
        print('\n\n')

def main():
    #initialize the gear ball
    puzzle = gearball()
    
    puzzle.cw(puzzle.B_side)
    puzzle.cw(puzzle.B_side.Opp_Side)
    puzzle.cw(puzzle.R_side)
    puzzle.cw(puzzle.R_side.Opp_Side)
    puzzle.ccw(puzzle.R_side)
    puzzle.ccw(puzzle.R_side.Opp_Side)
    puzzle.ccw(puzzle.B_side)
    puzzle.ccw(puzzle.B_side.Opp_Side)
    #puzzle.ccw(puzzle.R_side)
    
    #maybe I can make pointers to the row, column it touches instead of the whole side?

if __name__ == "__main__":
    main()
