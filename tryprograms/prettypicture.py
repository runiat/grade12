import turtle


def draw_fractal(length, depth,t):
    #first line
    if depth==1:   t.forward(length)
    else:    draw_fractal(length,depth-1,t)
    t.right(60)
    #second line
    if depth==1:    t.forward(length)
    else:   draw_fractal(length,depth-1,t)
    t.left(120)
    # third line
    if depth==1:    t.forward(length)
    else:    draw_fractal(length,depth-1,t)
    t.right(60)
    # fourth line
    if depth==1:    t.forward(length)
    else:    draw_fractal(length,depth-1,t)



def draw_snowflake(length, depth, t):
    # draw three fractals in a "triangle" to make a snowflake
    draw_fractal(length, depth-1, t)
    t.left(120)
    draw_fractal(length, depth-1, t)
    t.left(120)
    draw_fractal(length, depth-1, t)
    t.left(120)

def floor(x,y):
    # return the smaller of x and y. Keep the type the same.
    if x<y : return x
    else: return y


# not working yet.
def draw_fern(length1,angle1,length2,angle2,depth,t):
    '''
    :param length1: stem length
    :param angle1:stem-leaf angle
    :param length2:
    :param angle2: stem-curve angle
    :param depth:
    :param t:
    :return: None
    '''
    flip=1
    for i in range(length2):
        t.left(angle2)
        t.forward(length1)

        if depth>1:
            t.left(angle1*flip)
            # length1 becomes 1 or length1/3-i/2.
            # legnth2 becomes 1 or length2-i
            # angle 1 and angle2 flip, decrease depth
            draw_fern(floor((length1/3)-(i/2),1),angle1*flip, floor(length2-i,1) , angle2*flip, depth-1,t)
            t.left(180-angle1*flip)
        flip*=-1

    t.left(180)

    for i in range(length2):
        t.forward(length1)
        t.right(angle2)





def main():
    t=turtle.Turtle()
    wn=turtle.Screen()
    # setup the turtle
    t.speed(0)
    t.up()
    t.goto(-100,0)
    t.down()
    t.left(90)


    #call recursive function
    draw_fern(80,70,10,6,1,t)


    wn.exitonclick()

main()