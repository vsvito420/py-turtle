import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # Turn off screen updates for smoother animation

# Turtle setup
pen = turtle.Turtle()
pen.speed(0) # Fastest speed
pen.hideturtle()
pen.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    pen.pencolor(colors[i % len(colors)])
    pen.width(i / 100 + 1)
    pen.forward(i)
    pen.left(59)
    screen.update() # Update screen manually
    # time.sleep(0.01) # Optional: slow down the animation

screen.mainloop() # Keep the window open
