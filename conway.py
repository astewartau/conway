'''Conway's Game of Life
Implemented by Ashley Stewart (22-05-2018)

a.stewart.au@gmail.com
Queensland University of Technology

This module contains several functions to demonstrate and run John Conway's Game
of Life. Read more: https://en.wikipedia.org/wiki/Conway_game

usage: python conway.py [-h] [-dims width height] [-timer [seconds]]

optional arguments:
  -h, --help            show this help message and exit
  -dims width height, -size width height
                        the size of the life grid
  -timer [seconds], -t [seconds]
                        indicates whether a timer should be used and the time
                        between generations (default 0.5s)

'''

import numpy as np
from scipy.signal import convolve2d

def build_life_grid(width, height, random_life=True):
    '''Build a life grid according using the given dimensions'''
    return np.array(
        np.random.random((width, height))*2 if random_life
        else np.zeros((width, height)),
        dtype = np.int
    )

def conway(cells):
    '''Progress the cells in Conway's Game of Life by one generation.

    Rules:
      1. Any live cell with fewer than two live neighbors dies, as if by 
         underpopulation
      2. Any live cell with two or three live neighbors lives on to the next
         generation
      3. Any live cell with more than three live neighbors dies, as if by
         overpopulation
      4. Any dead cell with exactly three live neighbors becomes a live cell, as
         if by reproduction

    Parameters
    ----------
    cells : np.ndarray
            a 2D array of cells of (1, 0) where 1 represents a living cell and 0
            represents a dead cell

    '''
    
    # kernal used to count cell neighbors
    kernel = np.ones((3, 3)); kernel[1][1] = 0
    
    # count cell neighbors
    n_neighbors = np.array(
        convolve2d(cells, kernel, mode='same'),
        dtype=np.int
    )

    # underpopulated cells die
    cells[n_neighbors < 2] = 0

    # overpopulated cells die
    cells[n_neighbors > 3] = 0

    # three neighbors reproduce
    cells[n_neighbors == 3] = 1

def display_conway(cells):
    '''Displays the given 2D grid of cells as block characters and spaces'''
    
    for row in cells:
        for cell in row:
            if cell:
                print('\u2588', end='')
            else:
                print(' ', end='')
        print()

def play_conway(cells, timer=None):
    '''Runs the game of life

    Parameters
    ----------
    cells : np.ndarray
            a 2D array of cells of (1, 0) where 1 represents a living cell and 0
            represents a dead cell
    timer : non-zero positive number
            if None, no timer will be used; the user presses RETURN to continue
            if a 
    '''
    
    # setup the action to occur between generations
    if timer:
        from time import sleep
        time_action = lambda: sleep(float(timer))
    else:
        time_action = lambda: input("Press ENTER to continue\n")

    # enable screen clearing for Windows and UNIX-like systems
    from os import system, name
    clear = lambda: system('cls' if name=='nt' else 'clear')

    # run life
    while True:
        try:
            clear()
            display_conway(cells)
            print("Press CTRL+C to quit")
            time_action()
            conway(cells)
        except KeyboardInterrupt:
            clear()
            display_conway(cells)
            print("Exiting")
            break
        
if __name__ == '__main__':
    def positive_int(x):
        '''Positive-integer only type'''
        x = int(x)
        if x <= 0:
            raise argparse.ArgumentTypeError("Minimum positive integer is 1")
        return x

    def positive_nonzero_float(x):
        '''Positive-float only type'''
        x = float(x)
        if x <= 0: raise argparse.ArgumentTypeError("Must be > 0")
        return x

    # parse command-line arguments
    import argparse
    parser = argparse.ArgumentParser('python conway.py')
    
    parser.add_argument(
        '-dims', '-size',
        nargs=2,
        metavar=('width', 'height'),
        default=(30, 30),
        dest='size',
        type=positive_int,
        help='the size of the life grid'
    )
    parser.add_argument(
        '-timer', '-t',
        nargs='?',
        metavar='seconds',
        const=0.5,
        default=None,
        dest='timer',
        type=positive_nonzero_float,
        help='indicates whether a timer should be used and the time between ' \
             'generations (default 0.5s)'
    )

    args = parser.parse_args()

    # start life
    play_conway(build_life_grid(*args.size), args.timer)
