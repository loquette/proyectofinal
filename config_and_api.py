import requests
from datetime import datetime

# Configuraciones de las APIs
GEONAMES_USER = 'Lu_Fer'  # Tu usuario de GeoNames
WEATHER_API_KEY = '2703290a2ce7e24c668bd3dc8696d8cc'  # API Key de OpenWeatherMap

# Lista de países soportados
paises = ["Argentina", "México", "Colombia"]

# GeonameId para países
geonames_ids = {
    "Argentina": 3865483,  # geonameId de Argentina
    "México": 3996063,  # geonameId de México
    "Colombia": 3686110  # geonameId de Colombia
}

# Función para obtener los departamentos de un país usando GeoNames
def get_departamentos(pais):
    try:
        geoname_id = geonames_ids.get(pais)
        response = requests.get(f"http://api.geonames.org/childrenJSON?geonameId={geoname_id}&username={GEONAMES_USER}")
        data = response.json()
        departamentos = [item['name'] for item in data['geonames']]
        return departamentos
    except Exception as e:
        print(f"Error al obtener departamentos: {e}")
        return []

# Función para obtener las ciudades de un departamento usando GeoNames
def get_ciudades(departamento):
    try:
        response = requests.get(f"http://api.geonames.org/searchJSON?q={departamento}&adminCode1=&username={GEONAMES_USER}")
        data = response.json()
        ciudades = [item['name'] for item in data['geonames']]
        return ciudades
    except Exception as e:
        print(f"Error al obtener ciudades: {e}")
        return []

# Función para obtener la recomendación del clima
def get_weather_recommendation(pais, ciudad, fecha, hora):
    try:
        dt_str = f"{fecha} {hora}"
        dt = datetime.strptime(dt_str, "%m/%d/%y %H:%M")
        timestamp = int(dt.timestamp())
        
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={WEATHER_API_KEY}")
        data = response.json()
        temp = data['main']['temp'] - 273.15  # Convertir de Kelvin a Celsius
        
        if temp < 10:
            return 'Clima frío, usa protector solar, guantes, botas, paraguas y ropa abrigada'
        elif temp < 20:
            return 'Clima templado, usa ropa cómoda, camiseta o camisa manga larga, protector solar, lleva abrigo para la tarde'
        else:
            return 'Clima caluroso, usa ropa ligera, protector solar, sombrero. Recuerda hidratarte'
    except Exception as e:
        print(f"Error al obtener recomendación del clima: {e}")
        return 'No se puede obtener recomendación del clima.'

        # Llamada a la API de OpenWeatherMap para obtener el clima actual
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={WEATHER_API_KEY}")
        data = response.json()
        temp = data['main']['temp'] - 273.15  # Convertir de Kelvin a Celsius
        
        # Determinar la recomendación en función de la temperatura
        if temp < 10:
            return 'Clima frío, usa protector solar, guantes, botas, paraguas y ropa abrigada'
        elif temp < 20:
            return 'Clima templado, usa ropa cómoda, camiseta o camisa manga larga, protector solar, lleva abrigo para la tarde'
        else:
            return 'Clima caluroso, usa ropa ligera, protector solar, sombrero. Recuerda hidratarte'
    except Exception as e:
        print(f"Error al obtener recomendación del clima: {e}")
        return 'No se puede obtener recomendación del clima.'
