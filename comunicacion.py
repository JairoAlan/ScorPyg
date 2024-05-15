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
        data = await reader.read(100)
        if data:
            print(data.decode())

asyncio.run(main())


