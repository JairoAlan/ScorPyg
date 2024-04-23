import webbrowser
import requests
import pygame
import io
from PIL import Image

def direccion_actual(destino_latitud, destino_longitud):
    map_url = f"https://maps.google.com/maps?daddr={destino_latitud},{destino_longitud}"
    webbrowser.open(map_url)

# Ejemplo de uso
direccion_actual("40.7128", "-74.0060")  # Coordenadas de la ciudad de Nueva York como ejemplo

# Función para cargar el mapa de Google Maps
def cargar_mapa(latitud, longitud, zoom, tamaño):
    api_key = "AIzaSyDzdqPpaND_WEWZauxETqi5AdfhaCDI7yw" 
    marker = f"markers=color:red|label:U|{latitud},{longitud}"
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitud},{longitud}&zoom={zoom}&size={tamaño}&key={api_key}&{marker}&maptype=satellite"
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    img.save("mapa_temp.png")  # Guarda temporalmente la imagen
    mapa = pygame.image.load("mapa_temp.png")
    return mapa


