from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,languag='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2) # Округляем до 2-х знаков после запятой
            lng = round(results[0]['geometry']['lng'], 2)
            return lat, lng
        else:
            return "Город не найден"

    except Exception as e:
        return (f"Возникла ошибка: {e}")

key = 'b4cee9ecd4a341f485dc41cb649887cb'
city = "Химки"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
