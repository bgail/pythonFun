
import turtle




def triangle(tim):
    
    tim.right(55+180)
    tim.forward(10)
    tim.left(135)
    tim.forward(7)
    

def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    tim = turtle.Turtle()
    # put main code here, make sure each line is indented one level, and delete this comment
    tim.speed(0)
    tim.pensize(4)

    turtle.colormode(255)

    tim.color(132,148,95)

    tim.pencolor("black")

    tim.penup()
    tim.goto(-220,220)
    tim.pendown()
    tim.begin_fill()
    tim.circle(45)

    tim.end_fill()

    tim.begin_fill()
    tim.forward(200)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(200)
    tim.right(90)
    tim.forward(100)
    tim.end_fill()


    tim.begin_fill()
    tim.backward(60)
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.forward(10)
    tim.left(90)
    tim.forward(60)
    tim.left(90)
    tim.forward(10)
    tim.left(90)
    tim.forward(30)
    tim.end_fill()


    tim.penup()
    tim.goto(-100,145)
    tim.begin_fill()
    tim.pendown()
    tim.circle(36)
    tim.end_fill()

    tim.penup()
    tim.goto(-115,100)
    tim.pendown()
    tim.begin_fill()
    tim.left(45)
    tim.forward(20)
    tim.left(90)
    tim.forward(70)
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(70)
    tim.end_fill()

    tim.penup()
    tim.goto(-82, 33)
    tim.pendown()
    tim.begin_fill()
    tim.left(45)
    tim.forward(50)
    tim.left(90)
    tim.forward(15)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(15)
    tim.end_fill()

    tim.penup()
    tim.goto(-20,120)
    tim.pendown()
    tim.begin_fill()
    tim.right(90)
    tim.forward(100)
    tim.left(150)
    tim.forward(115)
    tim.end_fill()

    tim.penup()
    tim.goto(-225, 250)
    tim.pendown()
    tim.left(30)
    tim.forward(35)


    tim.penup()
    tim.goto(-235, 295)
    # tim.right(180)
    tim.pendown()
    tim.circle(10)

    tim.penup()
    tim.goto(-260,250)
    tim.pendown()
    triangle(tim)
    tim.left(101)
    triangle(tim)
    tim.left(101)
    triangle(tim)
    tim.left(101)
    triangle(tim)
    tim.left(101)
    triangle(tim)

    tim.penup()
    tim.goto(0,0)

    


    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
