# Модуль вывода зафиксированных землетрясений с данными введенными с клавиатуры: 
#период, широта, долгота, радиус от координатов, минимальная магнитуда

import requests
import sqlite3
from datetime import datetime

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'


def save(place_list):
    # creates a database
    conn = sqlite3.connect("earthquake.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS earthquake (place TEXT, magnitude REAL, date TEXT);")
    insert_query = "INSERT INTO earthquake VALUES (?, ?, ?);"
    for earthquake in place_list:
        cursor.execute(insert_query, earthquake)
    conn.commit()
    conn.close()


def print_earth():
    # opens the created database and displays in a tuple
    conn = sqlite3.connect("earthquake.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquake;")
    for row in cursor:
        print(row)
    conn.commit()
    conn.close()

# Ввод данных с клавиатуры в соответствующем формате. Если ввод не осуществляется вручную, то выводится информация с
# данными по уфе с радиусом 700 км с 2001-01-01 по 2020-01-01 и магнитудой больше 2
starttime = str(input('Enter Start Time (f:YYYY-MM-DD): '))
if starttime == '': starttime='2001-01-01'
endtime = str(input('Enter End Time (f:YYYY-MM-DD): '))
if endtime == '': endtime='2020-01-01'
latitude = str(input('Enter Latitude (f:XX.XX): '))
if latitude == '': latitude='54.74'
longitude = str(input('Enter Longtitude (f:XX.XX): '))
if longitude == '': longitude='55.96'
maxradiuskm = str(input('Enter Max Radius Km: '))
if maxradiuskm == '': maxradiuskm='700'
minmagnitude = str(input('Enter Min Magnitude: '))
if minmagnitude =='': minmagnitude='2'

response = requests.get(url, headers={'Accept': 'application/json'}, params={
        'format': 'geojson',
        'starttime': starttime,
        'endtime': endtime,
        'latitude': latitude,
        'longitude': longitude,
        'maxradiuskm': maxradiuskm,
        'minmagnitude': minmagnitude
    })

data = response.json()
count = data['metadata']['count']
earthquake_list = []
for num in range(1, count):
    date = int(str(data['features'][num]['properties']['time'])[:10])
    find = (data['features'][num]['properties']['place'],
            data['features'][num]['properties']['mag'],
            datetime.fromtimestamp(date).strftime('%Y-%m-%d %I:%M:%S %p'))
    earthquake_list.append(find)


if __name__ == '__main__':
    save(earthquake_list)
    print_earth()
