import numpy as np
import matplotlib.pyplot as mp

def show_chessboard():
    # we use numpy to create the dimensions of the board with an array of arrays 8x8 and then use slice to make the rows and columns
    chessboard = np.zeros((8, 8))
    chessboard[::2, ::2] = 1  # we assign the value of 1 to every over element of our array starting at index 0
    chessboard[1::2, 1::2] = 1 # We do the same starting at index 1 on the lines filling the rest of the board

    # This shows the board on screen
    mp.imshow(chessboard)
    mp.show()