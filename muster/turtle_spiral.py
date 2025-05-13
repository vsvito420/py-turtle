import turtle
import time

# Bildschirm einrichten
bildschirm = turtle.Screen()
bildschirm.setup(width=600, height=600)
bildschirm.bgcolor("black")
bildschirm.tracer(0) # Bildschirmaktualisierungen für sanftere Animation ausschalten

# Stift einrichten
stift = turtle.Turtle()
stift.speed(0) # Schnellste Geschwindigkeit
stift.hideturtle()
stift.pensize(20)

farben = ["red", "orange", "yellow", "green", "blue", "purple"] # Farben bleiben Englisch für turtle-Kompatibilität

for i in range(360):
    stift.pencolor(farben[i % len(farben)])
    stift.width(i / 100 + 1)
    stift.forward(i)
    stift.left(59)
    bildschirm.update() # Bildschirm manuell aktualisieren
    # time.sleep(0.01) # Optional: Animation verlangsamen

bildschirm.mainloop() # Fenster offen halten
