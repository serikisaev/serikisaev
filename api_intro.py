import requests
from datetime import datetime

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
st_time = str(input('Enter Start Time (f:YYYY-MM-DD): '))
end_time = str(input('Enter End Time (f:YYYY-MM-DD): '))
latitude = str(input('Enter Latitude (f:XX.XX): '))
longtitude = str(input('Enter Longtitude (f:XX.XX): '))
maxradius = str(input('Enter Max Radius Km: '))
minmagnitude = str(input('Enter Min Magnitude: '))

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': st_time,
    'endtime': end_time,
    'latitude': latitude,
    'longitude': longtitude,
    'maxradiuskm': maxradius,
    'minmagnitude': minmagnitude
    
    # 'format': 'geojson',
    # 'starttime': '2001-01-01',
    # 'endtime': '2020-01-01',
    # 'latitude': '54.74',
    # 'longitude': '55.96',
    # 'maxradiuskm': '700',
    # 'minmagnitude': '2'

    })
data = response.json()

count = data['metadata']['count']


for num in range(1, count):
    date = int(str(data['features'][num]['properties']['time'])[:10])

    print(str(num) + '. ' + 'Место: ' + data['features'][num]['properties']['place'] + ' '
          + str(data['features'][num]['properties']['mag']) + ' '
          + 'Дата и время: ' + datetime.fromtimestamp(date).strftime('%Y-%m-%d %I:%M:%S %p'))
