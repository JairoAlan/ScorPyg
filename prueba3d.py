import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_cylinder():
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    
    # Dibujar la parte superior del cilindro (cara negra)
    glColor3f(0, 0, 0)
    gluDisk(quadric, 0, 1, 20, 1)
    
    # Dibujar el cuerpo del cilindro (cara uniforme)
    glColor3f(0.5, 0.5, 1.0)  # Color del cilindro
    gluCylinder(quadric, 1, 1, 2, 20, 1)
    
    # Dibujar la parte inferior del cilindro (cara roja)
    glColor3f(1, 0, 0)  # Color rojo
    glPushMatrix()
    glTranslatef(0, 0, 2)  # Mover hacia abajo para la parte inferior
    gluDisk(quadric, 0, 1, 20, 1)
    glPopMatrix()

# Función principal
def main():
    pygame.init()
    display = (300, 200)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -4)
    
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Establecer color de fondo blanco
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotatef(0.1, 1,1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cylinder()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
