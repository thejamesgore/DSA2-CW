import numpy as np

def back_tracking(tour_type):
    """
    Backtracking approach to solving the Knights Tour
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
    path =[]
    # We will also need to know if we've hit every square on the board somehow
    
    # We need a way to make sure the knight can't go outside of our board
    # We can get board dimensions and ensure the tuples for the moves are within those bounds
    # This may mean also tracking where the knight is on a 2D array of the board
    def is_possible_move(x,y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    # We make the chess board again
    chessboard = np.zeros((8, 8))
    chessboard[::2, ::2] = 1  
    chessboard[1::2, 1::2] = 1 

