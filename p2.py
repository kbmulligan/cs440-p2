"""
CS440 Assignment 2
Submitted by K. Brett Mulligan (CSUID: 830189830)
My code utilizes the search.py code from the Norvig text.
It searches for solutions to the Huarong Pass puzzle using different search methods.
To find a solution to the puzzle, just execute the file. 
The code will print each solution as a list of actions which will lead to the goal state.
"""

#################################################
# p2.py - find a solution to the Huarong Pass Puzzle
# by K. Brett Mulligan
# 9 Sep 2014
# CSU CS440
# Dr. Asa Ben-Hur
#################################################

import search


DO_TESTING = True


BLANK = 'X'

initial_state = (('A', 'B', 'B', 'C'),
                 ('A', 'B', 'B', 'C'),
                 ('D', 'E', 'E', 'F'),
                 ('D', 'G', 'H', 'F'),
                 ('I', 'X', 'X', 'J'))

goal_state =    (('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'B', 'B', 'X'),
                 ('X', 'B', 'B', 'X'))

no_state =      (('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'))

bogus_state =   (('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'X', 'X', 'X'),
                 ('X', 'B', 'X', 'X'),
                 ('X', 'X', 'X', 'X'))

testing_state =   (('X', 'X', 'X', 'X'),
                   ('X', 'X', 'C', 'X'),
                   ('X', 'X', 'C', 'X'),
                   ('X', 'E', 'E', 'X'),
                   ('X', 'X', 'X', 'X'))

testing_state0 =  (('B', 'B', 'X', 'X'),
                   ('B', 'B', 'C', 'X'),
                   ('X', 'X', 'C', 'I'),
                   ('X', 'E', 'E', 'H'),
                   ('X', 'X', 'X', 'X'))

testing_state1 =  (('X', 'X', 'X', 'X'),
                   ('I', 'J', 'C', 'X'),
                   ('G', 'H', 'C', 'X'),
                   ('X', 'E', 'E', 'F'),
                   ('X', 'X', 'X', 'F'))

e_state =         (('X', 'X', 'X', 'X'),
                   ('X', 'X', 'X', 'X'),
                   ('X', 'X', 'X', 'X'),
                   ('X', 'E', 'E', 'X'),
                   ('X', 'X', 'X', 'X'))

# dictionary full of test states organized by tile
test_state = {  'A':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'A', 'X', 'X'),
                       ('X', 'A', 'X', 'X'),
                       ('X', 'X', 'X', 'X')),

                'B':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'B', 'B', 'X'),
                       ('X', 'B', 'B', 'X'),
                       ('X', 'X', 'X', 'X')),

                'C':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'C', 'X', 'X'),
                       ('X', 'C', 'X', 'X'),
                       ('X', 'X', 'X', 'X')),

                'D':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'D', 'X'),
                       ('X', 'X', 'D', 'X'),
                       ('X', 'X', 'X', 'X')),

                'E':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'E', 'E', 'X'),
                       ('X', 'X', 'X', 'X')),

                'F':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'F', 'X'),
                       ('X', 'X', 'F', 'X'),
                       ('X', 'X', 'X', 'X')),

                'G':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'G', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X')),

                'H':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'H', 'X', 'X'),
                       ('X', 'X', 'X', 'X')),

                'I':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'I', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X')),

                'J':  (('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'X', 'X'),
                       ('X', 'X', 'J', 'X'),
                       ('X', 'X', 'X', 'X'))
}



# state is a tuple of dimensions  5x4, i.e. 5 rows of 4 columns each
# individual elements are addressed row first, then column, e.g. state[4][0] = 'I'

# action is a tuple of length 2
# action includes, the tile and direction
# e.g. ('G', 'LEFT') or ('A', 'DOWN')



