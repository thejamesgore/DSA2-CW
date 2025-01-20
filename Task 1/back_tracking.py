import numpy as np
import time  # Need this to track how long we're taking

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
    path = []
    
    # We need a separate board to track visited squares
    visited = np.zeros((8, 8), dtype=bool)
    
    # Adding some counters to see what's happening
    attempts = 0
    start_time = time.time()
    
    # We need a way to make sure the knight can't go outside of our board
    # We can get board dimensions and ensure the tuples for the moves are within those bounds
    def is_possible_move(x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False
    
    # This helps us pick moves that are less likely to lead to dead ends
    def count_possible_moves(x, y):
        count = 0
        for dx, dy in knight_moves:
            next_x, next_y = x + dx, y + dy
            if is_possible_move(next_x, next_y) and not visited[next_x, next_y]:
                count += 1
        return count
    
    # Our recursive function that tries to find a valid tour
    def find_tour(current_x, current_y, move_count):
        nonlocal attempts
        attempts += 1
        
        # Print progress every million attempts
        if attempts % 1000000 == 0:
            elapsed = time.time() - start_time
            print(f"\nAttempts so far: {attempts}, Time: {elapsed:.2f}s")
            print(f"Currently at: ({current_x}, {current_y}), Move: {move_count}")
        
        # Add this position to our path and mark it as visited
        path.append((current_x, current_y))
        visited[current_x, current_y] = True
        
        # If we've visited all squares
        if move_count == 63:  # 63 moves = all 64 squares visited (counting from 0)
            if tour_type == "Open":
                return True
            else:  # Closed tour - check if we can get back to start
                start_x, start_y = path[0]
                for dx, dy in knight_moves:
                    final_x, final_y = current_x + dx, current_y + dy
                    if (final_x, final_y) == (start_x, start_y):
                        path.append((start_x, start_y))
                        return True
        
        # Get all possible next moves
        possible_moves = []
        for dx, dy in knight_moves:
            next_x, next_y = current_x + dx, current_y + dy
            if is_possible_move(next_x, next_y) and not visited[next_x, next_y]:
                # Count accessible squares from this position
                moves = count_possible_moves(next_x, next_y)
                possible_moves.append((moves, next_x, next_y))
        
        # Sort moves by number of future moves (fewer first - Warnsdorff's rule)
        possible_moves.sort()
        
        # Try each possible move
        for _, next_x, next_y in possible_moves:
            if find_tour(next_x, next_y, move_count + 1):
                return True
        
        # If no moves worked, backtrack
        visited[current_x, current_y] = False
        path.pop()
        return False
    
    # Try from corner positions first as they're often good starting points
    start_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
    start_positions.extend((x, y) for x in range(8) for y in range(8) 
                         if (x, y) not in start_positions)
    
    for start_x, start_y in start_positions:
        # Reset for new attempt
        path.clear()
        visited.fill(False)
        attempts_before = attempts  # Track attempts for this starting position
        
        print(f"\nTrying start position ({start_x}, {start_y})")
        if find_tour(start_x, start_y, 0):
            elapsed = time.time() - start_time
            print(f"Solution found starting from ({start_x}, {start_y})")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {elapsed:.2f} seconds")
            return path
        
        # Show attempts made from this starting position
        attempts_made = attempts - attempts_before
        print(f"No solution from ({start_x}, {start_y}) after {attempts_made} attempts")
    
    print(f"\nNo solution found after {attempts} total attempts")
    print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
    return None