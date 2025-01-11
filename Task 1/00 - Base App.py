"""
    Knights Tour Visualiser

    This is the solution to Task 1 and main program which takes 
    the user input and decides what functions shall be called
    to provide the relevant solutions
"""

from chessboard import show_chessboard
from las_vegas import las_vegas

def main():

    # This is a helper function that ensures a user always enters a 1 or a 2 otherwise program will error out 
    def get_valid_input(prompt):
        while True:
            choice = input(prompt).strip()
            if choice in ('1', '2'):
                return choice
            print("Invalid input. Please enter 1 or 2.")

    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Welcome to the Knights Tour visualiser!")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Choose your method of solving the Knights Tour:")
    print("")
    print("(1) Open Tour OR (2) Closed Tour")
    print("")
    tour_type = get_valid_input("Type your choice (1) or (2): ") 
    
    print("")
    print("Choose the method we will use to solve this problem:")
    print("")
    print("(1) Backtracking method OR (2) Las Vegas method")
    print("")
    method = get_valid_input("Type your choice (1) or (2): ")

    tour_run = ""
    
    if method == "1":
        print("Lets try the Backtracking approach.")
        if tour_type == "1":
            print("With an Open Tour.")
            print("")
            print("Visualising board...")
        else:
            print("With a Closed Tour.")
            print("")
            print("Visualising board...")
        tour_run = backtracking
        
    
    if method == "2":
        print("Lets try the Las Vegas approach. Visualising board....")
        if tour_type == "1":
            print("With an Open Tour.")
            print("")
            print("Visualising board...")
        else:
            print("With a Closed Tour.")
            print("")
            print("Visualising board...")
        tour_run = las_vegas
    
    moves = [(0, 0), (2, 1), (4, 2), (6, 3), (5, 5), (3, 6), (1, 7)]
    show_chessboard(moves)
    
main()