######### MAIN CLASS ##################
class HuarongPass(search.Problem):
    """This class extendes search.Problem and implements the actions, 
    result, and goal_test methods. To use this class, instantiate it, 
    and call the appropriate search.py methods on it."""

    # tiles = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    tiles_single = ('G', 'H', 'I', 'J')
    tiles_vtwo = ('A', 'C', 'D', 'F')
    tiles_htwo = ('E')
    tiles_four = ('B')

    directions = ('UP', 'DOWN', 'LEFT', 'RIGHT')

    all_possible_actions = []

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once. This time
        they're just going to be a list."""
        return [action for action in self.generate_all_actions(state) if not self.has_conflict(state, action)]

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state). We're assuming since the action comes 
        from self.actions(state) that it's an allowable action."""
        mut_state = self.mutable_state(state)

        coords = self.get_coords(state, tile_of(action))

        if (tile_of(action) in self.tiles_single):                          # Single blocks, fairly straightforward
            if (direction_of(action) == 'UP'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] - 1][coords[1]] = tile_of(action)

            elif (direction_of(action) == 'DOWN'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] + 1][coords[1]] = tile_of(action)

            elif (direction_of(action) == 'LEFT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] - 1] = tile_of(action)

            elif (direction_of(action) == 'RIGHT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 1] = tile_of(action)
            else:
                print "result: Invalid direction passed."

        elif (tile_of(action) in self.tiles_vtwo):                          # VERTICAL 2x1 blocks, tricky
            if (direction_of(action) == 'UP'):
                mut_state[coords[0] + 1][coords[1]] = BLANK
                mut_state[coords[0] - 1][coords[1]] = tile_of(action)

            elif (direction_of(action) == 'DOWN'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] + 2][coords[1]] = tile_of(action)

            elif (direction_of(action) == 'LEFT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] + 1][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] - 1] = tile_of(action)
                mut_state[coords[0] + 1][coords[1] - 1] = tile_of(action)

            elif (direction_of(action) == 'RIGHT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] + 1][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 1] = tile_of(action)
                mut_state[coords[0] + 1][coords[1] + 1] = tile_of(action)
            else:
                print "result: Invalid direction passed."

        elif (tile_of(action) in self.tiles_htwo):                          # HORIZONTAL 2x1 block, also tricky
            if (direction_of(action) == 'UP'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 1] = BLANK
                mut_state[coords[0] - 1][coords[1]] = tile_of(action)
                mut_state[coords[0] - 1][coords[1] + 1] = tile_of(action)

            elif (direction_of(action) == 'DOWN'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 1] = BLANK
                mut_state[coords[0] + 1][coords[1]] = tile_of(action)
                mut_state[coords[0] + 1][coords[1] + 1] = tile_of(action)

            elif (direction_of(action) == 'LEFT'):
                mut_state[coords[0]][coords[1] + 1] = BLANK
                mut_state[coords[0]][coords[1] - 1] = tile_of(action)

            elif (direction_of(action) == 'RIGHT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 2] = tile_of(action)
            else:
                print "result: Invalid direction passed."

        elif (tile_of(action) in self.tiles_four):
            if (direction_of(action) == 'UP'):
                mut_state[coords[0] + 1][coords[1]] = BLANK
                mut_state[coords[0] + 1][coords[1] + 1] = BLANK
                mut_state[coords[0] - 1][coords[1]] = tile_of(action)
                mut_state[coords[0] - 1][coords[1] + 1] = tile_of(action)

            elif (direction_of(action) == 'DOWN'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 1] = BLANK
                mut_state[coords[0] + 2][coords[1]] = tile_of(action)
                mut_state[coords[0] + 2][coords[1] + 1] = tile_of(action)

            elif (direction_of(action) == 'LEFT'):
                mut_state[coords[0]][coords[1] + 1] = BLANK
                mut_state[coords[0] + 1][coords[1] + 1] = BLANK
                mut_state[coords[0]][coords[1] - 1] = tile_of(action)
                mut_state[coords[0] + 1][coords[1] - 1] = tile_of(action)

            elif (direction_of(action) == 'RIGHT'):
                mut_state[coords[0]][coords[1]] = BLANK
                mut_state[coords[0] + 1][coords[1]] = BLANK
                mut_state[coords[0]][coords[1] + 2] = tile_of(action)
                mut_state[coords[0] + 1][coords[1] + 2] = tile_of(action)
            else:
                print "result: Invalid direction passed."

        else:
            print "result: Invalid action/tile passed."

        return self.immutable_state(mut_state)

    def goal_test(self, state):
        """Return True if the state is a goal. In this case, the 2x2 'B' tile 
        must be centered at the bottom of the grid. This method checks for 
        that condition."""
        return state[3][1] == 'B' and state[3][2] == 'B' and state[4][1] == 'B' and state[4][2] == 'B'


    # returns True if the given action is impossible for the given state
    # must check border conflicts AND tile conflicts
    def has_conflict(self, state, action):
        conflicted = True
        
        tile = tile_of(action)
        direction = direction_of(action)

        if not self.has_edge_conflict(state, tile, direction):            # make sure no edge conflicts before checking for tile conflicts
            conflicted = self.has_tile_conflict(state, tile, direction)   
        return conflicted

    # checks edge conflict for given tile and direction
    def has_edge_conflict(self, state, tile, direction):
        conflicted = True

        if (direction == 'UP'):                             
            conflicted = self.tile_touches_top_edge(state, tile)

        elif (direction == 'DOWN'):
            conflicted = self.tile_touches_bottom_edge(state, tile)

        elif (direction == 'LEFT'):
            conflicted = self.tile_touches_left_edge(state, tile)
            
        elif (direction == 'RIGHT'):
            conflicted = self.tile_touches_right_edge(state, tile)

        else:
            print "has_border_conflict: invalid direction passed"

        return conflicted

    # checks tile conflict for given tile and direction
    def has_tile_conflict(self, state, tile, direction):
        conflicted = False

        if (direction == 'UP'):                             
            conflicted = self.has_tile_above(state, tile)

        elif (direction == 'DOWN'):
            conflicted = self.has_tile_below(state, tile)

        elif (direction == 'LEFT'):
            conflicted = self.has_tile_left(state, tile)
            
        elif (direction == 'RIGHT'):
            conflicted = self.has_tile_right(state, tile)

        else:
            print "has_tile_conflict: invalid direction passed"

        return conflicted

    def has_tile_above(self, state, tile):
        tile_above = True
        coords = self.get_coords(state, tile)

        if (tile in self.tiles_single or tile in self.tiles_vtwo):      # Single blocks or vertical 2s, fairly straightforward
            tile_above = (state[coords[0] - 1][coords[1]] != BLANK)

        elif (tile in self.tiles_htwo or tile in self.tiles_four):      # Horizontal 2s and four, check the other tile for a block above

            # print coords, tile
            # if (coords[1] >= 3):
            #     print_state(state)
            tile_above = (state[coords[0] - 1][coords[1]] != BLANK or state[coords[0] - 1][coords[1] + 1] != BLANK)              

        else:
            print "has_tile_above: Invalid tile passed."

        return tile_above

    def has_tile_below(self, state, tile):
        tile_below = True
        coords = self.get_coords(state, tile)

        if (tile in self.tiles_single):                                 # Single blocks, fairly straightforward
            tile_below = (state[coords[0] + 1][coords[1]] != BLANK)

        elif (tile in self.tiles_vtwo):                                 # Vertical 2s, tricky
            tile_below = (state[coords[0] + 2][coords[1]] != BLANK)

        elif (tile in self.tiles_htwo):                                 # Horizontal 2s, check the other tile for a block below
            tile_below = (state[coords[0] + 1][coords[1]] != BLANK or state[coords[0] + 1][coords[1] + 1] != BLANK)              
        
        elif (tile in self.tiles_four):
            tile_below = (state[coords[0] + 2][coords[1]] != BLANK or state[coords[0] + 2][coords[1] + 1] != BLANK)

        else:
            print "has_tile_below: Invalid tile passed."

        return tile_below

    def has_tile_left(self, state, tile):
        tile_left = True
        coords = self.get_coords(state, tile)

        if (tile in self.tiles_single or tile in self.tiles_htwo):      # Single blocks or horizontal 2, fairly straightforward
            tile_left = (state[coords[0]][coords[1] - 1] != BLANK)
        
        elif (tile in self.tiles_vtwo or tile in self.tiles_four):      # Vertical 2s and four, check the other tile for a block left
            tile_left = (state[coords[0]][coords[1] - 1] != BLANK or state[coords[0] + 1][coords[1] - 1] != BLANK)

        else:
            print "has_tile_left: Invalid tile passed"

        return tile_left

    def has_tile_right(self, state, tile):
        tile_right = True
        coords = self.get_coords(state, tile)

        if (tile in self.tiles_single):                                 # Single blocks, fairly straightforward
            tile_right = (state[coords[0]][coords[1] + 1] != BLANK)
        
        elif (tile in self.tiles_htwo):                                 # Horizontal 2, tricky
            tile_right = (state[coords[0]][coords[1] + 2] != BLANK)
        
        elif (tile in self.tiles_vtwo):                                 # Vertical 2s, check the other tile for a block left
            tile_right = (state[coords[0]][coords[1] + 1] != BLANK or state[coords[0] + 1][coords[1] + 1] != BLANK)

        elif (tile in self.tiles_four):
            tile_right = (state[coords[0]][coords[1] + 2] != BLANK or state[coords[0] + 1][coords[1] + 2] != BLANK)

        else:
            print "has_tile_right: Invalid tile passed"

        return tile_right

    # generate all possible combinations of actions, regardless of conflicts
    # should only need to run this once ideally
    def generate_all_actions(self, state):
        self.all_possible_actions = ((tile, direction) for tile in self.tiles(state) for direction in self.directions)
        return ((tile, direction) for tile in self.tiles(state) for direction in self.directions)

    # given a state, returns the list version of it
    def mutable_state(self, state):
        return [list(row) for row in state]

    # given a state, returns the tuple version of it
    def immutable_state(self, state):
        return tuple(tuple(row) for row in state)

    # given a state, returns all tiles present
    def tiles(self, state):
        tiles = []

        for row in state:
            for col in row:
                if col not in tiles:
                    tiles.append(col)

        tiles.remove(BLANK)
        return tuple(tiles)

    # given a state and a tile, returns the top left coords of the tile, row first
    def get_coords(self, state, tile):

        for row in range(len(state)):
            for col in range(len(state[row])):
                if (state[row][col] == tile):
                    return (row, col)

        return ()

    def tile_touches_top_edge(self, state, tile):                       
        return self.get_coords(state, tile)[0] == 0

    def tile_touches_left_edge(self, state, tile):
        return self.get_coords(state, tile)[1] == 0


    def tile_touches_bottom_edge(self, state, tile):                        #### TODO - Make sure these work for the big blocks
        touches = True

        coords = self.get_coords(state, tile)
        limit = len(state) - 1

        if (tile in self.tiles_single):                          # Single blocks, fairly straightforward
            touches = (coords[0] >= limit)

        elif (tile in self.tiles_vtwo):                          # VERTICAL 2x1 blocks, touching if displaced by 1
            touches = (coords[0] >= limit - 1)

        elif (tile in self.tiles_htwo):                          # HORIZONTAL 2x1 block, also straightforward
            touches = (coords[0] >= limit)

        elif (tile in self.tiles_four):                          # FOUR block, touching if displaced by 1
            touches = (coords[0] >= limit - 1)                  

        else:
            print "tile_touches_bottom_edge: Invalid tile passed."

        return touches
    

    def tile_touches_right_edge(self, state, tile):
        touches = True

        coords = self.get_coords(state, tile)
        limit = len(state[0]) - 1

        if (tile in self.tiles_single):                          # Single blocks, fairly straightforward
            touches = (coords[1] >= limit)

        elif (tile in self.tiles_vtwo):                          # VERTICAL 2x1 blocks, also straightforward
            touches = (coords[1] >= limit)

        elif (tile in self.tiles_htwo):                          # HORIZONTAL 2x1 block, also tricky
            touches = (coords[1] >= limit - 1)

        elif (tile in self.tiles_four):                          # FOUR block, touching if displaced by 1
            touches = (coords[1] >= limit - 1)

        else:
            print "tile_touches_right_edge: Invalid tile passed."

        return touches

#######################################

####### UTILITY FUNCTIONS #############

# pretty print state
def print_state(state):
    for row in state:
        print ' '.join(row).replace('X', '-')
    print ''

def tile_of (action):
    return action[0]

def direction_of (action):
    return action[1]


#######################################

####### WORK HORSE FUNCTION ###########
# This is the external interface.
# Given "search_type" of 'BFS', 'DFS', 'IDS', or 'BID'
# returns a list of actions which lead initial state to goal state
def huarong_pass_search(search_type):
    goal_actions = []

    hp = HuarongPass(initial_state)

    if search_type == 'BFS':
        print "Breadth first search..."
        goal_actions = search.breadth_first_search(hp).solution()

    elif search_type == 'DFS':
        print "Depth first search..."
        goal_actions = search.depth_first_graph_search(hp).solution()

    elif search_type == 'IDS':
        print "Iterative deepening search..."
        goal_actions = search.iterative_deepening_search(hp).solution()

    elif search_type == 'BID':
        print "Bidirectional search..."
        goal_actions = search.bidirectional_search(hp).solution()

    else:
        print "Invalid search_type given. Exiting..."

    return goal_actions




#######################################

hp = HuarongPass(initial_state)


######### TEST FUNCTIONS ##############

def audit_state(state):
    print_state(state)
    print "Available actions: ", hp.actions(state)
    print ''

def test_moves(tile):

    state = test_state[tile]
    audit_state(state)

    state = hp.result(state, (tile, 'UP'))
    audit_state(state)

    state = hp.result(state, (tile, 'LEFT'))
    audit_state(state)

    state = hp.result(state, (tile, 'UP'))
    audit_state(state)

    state = hp.result(state, (tile, 'RIGHT'))
    audit_state(state)

    state = hp.result(state, (tile, 'DOWN'))
    audit_state(state)

######### TESTING #####################

if DO_TESTING:

    print "Testing..."
    
    # print ''
    # print "Initial state:"
    # print_state(hp.initial)
    
    # print ''
    # print "Goal state:"
    # print_state(goal_state)


    # print hp.mutable_state(initial_state)
    # print_state(hp.mutable_state(initial_state))

    # print hp.immutable_state(hp.mutable_state(initial_state))
    # print_state(hp.immutable_state(hp.mutable_state(initial_state)))

    # for tile in hp.tiles:
    #     print hp.get_coords(initial_state, tile)

    # print "Possible actions from initial state:"
    # print hp.actions(initial_state)

    # print hp.tiles[6:10]
    # print hp.tiles_single
    # print hp.tiles_vtwo
    # print hp.tiles_htwo
    # print hp.tiles_four

    print ''

    assert hp.goal_test(goal_state) == True
    assert hp.goal_test(no_state) == False
    assert hp.goal_test(bogus_state) == False

    assert huarong_pass_search('x') == []
    assert huarong_pass_search(' ')  == []
    assert huarong_pass_search('')  == []


    # dfs_actions = huarong_pass_search('DFS')
    # print dfs_actions

    bfs_actions = huarong_pass_search('BFS')
    print bfs_actions
    
    # ids_actions = huarong_pass_search('IDS')
    # print ids_actions

    # bid_actions = huarong_pass_search('BID')
    # print bid_actions


    print ''
    print "All tests passed!"
    print ''


    # for tile in hp.tiles(initial_state):
    #     test_moves(tile)


    # state = initial_state

    # act1 = hp.actions(state)

    # for act in act1:
    #     print_state(hp.result(state, act))
    #     print hp.actions(hp.result(state, act))
    #     print ''

    # print hp.initial

    # states = [initial_state, bogus_state, no_state, testing_state, testing_state0, testing_state1]
    
    # for state in states:
    #     audit_state(state)

    
    # print_state(initial_state)
    # print_state(hp.result(initial_state, ('G', 'DOWN')))
    # print_state(hp.result(hp.result(initial_state, ('G', 'DOWN')), ('G', 'RIGHT')))
    # print_state(hp.result(hp.result(hp.result(initial_state, ('G', 'DOWN')), ('G', 'RIGHT')), ('H', 'LEFT')))
    # print_state(hp.result(hp.result(hp.result(hp.result(initial_state, ('G', 'DOWN')), ('G', 'RIGHT')), ('H', 'LEFT')), ('H', 'DOWN')))

    # state = hp.result(state, ('C', 'RIGHT'))
    # print_state(state)

    # state = hp.result(state, ('C', 'UP'))
    # print_state(state)

    # state = hp.result(state, ('C', 'LEFT'))
    # print_state(state)

    # state = hp.result(state, ('C', 'DOWN'))
    # print_state(state)

    # state = hp.result(state, ('E', 'RIGHT'))
    # print_state(state)

    # state = hp.result(state, ('E', 'DOWN'))
    # print_state(state)

    # state = hp.result(state, ('E', 'LEFT'))
    # print_state(state)

    # state = hp.result(state, ('E', 'UP'))
    # print_state(state)

    # print hp.tiles(testing_state)
    # print hp.tiles(initial_state)