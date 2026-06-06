"""
Write a robot simulator.

A robot factory's test facility needs a program to verify robot movements.

The robots have three possible movements:

    - turn right (R)
    - turn left (L)
    - advance (A)

"""

# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    
    def move(self, letters):
        moves = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0)
        }
        
        for letter in letters:
            if letter == "A":
                dx, dy = moves[self.direction]
                self.x_pos += dx
                self.y_pos += dy
            if letter == "R":
                self.direction = (self.direction + 1) % 4 
            if letter == "L":
                self.direction  = (self.direction - 1) % 4 
                