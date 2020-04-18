# Модуль вывода зафиксированных землетрясений с данными введенными с клавиатуры:
# период, широта, долгота, радиус от координатов, минимальная магнитуда

import requests
import sqlite3
from datetime import datetime
from contextlib import closing

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

_conn = None


def get_conn():
    global _conn
    if _conn is None:
        _conn = sqlite3.connect("earthquake.db")
    return _conn


def close_conn():
    if _conn is not None:
        _conn.close()


def save(place_list):
    # creates a database
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS earthquake (place TEXT, magnitude REAL, date TEXT);")
    insert_query = "INSERT INTO earthquake VALUES (?, ?, ?);"
    for earthquake in place_list:
        cursor.execute(insert_query, earthquake)
    conn.commit()


def print_earth():
    # opens the created database and displays in a tuple
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquake;")
    for row in cursor:
        print(row)
    conn.commit()


def main():
    # Ввод данных с клавиатуры в соответствующем формате. Если ввод не осуществляется вручную, то выводится информация с
    # данными по уфе с радиусом 700 км с 2001-01-01 по 2020-01-01 и магнитудой больше 2
    starttime = input('Enter Start Time (f:YYYY-MM-DD): ') or '2001-01-01'
    endtime = input('Enter End Time (f:YYYY-MM-DD): ') or '2020-01-01'
    latitude = input('Enter Latitude (f:XX.XX): ') or '54.74'
    longitude = input('Enter Longtitude (f:XX.XX): ') or '55.96'
    maxradiuskm = input('Enter Max Radius Km: ') or 700
    minmagnitude = input('Enter Min Magnitude: ') or 2

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

    save(earthquake_list)
    print_earth()


if __name__ == '__main__':
    main()
    close_conn()
