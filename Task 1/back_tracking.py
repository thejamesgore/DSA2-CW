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
    def is_possible_move(x,y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    # We make the chess board again
    chessboard = np.zeros((8, 8))
    chessboard[::2, ::2] = 1  
    chessboard[1::2, 1::2] = 1 

    # We do the next move helper function
    def next_move(x,y):
        path.append((x,y)) # We add the move to the path we've taken so we can return it to our visualiser
        chessboard[x,y] = True # For the square visited we change it to True to indicate we've landed there
        
        # Next we work out from where we are on the board what moves are even available to us in this moment.
        available_moves = []
        
        for dx, dy in knight_moves:
            next_x, next_y = x + dx, y + dy # from current position we add the next potential move dimensions   
            if is_possible_move(next_x, next_y) and not chessboard[next_x, next_y]:
                available_moves.append((next_x, next_y))  # Add valid unvisited moves to the list
        
        # Debugging to see if this actually works
        # print(f"Current position: ({x}, {y})")
        # print(f"Path so far: {path}")
        # print(f"Available moves: {available_moves}")
        
        # Return the list of valid moves
        return available_moves
    
    