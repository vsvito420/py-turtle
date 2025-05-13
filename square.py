import turtle

# Erstelle ein Turtle-Objekt
t = turtle.Turtle()

# Geschwindigkeit setzen (1: langsam, 10: schnell)
t.speed(5)

# Stiftfarbe und -dicke setzen
t.pencolor("blue")
t.pensize(3)

# Zeichne ein Quadrat
for _ in range(4):
    t.forward(100)  # 100 Pixel vorwärts bewegen
    t.right(90)     # 90 Grad nach rechts drehen

# Halte das Fenster offen, bis es geschlossen wird
turtle.exitonclick()