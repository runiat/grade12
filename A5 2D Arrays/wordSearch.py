# modified from http://programarcadegames.com/index.php?chapter=example_code
# Name:
# Date:

import random

# Create a grid filled with "." representing a blank
def createGrid():
    grid=[]
    for row in range(15):
        grid.append([])
        for column in range(30):
            grid[row].append(".")
    return grid

# Print the grid to the screen
def printGrid(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            print(grid[row][column],end="")
        print()

# You decide what paramaters you want to use
def printGridToFile():
    '''
    :param
    :param
    :return: None. but create an output file with the wordsearch and list of words to find
    '''
    # write your code here


# Try to place the word. Return True if successful
# False if it failed and we need to try again.
def tryToPlaceWord(grid,word):
    # Figure out the direction of the work.
    # Change the 8 to a 7 if you don't want backwards
    # words.
    direction=random.randrange(0,8)
    if( direction == 0 ):
        x_change=-1
        y_change=-1
    if( direction == 1 ):#(up)
        x_change = 0
        y_change = 1
    if( direction == 2 ):
        x_change=1
        y_change=-1
    if( direction == 3 ): #forwards (right)
        x_change=1
        y_change=0
    if( direction == 4 ):
        x_change=1
        y_change=1
    if( direction == 5 ):
        x_change=0
        y_change=1
    if( direction == 6 ):
        x_change=-1
        y_change=1
    if( direction == 7 ): #backwards (left)
        x_change=-1
        y_change=0

    # Find the length and height of the grid
    height=len(grid)
    width=len(grid[0])

    # Create a random start point
    column=random.randrange(width)
    row=random.randrange(height)

    # Check to make sure  the word won't run off the edge of the grid.
    # If it does, return False. We failed.
    if( x_change < 0 and column < len(word) ):
        return False
    if( x_change > 0 and column > width-len(word) ):
        return False
    if( y_change < 0 and row < len(word) ):
        return False
    if( y_change > 0 and row > height-len(word) ):
        return False

    # Now check to make sure there isn't another letter in our way
    current_column=column
    current_row=row
    for letter in word:
        # Make sure it is blank, or already the correct letter.
        if grid[current_row][current_column]==letter or grid[current_row][current_column]=='.':
            current_row += y_change
            current_column += x_change
        else:
            # Oh! A different letter is already here. Fail.
            return False

    # Everything is good so far, actually place the letters.
    current_column=column
    current_row=row
    for letter in word:
        grid[current_row][current_column]=letter
        current_row += y_change
        current_column += x_change
    return True

# This just calls tryToPlaceWord until we succeed. It could
# repeat forever if there is no possible place to put the word.
def placeWord(grid,word):
    success=False

    while not(success):
        success=tryToPlaceWord(grid,word)

def fillGrid(grid):
    '''
    Call this when finished adding all words. This method will replace every "." and change it to be a random letter.
    :return: None
    '''

    # go through each element in the 2Darray. if it doesnt have a letter, put in arandom letter.



def main():
    # Create an empty grid
    grid = createGrid()

    words=["pandabear","fish","snake","porcupine","dog","cat","tiger","alligator","dolphin","Angela", "Computer","snow"]

    # Place some words
    for i in range(len(words)):
        placeWord(grid,words[i])

    # fill in the grid
    fillGrid(grid)

    # Print it out
    printGrid(grid)

main()