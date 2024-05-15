import pygame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import os
import requests
import button
from PIL import Image,ImageDraw, ImageFont
from geopy.distance import geodesic

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK      =  (0, 0, 0)
WHITE      =  (255, 255, 255)
lila       =  (242, 223, 247)
morado     =  (75, 41, 157)
amarillo   =  (253, 183, 15)
gris       =  (240, 240, 240)
marcadorC  =  (207, 170, 255)
marcadorT  =  (170, 192, 255)

# Definir la pantalla
size = (1920, 990)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
icono = pygame.image.load('Img/lia.png')
pygame.display.set_caption("Equipo Scorpion")
pygame.display.set_icon(icono)

# Cargar imagenes
logo = pygame.image.load('Img/Scorpion.png')
logou = pygame.image.load('Img/upt.png')
reporte = pygame.image.load('Img/reporte.png').convert_alpha()

# Definir botón
boton_reporte = button.Button(1450, 15, reporte, 1)

# Escribir textos para la interfaz
encabezado = pygame.font.SysFont("Arial Black", 50)
seccion = pygame.font.SysFont("Century Gothic", 20)
tablaE = pygame.font.SysFont("Century Gothic", 15, bold=True)

# Funcion para dibujar texto
def draw_text(text, font, text_clr, corX, corY):
    img = font.render(text, True, text_clr)
    screen. blit(img, (corX, corY))

# Función para dibujar el gráfico en Pygame
def draw_graph(surface, image, posX, posY):
    surface.blit(image, (posX, posY))


# Función para cargar datos desde el archivo CSV
def load_data_from_csv(filename):
    return pd.read_csv(filename)


# Función para cargar el mapa de Google Maps
def cargar_mapa(mi_latitud, mi_longitud, destino_latitud, destino_longitud, zoom=18, tamaño="550x550"):
    api_key = "AIzaSyDzdqPpaND_WEWZauxETqi5AdfhaCDI7yw" 
    maptype = "satellite"
    marker_destino = f"markers=color:red|label:D|{destino_latitud},{destino_longitud}"
    marker_origen = f"markers=color:green|label:O|{mi_latitud},{mi_longitud}"
    distancia = geodesic((mi_latitud, mi_longitud), (destino_latitud, destino_longitud)).meters
    texto_distancia = f"Distancia al destino: {distancia:.2f} mts"
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={destino_latitud},{destino_longitud}&zoom={zoom}&size={tamaño}&key={api_key}&maptype={maptype}&{marker_destino}&{marker_origen}&markers=size:mid|color:blue|label:D|{mi_latitud},{mi_longitud}&path=color:0x0000ff|weight:5|{mi_latitud},{mi_longitud}|{destino_latitud},{destino_longitud}"
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((10, 10), texto_distancia, fill="white", font=font)

    img.save("mapa_temp.png")  # Guarda temporalmente la imagen
    mapa = pygame.image.load("mapa_temp.png")
    return mapa

def obtener_ubicacion_actual():
    try:
        api_key = "AIzaSyDzdqPpaND_WEWZauxETqi5AdfhaCDI7yw" 
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
        response = requests.post(url)
        data = response.json()
        print(data)
        if 'location' in data:
            latitud = data['location']['lat']
            longitud = data['location']['lng']
            return latitud, longitud
        else:
            print("No se pudo obtener la ubicación.")
            return None, None
    except Exception as e:
        print(e)

# Función para generar la gráfica usando matplotlib
def generate_graph(data, i):
    plt.cla()
    plt.figure(figsize=(11.5, 4),dpi=60,facecolor="#F0F0F0")
    plt.gca().set_facecolor('#F0F0F0')
    plt.plot(data['Tiempo'][:i+1], data['Altitud'][:i+1], color="#4B299D")  
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
    plt.figure(figsize=(6.5, 4),dpi=50,facecolor="#F0F0F0")
    plt.gca().set_facecolor('#F0F0F0')
    plt.plot(data['Tiempo'][:i+1], data['Temperatura'][:i+1], color="#4B299D")  
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
    plt.figure(figsize=(6.5, 4),dpi=50,facecolor="#F0F0F0")
    plt.gca().set_facecolor('#F0F0F0')
    plt.plot(data['Tiempo'][:i+1], data['Presion'][:i+1], color="#4B299D")  
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
    plt.figure(figsize=(6.5, 4),dpi=50,facecolor="#F0F0F0")
    plt.gca().set_facecolor('#F0F0F0')
    plt.plot(data['Tiempo'][:i+1], data['Velocidad'][:i+1], color="#4B299D")  
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
    plt.figure(figsize=(6.5, 4),dpi=50,facecolor="#F0F0F0")
    plt.gca().set_facecolor('#F0F0F0')
    plt.plot(data['Tiempo'][:i+1], data['Aceleracion'][:i+1], color="#4B299D")  
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
des_latitud = "20.133534"
des_long = "-98.383157"
#zoom = 18
#tamaño = "550x550"

