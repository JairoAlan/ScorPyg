import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import serial_asyncio
import asyncio
import csv


df = pd.read_csv('data_Sat.csv')

async def main():
    reader, writer = await serial_asyncio.open_serial_connection(url='COM3', baudrate=115200)    
    writer.write(("AT+PARAMETER=7,7,1,4\r\n").encode())
    await writer.drain()

    while True:
        data = await reader.read(400)
        await asyncio.sleep(1)
        if data:
            #print(data.decode())
            if len(data) > 140 and data.decode().startswith("+RCV=1"):
                datos = data.decode()
                lista = datos.split(',')
                temp = lista[2]
                preHp = lista[3]
                altitud = lista[4]
                acc_x = lista[5]
                acc_y = lista[6]
                acc_z = lista[7]
                gy_x = lista[8]
                gy_y = lista[9]
                gy_z = lista[10]
                velocidad = lista[11]
                aceleracion = lista[12]
                latitud = lista[13]
                longitud = lista[14]
                altGps = lista[15]
                tiempo = lista[16]
                
                
                print(temp,preHp,altitud,acc_x,acc_y,acc_z,gy_x,gy_y,gy_z,velocidad,aceleracion,latitud,longitud,altGps,tiempo)

asyncio.run(main())

