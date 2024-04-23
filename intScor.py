import pygame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir la pantalla
screen_width = 1550
screen_height = 785
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Equipo Scorpion")

# Función para dibujar el gráfico en Pygame
def draw_graph(surface, image):
    surface.blit(image, (599, 294))
    
def draw_graph2(surface, image):
    surface.blit(image, (599, 100))
    
def draw_graph3(surface, image):
    surface.blit(image, (897, 104))

def draw_graph4(surface, image):
    surface.blit(image, (599, 699))
    
def draw_graph5(surface, image):
    surface.blit(image, (897, 699))

# Función para cargar datos desde el archivo CSV
def load_data_from_csv(filename):
    return pd.read_csv(filename)

# Función para generar la gráfica usando matplotlib
def generate_graph(data, i):
    plt.cla()
    plt.figure(figsize=(5, 4),dpi=80)
    plt.plot(data['Tiempo'][:i+1], data['Altitud'][:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Altitud')
    plt.title('Altitud con respecto al Tiempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)

def generate_graph2(data, i):
    plt.cla()
    plt.figure(figsize=(5, 4),dpi=50)
    plt.plot(data['Tiempo'][:i+1], data['Temperatura'][:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Temperatura con respecto al Tiempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)

def generate_graph3(data, i):
    plt.cla()
    plt.figure(figsize=(5, 4),dpi=50)
    plt.plot(data['Tiempo'][:i+1], data['Presion'][:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Presion')
    plt.title('Presion con respecto al Tiempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)

def generate_graph4(data, i):
    plt.cla()
    plt.figure(figsize=(5, 4),dpi=50)
    plt.plot(data['Tiempo'][:i+1], data['Velocidad'][:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title('Velocidad con respecto al Tiempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)

def generate_graph5(data, i):
    plt.cla()
    plt.figure(figsize=(5, 4),dpi=50)
    plt.plot(data['Tiempo'][:i+1], data['Aceleracion'][:i+1])  
    plt.xlabel('Tiempo')
    plt.ylabel('Aceleracion')
    plt.title('Aceleracion con respecto al Tiempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return pygame.image.load(buf)

# Cargar datos desde el archivo CSV
filename = 'data_Sat.csv'
data = load_data_from_csv(filename)

# Bucle principal
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Generar la gráfica
    graph_image = generate_graph(data, i)
    graph_image2 = generate_graph2(data, i)
    graph_image3 = generate_graph3(data, i)
    graph_image4 = generate_graph4(data, i)
    graph_image5 = generate_graph5(data, i)

    # Dibujar la gráfica
    draw_graph(screen, graph_image)
    draw_graph2(screen, graph_image2)
    draw_graph3(screen, graph_image3)
    draw_graph4(screen, graph_image4)
    draw_graph5(screen, graph_image5)

    # Actualizar la pantalla
    pygame.display.flip()

    # Incrementar el índice para la siguiente iteración (simula el tiempo)
    i += 1

    # Ajustar la velocidad de la animación según sea necesario
    pygame.time.delay(1000)  # Pausa de 100 milisegundos

# Salir de Pygame
pygame.quit()
