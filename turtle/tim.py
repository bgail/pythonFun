# put all of your import statements below this line and then delete this comment
import turtle
import random
# put all of your function definitions below this line and then delete this comment


#==========================================================

def diamond(tim, length):
    
    tim.right(45)
    tim.forward(length)
    tim.right(45)
    tim.forward(length)
    tim.right(135)
    tim.forward(length)
    tim.right(45)
    tim.forward(length)
    
    
def flower(tim,length):
    


    for i in range(0,7):
        if(i==0):
            tim.color("red")
        elif(i==1):
            tim.color("yellow")
        elif(i==2):
            tim.color("green")
        elif(i==3):
            tim.color("blue")
        elif(i==4):
            tim.color("red")
        elif(i==5):
            tim.color("yellow")
        elif(i==6):
            tim.color("green")

        tim.begin_fill()
        diamond(tim,length)
        tim.end_fill()
        tim.right(135)
    else:
        tim.color("blue")
        tim.begin_fill()
        diamond(tim,length)
        tim.end_fill()
        tim.right(180)


def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    tim = turtle.Turtle()
    turtle.colormode(255)
    tim.speed(100)
    tim.pensize(4)
    flower(tim,180)
    flower(tim,120)
    flower(tim,80)
    flower(tim,50)
    

    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()