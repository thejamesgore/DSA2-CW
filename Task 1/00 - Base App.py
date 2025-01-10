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
    
main()
