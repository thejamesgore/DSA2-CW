import numpy as np
import random
import time  # Need this to track how long we're taking

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
    
    # Adding some counters to see what's happening
    attempts = 0
    successful_attempts = 0
    start_time = time.time()
    
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

    def try_random_tour(start_x, start_y):
        nonlocal attempts, successful_attempts, path, visited
        attempts += 1
        
        # Reset for new attempt
        path = [(start_x, start_y)]
        visited.fill(False)
        visited[start_x, start_y] = True
        current_x, current_y = start_x, start_y
        moves_made = 0
        
        # Keep making moves until we finish or fail
        while moves_made < 63:
            dx, dy = random.choice(knight_moves)
            next_x, next_y = current_x + dx, current_y + dy
            
            # If we're off the board or hit visited square - that's a fail
            if not is_possible_move(next_x, next_y):
                continue  # Try another random move
            if visited[next_x, next_y]:
                return False  # Hit visited square - Las Vegas failure condition
            
            # Make the move
            current_x, current_y = next_x, next_y
            path.append((current_x, current_y))
            visited[current_x, current_y] = True
            moves_made += 1
        
        # If we're doing a closed tour, check if we can get back
        if tour_type == "Closed":
            for dx, dy in knight_moves:
                final_x, final_y = current_x + dx, current_y + dy
                if (final_x, final_y) == (start_x, start_y):
                    path.append((start_x, start_y))
                    successful_attempts += 1
                    return True
            return False
        
        successful_attempts += 1
        return True

    # Try from starting position (0,0) initially
    while attempts < 1000000:  # Set a reasonable limit
        if try_random_tour(0, 0):
            elapsed = time.time() - start_time
            print(f"\nFound a solution!")
            print(f"Total attempts: {attempts:,}")
            print(f"Success rate: {(successful_attempts/attempts)*100:.2f}%")
            print(f"Time taken: {elapsed:.2f} seconds")
            return path
    
    print(f"\nNo solution found")
    print(f"Total attempts: {attempts:,}")
    print(f"Success rate: {(successful_attempts/attempts)*100:.2f}%")
    return None