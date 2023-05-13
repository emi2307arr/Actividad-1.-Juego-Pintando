## El código comienza importando la biblioteca Turtle 
## y la función vector de la biblioteca Freegames que nos permite
## dibujar en nuestro programa.

from turtle import *

from freegames import vector
import math

## Definimos la función para hacer una línea

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

## Definimos la función para hacer un cuadrado
    
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

## Definimos la función para hacer un círculo    

def drawcircle(start, end):
    """Draw circle from start to end."""
    radius = abs(end.x - start.x)
    up()
    goto(start.x, start.y - radius)
    down()
    circle(radius)

def rectangle(start, end):
    """Draw rectangle from start to end."""


def triangle(start, end):
    """Draw triangle from start to end."""

##La función tap() se utiliza para almacenar el punto de inicio o dibujar la forma.
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

## Definimos la función de cada tecla para seleccionar
## en nuestro programa

onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', drawcircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
