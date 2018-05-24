# Conway's Game of Life in Python

This module contains several functions to demonstrate and run John Conway's Game
of Life. Simply [download the Python file](https://raw.githubusercontent.com/astewartau/conway/master/conway.py)
and run it with the usage described below.

Read more: https://en.wikipedia.org/wiki/Conway_game

# Dependencies
Requires numpy and scipy. These can be installed via:

    python -m pip install numpy scipy

# Usage
    usage: python conway.py [-h] [-dims width height] [-timer [seconds]]

    optional arguments:
      -h, --help            show this help message and exit
      -dims width height, -size width height
                            the size of the life grid
      -timer [seconds], -t [seconds]
                            indicates whether a timer should be used and the time
                            between generations (default 0.5s)
                            
# Video
![Video](https://raw.githubusercontent.com/astewartau/conway/master/output.gif)
