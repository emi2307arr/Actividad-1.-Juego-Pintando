# Actividad-1.-Juego-Pintando

'''
    El código comienza importando la biblioteca Turtle 
    y la función vector de la biblioteca Freegames que nos permite
    dibujar en nuestro programa.
    
    line(start, end): Dibuja una línea desde el punto de inicio (start) hasta el punto final (end).
    
    square(start, end): Dibuja un cuadrado desde el punto de inicio (start) hasta el punto final (end).
    
    drawcircle(start, end): Dibuja un círculo desde el punto de inicio (start) hasta el punto final (end).
    
    rectangle(start, end): Dibuja un rectángulo desde el punto de inicio (start) hasta el punto final (end).
    
    triangle(start, end): Dibuja un triángulo desde el punto de inicio (start) hasta el punto final (end).

La función tap(x, y) se utiliza para almacenar el punto de inicio o para dibujar la forma, dependiendo de si se ha establecido ya el punto de inicio.

La función store(key, value) almacena un valor en el estado en la clave especificada.

La variable state es un diccionario que almacena el estado del programa, incluyendo el punto de inicio, la forma que se está dibujando actualmente, etc.

Las siguientes líneas de código configuran la ventana gráfica y vinculan las teclas del teclado a las funciones correspondientes:

    setup(420, 420, 370, 0): Configura el tamaño de la ventana y su posición en la pantalla.
    
    onscreenclick(tap): Asigna la función tap al evento de clic del mouse en la ventana.
    
    listen(): Pone el programa en modo de escucha de eventos del teclado.
    onkey(undo, 'u'): Asigna la función undo al evento de pulsar la tecla "u".
    onkey(lambda: color('black'), 'K'): Asigna una función lambda que cambia el color a negro al evento de pulsar la tecla "K".
    
    onkey(lambda: color('white'), 'W'): Asigna una función lambda que cambia el color a blanco al evento de pulsar la tecla "W".
    
    onkey(lambda: color('green'), 'G'): Asigna una función lambda que cambia el color a verde al evento de pulsar la tecla "G".
    
    onkey(lambda: color('blue'), 'B'): Asigna una función lambda que cambia el color a azul al evento de pulsar la tecla "B".
    
    onkey(lambda: color('red'), 'R'): Asigna una función lambda que cambia el color a rojo al evento de pulsar la tecla "R".
    
    onkey(lambda: color('pink'), 'P'): Asigna una función lambda que cambia el color a rosa al evento de pulsar la tecla "P".
    
    onkey(lambda: store('shape', line), 'l'): Asigna una función lambda que cambia la forma actual a una línea al evento de pulsar la tecla "l".
    
    onkey(lambda: store('shape', square), 's'): Asigna una función lambda que cambia la forma actual a un cuadrado al evento de pulsar la tecla "s".
    
'''
