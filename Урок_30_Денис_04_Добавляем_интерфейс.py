from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,languag='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2) # Округляем до 2-х знаков после запятой
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            return "Город не найден"

    except Exception as e:
        return (f"Возникла ошибка: {e}")


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")


key = 'b4cee9ecd4a341f485dc41cb649887cb'

window=Tk()
window.title("Координаты городов")
window.geometry("200x100")

entry = Entry()
entry.pack()

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите на кнопку")
label.pack()

window.mainloop()
