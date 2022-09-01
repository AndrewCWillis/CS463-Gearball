# -*- coding: utf-8 -*-
import GearballModel

def main():# I think she wants this to be its own script
    #initialize the gear ball
    puzzle = GearballModel.gearball()
    running = True
    
    while running:
        inp = input('Please Select One of the Following Operations to Perform:\n'+
                '1. Scramble the Gear Ball  by N- rotations (Respond 1) \n'+
                '2. Provide the Side to Move(Red, Yellow, Blue, Orange, Green, or Violet), & the Direction (CW, or CCW) (Respond 2)\n'+
                '3. Quit program\n')
    
        if inp == '1':
            print('\nYou Want to Scramble.')
            num_moves = input('Please Provide an (Integer) Number of Moves to Scramble the Gear Ball:\n')
            puzzle.scramble(int(num_moves)) 
        elif inp == '2':
            print('\nYou Want to Move a Side')
            which_side = int(input('Please Provide the side to turn (1-6):\n1. Red/Violet\n2. Blue/Green\n3. Yellow/Orange\n'))
            direction = int(input('\nPlease Provide the direction to turn (1 or 2):\n1. Clockwise\n2. Counterclockwise\n'))
            num_moves = int(input('\nPlease Provide an (Integer) Number of Moves:\n'))
            print('\nStart State of Gear Ball:\n')
            puzzle.print_Puzzle_State()
            if(direction == 1):
                for i in range(num_moves):
                    print(str(i)+' AFTER, ' + puzzle.all_sides[which_side-1].color +', ' +puzzle.all_sides[which_side-1].Opp_Side.color+ ', CW :')
                    puzzle.cw(puzzle.all_sides[which_side-1])
                    puzzle.cw(puzzle.all_sides[which_side-1].Opp_Side)
                    puzzle.print_Puzzle_State()
            else:
                for i in range(num_moves):
                    print(str(i)+' AFTER, ' + puzzle.all_sides[which_side-1].color +', ' +puzzle.all_sides[which_side-1].Opp_Side.color+ ', CCW :')
                    puzzle.ccw(puzzle.all_sides[which_side-1])
                    puzzle.print_Puzzle_State()
        elif inp == '3':
            running = False
        else:
            print('PLEASE SELECT A VALID OPTION!!! (1, 2, or 3)\n')
    
    
 
    
    

    
  

if __name__ == "__main__":
    main()
