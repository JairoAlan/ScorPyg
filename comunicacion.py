import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import serial_asyncio
from matplotlib.animation import FuncAnimation
import asyncio
import csv

lora_band = "915000000"
lora_networkid = "6"
lora_address = "0"
df = pd.read_csv('data_Sat.csv')
async def main():
    reader, writer = await serial_asyncio.open_serial_connection(url='COM3', baudrate=115200)

    writer.write(("AT+BAND="+lora_band+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+NETWORKID="+lora_networkid+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+ADDRESS="+lora_address+'\r\n').encode())
    await writer.drain()
    writer.write(("AT+PARAMETER=7,7,1,4\r\n").encode())
    await writer.drain()

    while True:
        data = await reader.read(100)
        if data:
            print(data.decode())

# asyncio.run(main())


