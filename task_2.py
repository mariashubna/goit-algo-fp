import turtle
import math

def draw_pythagoras_tree(t, branch_length, depth):
    if depth == 0:
        return

    t.forward(branch_length)
    position = t.position()
    heading = t.heading()
    
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, depth - 1)
    
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()
    
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, depth - 1)
    
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    
    depth = int(screen.numinput("Input", "Enter the recursion depth:", minval=1, maxval=10))
    
    draw_pythagoras_tree(t, 100, depth)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