mapa = cargar_mapa(latitud, longitud,des_latitud,des_long)


# Bucle principal
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
        screen.fill(lila)

    # Inicio de zona de dibujo de interfaz
        #Cabecera de la interfaz
    pygame.draw.rect(screen, morado, (0,0, 1920, 80))
        	# Logo Scorpion
    screen.blit(logo,(20, 5))
            # Encabezado
    draw_text("Estación Terrena", encabezado, WHITE, 110, 0)
            # Boton de reporte de Misión
    if boton_reporte.draw(screen):
        print('Reporte')
            # Logo Scorpion
    screen.blit(logou,(1820, 5))
        # Tablero de datos
    pygame.draw.rect(screen, WHITE, (10, 90, 1900, 890), width=0, border_radius=10)

# Tabla de alturas
    pygame.draw.rect(screen, lila, (30, 100, 190, 40), width=0, border_radius=10)
    draw_text("Tabla de alturas", seccion, BLACK, 45, 105)        
    pygame.draw.rect(screen, morado, (20, 140, 550, 240), width=0, border_radius=10)
                # Altura actual
    pygame.draw.rect(screen, lila, (23, 143, 120, 76), width=0, border_radius=5)
    draw_text("Altura actual", tablaE, BLACK, 30, 170)
    pygame.draw.rect(screen, WHITE, (146, 143, 420, 76), width=0, border_radius=5)
                # Altura máxima
    pygame.draw.rect(screen, lila, (23, 222, 120, 76), width=0, border_radius=5)
    draw_text("Altura máxima", tablaE, BLACK, 30, 250)
    pygame.draw.rect(screen, WHITE, (146, 222, 420, 76), width=0, border_radius=5)
                # Altura de desacople
    pygame.draw.rect(screen, lila, (23, 301, 120, 76), width=0, border_radius=5)
    draw_text("Altura de", tablaE, BLACK, 30, 320)
    draw_text("desacople", tablaE, BLACK, 30, 333)
    pygame.draw.rect(screen, WHITE, (146, 301, 420, 76), width=0, border_radius=5)

# Mapa       
    screen.blit(mapa, (20, 420))
    pygame.draw.rect(screen, lila, (30, 390, 200, 40), width=0, border_radius=10)
    draw_text("Ubicación actual", seccion, BLACK, 45, 395)
    
# Graficas
    # Generar la gráfica
    graph_image = generate_graph(data, i)
    graph_image2 = generate_graph2(data, i)
    graph_image3 = generate_graph3(data, i)
    graph_image4 = generate_graph4(data, i)
    graph_image5 = generate_graph5(data, i)

    # Fondo y titulos de las gáficas
    pygame.draw.rect(screen, gris, (590, 120, 350, 250), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (600, 100, 190, 40), width=0, border_radius=10)
    draw_text("Tempreratura", seccion, BLACK, 605, 105)   
    pygame.draw.rect(screen, gris, (950, 120, 350, 250), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (960, 100, 230, 40), width=0, border_radius=10)
    draw_text("Presion atmosferica", seccion, BLACK, 965, 105)    
    pygame.draw.rect(screen, gris, (590, 400, 710, 290), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (600, 380, 100, 40), width=0, border_radius=10)
    draw_text("Altitud", seccion, BLACK, 605, 385)    
    pygame.draw.rect(screen, gris, (590, 720, 350, 250), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (600, 700, 190, 40), width=0, border_radius=10)
    draw_text("Velocidad", seccion, BLACK, 605, 705)   
    pygame.draw.rect(screen, gris, (950, 720, 350, 250), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (960, 700, 190, 40), width=0, border_radius=10)
    draw_text("Aceleración", seccion, BLACK, 965, 705)  

    # Dibujar la gráfica
    draw_graph(screen, graph_image, 600, 430)
    draw_graph(screen, graph_image2, 600, 150)
    draw_graph(screen, graph_image3, 960, 150)
    draw_graph(screen, graph_image4, 600, 750)
    draw_graph(screen, graph_image5, 960, 750)
# Giroscopio
    # Gráfico altura
    pygame.draw.rect(screen, gris, (1310, 120, 590, 410), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (1320, 100, 190, 40), width=0, border_radius=10)
    draw_text("Gráfico altura", seccion, BLACK, 1325, 105) 
    # Modelo 3d
    pygame.draw.rect(screen, gris, (1310, 560, 590, 410), width=0, border_radius=10)
    pygame.draw.rect(screen, lila, (1320, 540, 190, 40), width=0, border_radius=10)
    draw_text("Giroscopio", seccion, BLACK, 1325, 545) 

    # Fin de zona de dibujo de interfaz

    # Actualizar la pantalla
    pygame.display.flip()

    # Incrementar el índice para la siguiente iteración (simula el tiempo)
    i += 1

    # Ajustar la velocidad de la animación según sea necesario
    pygame.time.delay(1000)  # Pausa de 100 milisegundos

# Salir de Pygame
pygame.quit()
