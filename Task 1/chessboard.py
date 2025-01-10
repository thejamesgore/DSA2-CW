import numpy as np
import matplotlib.pyplot as mp

def show_chessboard():
    # we use numpy to create the dimensions of the board 8x8 and then use slice to make the rows and columns
    chessboard = np.zeros((8, 8))
    chessboard[::2, ::2] = 1  
    chessboard[1::2, 1::2] = 1

    # This shows the board on screen
    mp.imshow(chessboard)
    mp.show()