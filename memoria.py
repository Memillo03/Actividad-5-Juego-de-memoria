from random import *
from random import randrange
from turtle import *

from freegames import path

car = path('car.gif')
#tiles = list(range(32)) * 2
state = {'mark': None, 'Taps': 0}
hide = [True] * 64

writer = Turtle(visible=False)
tiles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
         "Z", "#", "%", "&", "$", "*"]*2


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    writer.undo()
    # se muestra en pantalla el "estado" de la variable taps
    writer.write(state['Taps'])
    # se suma 1 por cada tap al contador taps
    state['Taps'] += 1

    # Si mark es none se le asigna un índice inicial
    # Si índice mark es igual al tile seleccionado se le asigna ese número, si no uno diferente
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Asignación cuando cambian índices pero no número
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        # Se cubren los tiles con la imagen para los que estén escondidos
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        # Se marcan los cuadros no marcados
        x, y = xy(mark)
        up()
        # Se centran los numeros utilizando un factor de 25.5 para poder utilizar el align="center"
        goto(x + 25.5, y)
        # Se le agrega color a los números/letras
        colormode(255)
        color((randrange(255), randrange(255), randrange(255)))
        #Se centran los números en sus respectivas tiles
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    # Si todas las tiles ya están ocultas ("imagen completa") se termina el juego
    if not any(hide):
        # Se muestra el conteo total de taps en terminal al terminar juego
        print("Total taps: ", state["Taps"])
    else:
        update()  # actualización del tablero
        ontimer(draw, 100)


shuffle(tiles)
setup(500, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
# se acomoda la posición del contador dentro del juego y su color
writer.goto(220, 160)
writer.color('black')
writer.write(state['Taps'])
onscreenclick(tap)
draw()
done()
done()
done()
done()
