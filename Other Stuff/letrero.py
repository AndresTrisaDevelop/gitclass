import turtle

def neon_text(text):
    # Configuración de la ventana
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Anuncio de Neón")

    # Configuración del estilo de la fuente
    font_style = ("Arial", 50, "bold")

    # Crear la tortuga para dibujar el texto
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    
    # Mover la tortuga a la posición inicial
    pen.penup()
    pen.goto(0, 0)
    pen.color("cyan")
    
    # Dibujar el texto en el centro de la pantalla
    for _ in range(3):  # Tres capas para crear el efecto de neón
        pen.color("cyan")
        pen.write(text, align="center", font=font_style)
        
        pen.color("blue")
        pen.write(text, align="center", font=font_style)
        
        pen.color("magenta")
        pen.write(text, align="center", font=font_style)
    
    # Mantener la ventana abierta hasta que el usuario la cierre
    turtle.done()

# Texto del anuncio que quieres mostrar
neon_text("¡Ya vengo, fui por pola, queda la musica random!")
