"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""


"""
This week we will look at adding a lake that doesn't move in the middle of the forest. 
The lake is blue and will not catch on fire.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22
#I arbitrarily decided to make the lake about 1/3 the height and width of 
#the screen. I will add 1/6 the width and height to both sides of the 
#center point of the screen to make the lake.
LAKE_HALF_WIDTH = int(WIDTH/6)
LAKE_HALF_HEIGHT = int(HEIGHT/6)
APPROX_CENTER_WIDTH = int(WIDTH/2)
APPROX_CENTER_HEIGHT = int(HEIGHT/2)

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W' #add a new constant for water

INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

PAUSE_LENGTH = 0.5

# nothing changed in the main function
def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    #make the lake in the middle of the screen.
    #maybe I should have used shorter variable names?
    for x in range(APPROX_CENTER_WIDTH-LAKE_HALF_WIDTH, APPROX_CENTER_WIDTH+LAKE_HALF_WIDTH):
        for y in range(APPROX_CENTER_HEIGHT-LAKE_HALF_HEIGHT, APPROX_CENTER_HEIGHT+LAKE_HALF_HEIGHT):
            forest[(x,y)] = WATER
        
    #add an extra if statement to make sure we don't change the water to trees
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x,y) in forest: #if (x,y) already exists, it is water, so don't change it
                continue
            else:
                if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                    forest[(x, y)] = TREE  # Start as a tree.
                else:
                    forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            #add an elif statement to display the water
            elif forest[(x,y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
          	
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
