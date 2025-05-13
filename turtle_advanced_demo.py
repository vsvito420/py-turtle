import turtle
import random
import math

# Screen-Setup
screen = turtle.Screen()
screen.title("Python Turtle - Fortgeschrittene Demo")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)  # Deaktiviert automatisches Bildschirm-Update für bessere Performance

# Farbliste für zufällige Farbauswahl
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "cyan"]

# Funktion zum Erstellen einer neuen Turtle mit bestimmten Eigenschaften
def create_turtle(shape="turtle", color="white", speed=0):
    t = turtle.Turtle()
    t.hideturtle()
    t.shape(shape)
    t.color(color)
    t.speed(speed)  # 0 ist die schnellste Geschwindigkeit
    t.penup()
    return t

# 1. DEMO: SPIRALE MIT FARBWECHSEL
def draw_colorful_spiral():
    spiral_turtle = create_turtle(color="red")
    spiral_turtle.goto(0, 0)
    spiral_turtle.showturtle()
    spiral_turtle.pendown()
    
    spiral_turtle.width(2)
    size = 1
    
    # Zeichne eine Spirale mit wechselnden Farben
    for i in range(100):
        spiral_turtle.color(colors[i % len(colors)])
        spiral_turtle.forward(size)
        spiral_turtle.right(45)
        size += 0.5
    
    spiral_turtle.hideturtle()

# 2. DEMO: STERN MIT FÜLLUNG
def draw_filled_star(points=5, size=100, x=0, y=0):
    star_turtle = create_turtle(color="yellow")
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.begin_fill()
    
    # Berechne den Winkel für einen Stern
    angle = 180 - (180 / points)
    
    # Zeichne einen Stern
    for _ in range(points):
        star_turtle.forward(size)
        star_turtle.right(angle)
    
    star_turtle.end_fill()
    star_turtle.penup()

# 3. DEMO: MEHRERE TURTLES UND STAMPS
def draw_turtle_circle():
    stamp_turtle = create_turtle(shape="turtle", color="green")
    
    # Positioniere die Turtle und mache sie sichtbar
    stamp_turtle.goto(0, -150)
    stamp_turtle.showturtle()
    
    # Stamping: Hinterlasse Turtle-Stempel in einem Kreis
    for angle in range(0, 360, 30):
        stamp_turtle.goto(150 * math.sin(math.radians(angle)), 
                       -150 + 150 * math.cos(math.radians(angle)))
        stamp_turtle.setheading(angle)
        stamp_turtle.stamp()
    
    stamp_turtle.goto(0, -150)
    stamp_turtle.hideturtle()

# 4. DEMO: TEXT UND PUNKTE
def draw_text_and_dots():
    text_turtle = create_turtle(color="white")
    text_turtle.goto(0, 200)
    
    # Schreibe Text
    text_turtle.write("Python Turtle Demo", align="center", 
                   font=("Arial", 24, "bold"))
    
    # Zeichne einige zufällige Punkte
    for _ in range(50):
        text_turtle.goto(random.randint(-350, 350), random.randint(-250, 250))
        text_turtle.dot(random.randint(5, 15), random.choice(colors))

# 5. DEMO: BENUTZERDEFINIERTE FORM UND ANIMATION
def create_custom_shape():
    # Erstelle eine eigene Form (Rhombus)
    shape_coords = ((0, 0), (10, 10), (0, 20), (-10, 10))
    screen.register_shape("rhombus", shape_coords)
    
    custom_turtle = create_turtle(shape="rhombus", color="cyan")
    custom_turtle.showturtle()
    custom_turtle.goto(-200, 0)
    custom_turtle.pendown()
    
    # Einfache Animation der benutzerdefinierten Form
    positions = [(-200, 0), (-100, 50), (0, 0), (100, 50), (200, 0)]
    
    for pos in positions:
        custom_turtle.goto(pos)
        screen.update()  # Manuelles Update des Bildschirms
        turtle.delay(100)  # Kurze Pause
    
    custom_turtle.penup()
    custom_turtle.hideturtle()

# 6. DEMO: INTERAKTIVES ZEICHNEN MIT PFEILTASTEN
def setup_interactive_turtle():
    # Erstelle eine Turtle, die durch Pfeiltasten gesteuert werden kann
    interactive_turtle = create_turtle(color="purple")
    interactive_turtle.showturtle()
    interactive_turtle.goto(0, 0)
    interactive_turtle.pendown()
    interactive_turtle.width(3)
    
    # Definiere Funktionen für Tastatursteuerung
    def move_forward():
        interactive_turtle.forward(10)
        screen.update()
    
    def move_backward():
        interactive_turtle.backward(10)
        screen.update()
    
    def turn_left():
        interactive_turtle.left(15)
        screen.update()
    
    def turn_right():
        interactive_turtle.right(15)
        screen.update()
    
    def change_color():
        interactive_turtle.color(random.choice(colors))
        screen.update()
    
    def toggle_pen():
        if interactive_turtle.isdown():
            interactive_turtle.penup()
        else:
            interactive_turtle.pendown()
        screen.update()
    
    # Tastenbindungen einrichten
    screen.listen()
    screen.onkey(move_forward, "Up")
    screen.onkey(move_backward, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(change_color, "space")
    screen.onkey(toggle_pen, "p")
    
    # Anweisungen anzeigen
    instruction_turtle = create_turtle(color="white")
    instruction_turtle.goto(0, -250)
    instructions = "Pfeiltasten: Bewegen | Leertaste: Farbe ändern | p: Stift umschalten"
    instruction_turtle.write(instructions, align="center", font=("Arial", 12, "normal"))

# Hauptprogramm
def main():
    # Führe alle Demos nacheinander aus
    draw_text_and_dots()
    screen.update()
    
    draw_filled_star(points=5, size=100, x=-200, y=0)
    screen.update()
    
    draw_filled_star(points=8, size=70, x=200, y=0)
    screen.update()
    
    draw_colorful_spiral()
    screen.update()
    
    draw_turtle_circle()
    screen.update()
    
    create_custom_shape()
    
    # Interaktives Zeichnen zum Schluss
    setup_interactive_turtle()
    
    # Aktiviere Event-Loop und halte das Fenster offen
    screen.update()
    turtle.delay(100)
    print("Interaktiver Modus: Nutze die Pfeiltasten zum Zeichnen!")
    print("- Pfeiltasten: Bewegung")
    print("- Leertaste: Farbe ändern")
    print("- p: Stift ein-/ausschalten")
    screen.mainloop()

# Starte das Programm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()