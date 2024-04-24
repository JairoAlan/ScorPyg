import pygame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import requests
from PIL import Image,ImageDraw, ImageFont
from geopy.distance import geodesic

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir la pantalla
screen_width = 1550
screen_height = 800
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
    surface.blit(image, (599, 599))
    
def draw_graph5(surface, image):
    surface.blit(image, (897, 599))

# Función para cargar datos desde el archivo CSV
def load_data_from_csv(filename):
    return pd.read_csv(filename)


# Función para cargar el mapa de Google Maps
def cargar_mapa(mi_latitud, mi_longitud, destino_latitud, destino_longitud, zoom, tamaño):
    api_key = "AIzaSyDzdqPpaND_WEWZauxETqi5AdfhaCDI7yw" 
    maptype = "satellite"
    marker_destino = f"markers=color:red|label:D|{destino_latitud},{destino_longitud}"
    marker_origen = f"markers=color:green|label:U|{mi_latitud},{mi_longitud}"
    distancia = geodesic((mi_latitud, mi_longitud), (destino_latitud, destino_longitud)).meters
    texto_distancia = f"Distancia al destino: {distancia:.2f} mts"
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={mi_latitud},{mi_longitud}&zoom={zoom}&size={tamaño}&key={api_key}&maptype={maptype}&{marker_destino}&{marker_origen}&markers=size:mid|color:blue|label:D|{mi_latitud},{mi_longitud}&path=color:0x0000ff|weight:5|{mi_latitud},{mi_longitud}|{destino_latitud},{destino_longitud}"
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((10, 10), texto_distancia, fill="white", font=font)

    img.save("mapa_temp.png")  # Guarda temporalmente la imagen
    mapa = pygame.image.load("mapa_temp.png")
    return mapa

def obtener_ubicacion_actual():
    api_key = "AIzaSyDzdqPpaND_WEWZauxETqi5AdfhaCDI7yw" 
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.post(url)
    data = response.json()
    #print(data)
    if 'location' in data:
        latitud = data['location']['lat']
        longitud = data['location']['lng']
        return latitud, longitud
    else:
        print("No se pudo obtener la ubicación.")
        return None, None

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

# Obtiene la ubicación actual
latitud, longitud = obtener_ubicacion_actual()

# Destino debera tener las del satelite cansat
des_latitud = "20.1352721"
des_long = "-98.385339"
zoom = 18
tamaño = "400x300"

mapa = cargar_mapa(latitud, longitud,des_latitud,des_long, zoom, tamaño)


# Bucle principal
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)
    screen.blit(mapa, (50, 450))

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
