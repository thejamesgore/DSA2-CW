import numpy as np
import matplotlib.pyplot as mp

def show_chessboard(moves):
    # we use numpy to create the dimensions of the board with an array of arrays 8x8 and then use slice to make the rows and columns
    chessboard = np.zeros((8, 8))
    print(chessboard)
    chessboard[::2, ::2] = 1  # we assign the value of 1 to every over element of our array starting at index 0
    chessboard[1::2, 1::2] = 1 # We do the same starting at index 1 on the lines filling the rest of the board

    # We then take the move sequence, moves, and then in order plot them out in order
    x_coords, y_coords = zip(*moves)
    for i, (x, y) in enumerate(moves):
        mp.text(y, x, str(i + 1), color="white", ha="center", va="center", fontsize=8)
    mp.plot(y_coords, x_coords, color="orange", linewidth=4, marker="o")

    # This shows the board on screen
    mp.imshow(chessboard)
    mp.show()