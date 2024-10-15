import requests
from datetime import datetime

# Definir los parámetros de la consulta
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": "2024-01-01",
    "endtime": "2024-01-02",
    "minmagnitude": 5
}

# Realizar la solicitud GET a la API
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Filtrar e imprimir los datos relevantes
    print(f"{'Fecha':<20} {'Magnitud':<10} {'Ubicación'}")
    print("-" * 50)

    for feature in data['features']:
        # Obtener magnitud, lugar y tiempo
        magnitude = feature['properties']['mag']
        place = feature['properties']['place']
        timestamp = feature['properties']['time'] / 1000  # Convertir de milisegundos a segundos
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Imprimir de forma legible
        print(f"{date:<20} {magnitude:<10} {place}")
else:
    print(f"Error: {response.status_code}")
input("Presiona Enter para salir...")
