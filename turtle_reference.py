# Python Turtle Referenz - Übersicht aller wichtigen Features
# =========================================================

"""
Diese Datei dient als Referenz für die wichtigsten Features des Python Turtle-Moduls,
kategorisiert nach Funktionalität.
"""

import turtle

# Beispiel für ein einfaches Setup (Auskommentiert, damit die Datei nicht automatisch ein Fenster öffnet)
# screen = turtle.Screen()
# t = turtle.Turtle()

# ----------------------------------------
# KATEGORIE 1: BEWEGUNGSBEFEHLE
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| forward(d)       | Bewegt Turtle d Einheiten vorwärts| t.forward(100)         |
| fd(d)            | Kurzform für forward()            | t.fd(100)              |
| backward(d)      | Bewegt Turtle d Einheiten rückwärts| t.backward(100)       |
| bk(d)            | Kurzform für backward()           | t.bk(100)              |
| right(angle)     | Dreht Turtle um angle Grad rechts | t.right(90)            |
| rt(angle)        | Kurzform für right()              | t.rt(90)               |
| left(angle)      | Dreht Turtle um angle Grad links  | t.left(90)             |
| lt(angle)        | Kurzform für left()               | t.lt(90)               |
| goto(x, y)       | Bewegt Turtle zur Position (x,y)  | t.goto(50, 50)         |
| setx(x)          | Setzt x-Koordinate                | t.setx(100)            |
| sety(y)          | Setzt y-Koordinate                | t.sety(100)            |
| setheading(angle)| Setzt Ausrichtung auf angle Grad  | t.setheading(90)       |
| seth(angle)      | Kurzform für setheading()         | t.seth(90)             |
| home()           | Bewegt Turtle zur Position (0,0)  | t.home()               |
| circle(radius)   | Zeichnet Kreis mit Radius radius  | t.circle(50)           |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 2: ZEICHENSTIL-BEFEHLE
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| pendown()        | Aktiviert den Zeichenstift        | t.pendown()            |
| pd()             | Kurzform für pendown()            | t.pd()                 |
| penup()          | Deaktiviert den Zeichenstift      | t.penup()              |
| pu()             | Kurzform für penup()              | t.pu()                 |
| pensize(width)   | Setzt Stiftbreite auf width       | t.pensize(5)           |
| width(width)     | Synonym für pensize()             | t.width(5)             |
| pen(...)         | Setzt mehrere Stift-Attribute     | t.pen(pensize=5,       |
|                  |                                   | pencolor="red")        |
| isdown()         | Prüft, ob Stift aktiviert ist     | if t.isdown(): ...     |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 3: FARB- UND FÜLLUNGSBEFEHLE
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| color(c)         | Setzt Stift- und Füllfarbe auf c  | t.color("red")         |
| color(c1, c2)    | Setzt Stiftfarbe c1, Füllfarbe c2 | t.color("red", "blue") |
| pencolor(c)      | Setzt Stiftfarbe auf c            | t.pencolor("red")      |
| fillcolor(c)     | Setzt Füllfarbe auf c             | t.fillcolor("blue")    |
| begin_fill()     | Beginnt Füllung                   | t.begin_fill()         |
| end_fill()       | Beendet Füllung                   | t.end_fill()           |
| filling()        | Prüft, ob Füllung aktiv ist       | if t.filling(): ...    |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 4: SICHTBARKEITS- UND ERSCHEINUNGSBEFEHLE
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| hideturtle()     | Macht Turtle unsichtbar           | t.hideturtle()         |
| ht()             | Kurzform für hideturtle()         | t.ht()                 |
| showturtle()     | Macht Turtle sichtbar             | t.showturtle()         |
| st()             | Kurzform für showturtle()         | t.st()                 |
| isvisible()      | Prüft, ob Turtle sichtbar ist     | if t.isvisible(): ...  |
| shape(name)      | Ändert Form der Turtle            | t.shape("turtle")      |
|                  | (arrow, turtle, circle, square,   |                        |
|                  | triangle, classic)                |                        |
| shapesize(...)   | Ändert Größe der Turtle           | t.shapesize(2, 2)      |
| turtlesize(...)  | Synonym für shapesize()           | t.turtlesize(2, 2)     |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 5: EREIGNISBEHANDLUNG UND SCREEN-KONTROLLE
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| speed(s)         | Setzt Geschwindigkeit (0-10)      | t.speed(5)             |
|                  | 0=schnellste, 1=langsamste,       |                        |
|                  | 10=sehr schnell                   |                        |
| delay(d)         | Setzt Verzögerung in ms           | screen.delay(10)       |
| onclick(func)    | Bindet Funktion an Mausklick      | t.onclick(my_function) |
| onrelease(func)  | Bei Loslassen der Maustaste       | t.onrelease(func)      |
| ondrag(func)     | Bei Ziehen der Turtle mit Maus    | t.ondrag(func)         |
| onkey(func, key) | Bei Drücken der Taste key         | screen.onkey(func, "a")|
| listen()         | Aktiviert Tastaturereignisse      | screen.listen()        |
| exitonclick()    | Schließt Fenster bei Klick        | screen.exitonclick()   |
| tracer(n)        | Aktualisiert Bildschirm alle n    | screen.tracer(0)       |
|                  | Zeichenschritte (0=deaktiviert)   |                        |
| update()         | Aktualisiert Bildschirm manuell   | screen.update()        |
| bgcolor(c)       | Setzt Hintergrundfarbe            | screen.bgcolor("black")|
| title(t)         | Setzt Fenstertitel                | screen.title("Turtle") |
| setup(w, h)      | Setzt Fenstergröße                | screen.setup(800, 600) |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 6: ZUSTANDSABFRAGEN
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| position()       | Gibt aktuelle Position zurück     | pos = t.position()     |
| pos()            | Kurzform für position()           | pos = t.pos()          |
| xcor()           | Gibt x-Koordinate zurück          | x = t.xcor()           |
| ycor()           | Gibt y-Koordinate zurück          | y = t.ycor()           |
| heading()        | Gibt aktuelle Ausrichtung zurück  | angle = t.heading()    |
| distance(x, y)   | Abstand zu Punkt (x,y)            | dist = t.distance(0,0) |
| towards(x, y)    | Winkel zum Punkt (x,y)            | angle = t.towards(0,0) |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------
# KATEGORIE 7: FORTGESCHRITTENE FEATURES
# ----------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| clone()          | Erstellt Kopie der Turtle         | t2 = t.clone()         |
| stamp()          | Hinterlässt Stempel der Turtle    | stamp_id = t.stamp()   |
| clearstamp(id)   | Löscht Stempel mit ID id          | t.clearstamp(stamp_id) |
| clearstamps(n)   | Löscht n Stempel                  | t.clearstamps(2)       |
| getscreen()      | Gibt Screen-Objekt zurück         | s = t.getscreen()      |
| getturtle()      | Gibt Turtle-Objekt zurück         | turtle = t.getturtle() |
| getpen()         | Synonym für getturtle()           | pen = t.getpen()       |
| write(text)      | Schreibt Text an Position         | t.write("Hello")       |
| dot(size)        | Zeichnet Punkt mit Größe size     | t.dot(10)              |
| undo()           | Macht letzte Aktion rückgängig    | t.undo()               |
| reset()          | Setzt Turtle zurück               | t.reset()              |
| clear()          | Löscht Zeichnungen der Turtle     | t.clear()              |
| tilt(angle)      | Neigt Turtle-Form um angle Grad   | t.tilt(45)             |
| settiltangle(a)  | Setzt absoluten Neigungswinkel    | t.settiltangle(45)     |
| tiltangle()      | Gibt aktuellen Neigungswinkel     | angle = t.tiltangle()  |
| getshapes()      | Liste verfügbarer Formen          | shapes = screen.       |
|                  |                                   | getshapes()            |
| register_shape()| Registriert benutzerdefinierte    | screen.register_shape( |
|                  | Form                             | "newshape", ((0,0),    |
|                  |                                   | (10,10), (0,10)))      |
+------------------+-----------------------------------+------------------------+
"""

# ----------------------------------------------
# KATEGORIE 8: SCREEN METHODEN UND EIGENSCHAFTEN
# ----------------------------------------------
"""
+------------------+-----------------------------------+------------------------+
| Methode          | Beschreibung                      | Beispiel               |
+------------------+-----------------------------------+------------------------+
| mode(m)          | Setzt Koordinatenmodus           | screen.mode("logo")    |
|                  | (standard, logo, world)           |                        |
| colormode(cmode) | Setzt Farbmodus (1.0 oder 255)    | screen.colormode(255)  |
| getcanvas()      | Gibt tkinter.Canvas zurück        | canvas = screen.       |
|                  |                                   | getcanvas()            |
| window_width()   | Breite des Fensters               | w = screen.            |
|                  |                                   | window_width()         |
| window_height()  | Höhe des Fensters                 | h = screen.            |
|                  |                                   | window_height()        |
| screensize(w, h) | Ändert Zeichenfläche              | screen.screensize(     |
|                  |                                   | 1000, 1000)            |
| setworldcoord... | Setzt Weltkoordinaten             | screen.                |
|                  |                                   | setworldcoordinates(   |
|                  |                                   | -10, -10, 10, 10)      |
| mainloop()       | Startet Event-Loop                | screen.mainloop()      |
| bye()            | Schließt Turtle-Fenster           | screen.bye()           |
| getshapes()      | Liste aller Formen                | shapes = screen.       |
|                  |                                   | getshapes()            |
| bgpic(picname)   | Setzt Hintergrundbild             | screen.bgpic(          |
|                  |                                   | "background.gif")      |
| save_as_gif(f)   | Speichert Zeichenfläche als GIF   | screen.save_as_gif(    |
|                  |                                   | "bild.gif")            |
+------------------+-----------------------------------+------------------------+
"""

# Beispiel wie man diese Referenz nutzen kann
def beispiel_funktion():
    t = turtle.Turtle()
    t.speed(0)  # Schnellste Geschwindigkeit
    
    # Beispiel für Bewegung und Farbwechsel
    t.pencolor("red")
    t.forward(100)
    t.right(90)
    t.pencolor("blue")
    t.forward(100)
    
    # Beispiel für Füllung
    t.pencolor("green")
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    
    # Fenster offen halten
    turtle.exitonclick()

# Auskommentiert, damit die Datei nicht automatisch ausgeführt wird
# beispiel_funktion()

print("Diese Datei enthält eine umfassende Referenz für Python Turtle.")
print("Um die Funktionen zu nutzen, importieren Sie die Datei und rufen Sie beispiel_funktion() auf")
print("oder verwenden Sie die Referenztabellen für Ihre eigenen Turtle-Programme.")