# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:08:24 2022

@author: Owner
"""
import GearballModel
import numpy as np
import math
import pandas as pd
import time

class solver:
    def __init__(self, num_scramble): 
        self.heap = [] #can use the list.sort() method to make a heap / priority queue
        #might do tuples ini the heap. (F_value, Pointer_To_State_Instance)
        self.q = []
        self.start_state = GearballModel.gearball()
        self.start_state.scramble(num_scramble)
        self.translate = {0.0 : 0.0, 60.0 : 1.0, 120.0 : 2.0, 180.0 : 3.0, 240.0 : 2, 300.0 : 1}

        
    def find_children(self, state):
        #needs to take a state and generate a new child (6 total) for Blue,Red,Yellow rotation cw and ccw
        #make the cw(), ccw() functions return a copy of the gearball, or make a function that allows you to declare
        #a new gearball object provided the color states
        children = []
        children_depth = state.depth + 1
        '''
        for side in state.all_sides:#pointers to the states blue,red,yellow sides
            state.cw(side)
            state.cw(side.Opp_Side)
            
            children.append(GearballModel.gearball(children_depth, [state.G_side.gear_colors.copy(), 
                                                                    state.R_side.gear_colors.copy(),
                                                                    state.B_side.gear_colors.copy(),
                                                                    state.O_side.gear_colors.copy(),
                                                                    state.Y_side.gear_colors.copy(),
                                                                    state.V_side.gear_colors.copy()], 
                                                                    np.array( [state.G_side.gear_orientations.copy(), 
                                                                               state.R_side.gear_orientations.copy(),
                                                                               state.B_side.gear_orientations.copy(),
                                                                               state.O_side.gear_orientations.copy(),
                                                                               state.Y_side.gear_orientations.copy(),
                                                                               state.V_side.gear_orientations.copy()]), 
                                                                    parent = state, previous = str(side.color+' cw')))

            #declare a new gearball state and set its state to be the result of the move just executed
            #should undo the previous move so that subsequent results are accurate:
            state.ccw(side) 
         '''   
        
        for side in state.all_sides:#pointers to the states blue,red,yellow sides
            state.ccw(side) #should undo the previous move so that subsequent results are accurate
            
            children.append(GearballModel.gearball(children_depth, [state.G_side.gear_colors.copy(), 
                                                                    state.R_side.gear_colors.copy(),
                                                                    state.B_side.gear_colors.copy(),
                                                                    state.O_side.gear_colors.copy(),
                                                                    state.Y_side.gear_colors.copy(),
                                                                    state.V_side.gear_colors.copy()], 
                                                                    np.array( [state.G_side.gear_orientations.copy(), 
                                                                               state.R_side.gear_orientations.copy(),
                                                                               state.B_side.gear_orientations.copy(),
                                                                               state.O_side.gear_orientations.copy(),
                                                                               state.Y_side.gear_orientations.copy(),
                                                                               state.V_side.gear_orientations.copy()]), 
                                                                    parent = state, previous = str(side.color+' ccw')))
            #declare a new gearball state and set its state to be the result of the move just executed
            state.cw(side)
            state.cw(side.Opp_Side) #should undo the previous move so that subsequent results are accurate
            
        return children
    def gear_distance(self, state):
        #will get the total number of turns to return the gear orientations to 0-degrees. Can be at most 3 turns
        #for each (3) groups of 4 gears. 
        group_angles = {0.0} # because there are 3 groups of 4 gears each, and each group all has the same orientations
        #i just add all of the data from gear rotations to have a set to extract the unique entries 
        
        for side in state.all_sides:
            #I only check 3 sides to exploit symmetry of the gear ball
            #opposite sides will have the same exact gear orientations always
            group_angles = group_angles.union(set(x for x in side.gear_orientations.flatten())) 
        #Next, calculate the minimum distance home for each entry:
        sum = 0
        for entry in group_angles:
            sum += self.translate[entry]
        return sum
    
    def num_colors(self, state):
        #second component of the heuristic value-- get the number of colors on each face
        #I only check 3 sides to exploit symmetry of the gear ball
        #opposite sides will have the same exact number of colors, always
        ''' I want to double check if i should the floor or cieling of the result here'''
        num_colors = []
        for side in state.all_sides:
            #I only check 3 sides to exploit symmetry of the gear ball
            #opposite sides will have the same exact gear orientations always
            num_colors.append(2 * (len(set(x[0] if len(x) > 1 else x for x in side.gear_colors.flatten() )) - 1))
        # This counts the number of colors on a side (excluding expected color) and adds to a list
        # multiply by 2 because we are including each sides opposite in the tally, which has the same number of colors
        
        '''NEXT: sum the results, divide by something and take the FLOOR or CIELING'''
        
        return math.ceil(sum(num_colors) / 8)
    
    def heuristic_value(self, state):
        #should return an integer
        #check the number of colors on a side 
        #check minimum number of turns for gears to be correct
        #return the max of these two values
        return max(self.num_colors(state), self.gear_distance(state))
        
    def f_value(self, state):
        #self.f_value(self.start_state) = h(start_state)+ start_state.depth)
        #need to create a pointer which tethers a puzzle state to its f_value
        return self.heuristic_value(state) + state.depth
    
    def enheap(self, state):
        pointer = state
        tup = (self.f_value(state), pointer)
        
        self.heap.append(tup)
        self.heap.sort(key = lambda x: x[0]) #sort by the first entry of the tuple, which is the f_value
    def print_path(self, state):
        pointer = state
        move = 0
        while pointer != None:
            #pointer.print_Puzzle_State()
            print(str(move)+ ': '+ pointer.previous_move)
            pointer = pointer.parent
            move = move + 1
            
    def a_star(self):
        #probably want to delete gearball objects using the del obj command for memory
        #probably want to add parameters for pointer to parent and child in GearBall Model, also depth
        print('Begin A* solver: ')
        start_time = time.time()
        self.q.append(self.start_state)
        self.enheap(self.start_state)
        nodes_expanded = 0
        while len(self.q) != 0:
            #pop from the heap, find corresponding puzzle state
            p = self.heap.pop(0) # get the first entry in the heap
            #p[1]. print_Puzzle_State()
            #check if p = solved (heuristic = 0)
            if self.heuristic_value(p[1]) == 0.0:
                end_time = time.time() - start_time
                print('Time to find solution: '+ str(end_time))
                print('Nodes expanded to find solution: '  + str(nodes_expanded))
                p[1].print_Puzzle_State()
                self.print_path(p[1])
                break
            else:
                node_expanded = nodes_expanded + 1
                children = self.find_children(p[1])
                for child in children:
                    self.enheap(child)
                    self.q.append(child)
def main():
    puzzle_solver = solver(8)
    children = puzzle_solver.find_children(puzzle_solver.start_state)
    '''
    for child in children:
        child.print_Puzzle_State()
        print('Number of Colors Heuristic: '+str(puzzle_solver.num_colors(child)))
        print('Gear Distance Heuristic: '+str(puzzle_solver.gear_distance(child)))
        print('F-Value (Heuristic + depth): '+str(puzzle_solver.f_value(child)))
    '''   
    puzzle_solver.a_star()
if __name__ == "__main__":
    main()