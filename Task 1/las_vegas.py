import numpy as np
import random
import time  # Need this to track how long we're taking

def get_attempt_limit():
    while True:
        print("\nSelect number of attempts per starting position:")
        print("1: 100,000 attempts (low chance of success)")
        print("2: 1,000,000 attempts")
        print("3: 10,000,000 attempts (Could take quite some time...")
        choice = input("Enter your choice - 1 2, 3 or 4: ").strip()
        
        if choice in ['1', '2', '3', '4']:
            attempts = {
                '1': 10000,
                '2': 100000,
                '3': 1000000,
                '4': 10000000
            }[choice]
            print(f"\nUsing {attempts:,} attempts per starting position")
            return attempts
        print("Please enter 1, 2, 3, or 4")

def las_vegas(tour_type):
    """
    Las Vegas approach to solving the Knights Tour
    """
    
    if tour_type == "1":
        tour_type = "Open"
    else:
        tour_type = "Closed"
        
    print("Tour type is", tour_type)
    
    # Get attempt limit from user
    max_attempts_per_start = get_attempt_limit()
    
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
        
        # Show progress every 5% of max attempts
        progress_interval = max(max_attempts_per_start // 20, 10000)
        if attempts % progress_interval == 0:
            elapsed = time.time() - start_time
            print(f"\nAttempts: {attempts:,}, Success Rate: {(successful_attempts/attempts)*100:.2f}%")
            print(f"Time: {elapsed:.2f}s")
            print("Current board state:")
            print_board_state()
            
            # Check if we should move to next square
            if attempts % max_attempts_per_start == 0:
                print(f"\nReached {max_attempts_per_start:,} attempts. Moving to next square...")
                return None
        
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

    def try_from_position(start_x, start_y):
        print(f"\nTrying from ({start_x}, {start_y})")
        print("Initial board state:")
        print_board_state()
        
        attempts_this_start = 0
        while attempts_this_start < max_attempts_per_start:
            result = try_random_tour(start_x, start_y)
            
            # Check if we should move to next square
            if result is None:
                return False
            
            # Check if we found a solution
            if result:
                elapsed = time.time() - start_time
                print(f"\nFound a solution!")
                print(f"Starting position: ({start_x}, {start_y})")
                print(f"Total attempts: {attempts:,}")
                print(f"Success rate: {(successful_attempts/attempts)*100:.2f}%")
                print(f"Time taken: {elapsed:.2f} seconds")
                print("Final board state:")
                print_board_state()
                return True
            
            attempts_this_start += 1
        
        return False

    # Try corners first
    print("\nTrying corner positions first...")
    corner_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for start_x, start_y in corner_positions:
        if try_from_position(start_x, start_y):
            return path
    
    # Then try center positions
    print("\nNo solution from corners. Trying center positions...")
    center_positions = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for start_x, start_y in center_positions:
        if try_from_position(start_x, start_y):
            return path
    
    # If still no solution, systematically try every other square
    print("\nNo solution from corners or center. Trying all remaining squares...")
    for x in range(8):
        for y in range(8):
            # Skip if it was a corner or center we already tried
            if (x, y) in corner_positions or (x, y) in center_positions:
                continue
                
            if try_from_position(x, y):
                return path
    
    print(f"\nNo solution found after trying all squares")
    print(f"Total attempts: {attempts:,}")
    print(f"Final success rate: {(successful_attempts/attempts)*100:.2f}%")
    print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
    print("Final board state:")
    print_board_state()
    return None