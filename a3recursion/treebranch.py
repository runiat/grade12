# Name:
# Date:
# This function will draw a beautiful picture of a tree recursivly using turtle.

import turtle

def tree(branchLen,t):
    ''' This recursice function will draw a tree recursivly.
    :param branchLen: an int. the length of a branch
    :param t:  the turtle object
    :return: None
    '''
    #base case. stop drawing if the branch length is less than 5

    #recursive case: if branch length is more than 5, go forward, draw the right and left side and go back
    if branchLen > 5:
        # go forwarda
        t.forward(branchLen)
        # draw a tree on the right side
        t.right(20)
        tree(branchLen-15,t)
        # draw a tree on the left
        t.left(40)
        tree(branchLen-15,t)
        # move the turtle back to the starting position
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    # move the position of the turtle down by 100
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    # call the tree function
    tree(75,t)
    myWin.exitonclick()

main()


'''
Self Check: ***************TRY THESE**********
Modify the recursive tree program using one or all of the following ideas:

Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.
'''