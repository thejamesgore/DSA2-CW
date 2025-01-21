import numpy as np
import random

def las_vegas(tour_type):
    """
    Las Vegas approach to solving the Knights Tour
    """
    
    if tour_type == "1":
        tour_type = "Open"
    else:
        tour_type = "Closed"
        
    print("Tour type is", tour_type)
    
    # As with our original set of test moves, these are the only types of moves a knight can actually do.
    # This is what allows the L shape move in all directions
    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # We'll keep track of the path taken so we can return it to our board visualiser
    path = []
    
    # We need a separate board to track visited squares
    visited = np.zeros((8, 8), dtype=bool)
    
    # We need a way to make sure the knight can't go outside of our board
    def is_possible_move(x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False
    
    # Added this to help see what's happening on the board
    # V means we've visited that square, . means we haven't
    def print_board_state():
        for i in range(8):
            for j in range(8):
                if visited[i][j]:
                    print('V', end=' ')
                else:
                    print('.', end=' ')
            print()  # New line after each row
        print()  # Extra line after board

    return None