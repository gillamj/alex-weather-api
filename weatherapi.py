from pgeocode import Nominatim
from json import loads
from requests import get
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import pycountry as pc

window = tk.Tk()
entry = tk.StringVar()
zip_title = ""

global daytemp, nighttemp

def clear_screen():

    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.pack_forget()


def label_invalid():
    window.geometry("1400x1000")
    button_file.pack_forget()
    tk.Label(window, text="Not a valid zip code. Please try entering your zip code again.",
    font=('Cascadia Code', 9, 'bold'), fg="red", bg="black").pack()
    invalidpic.pack()


def label_validzip():
    window.geometry("900x600")
    button_file.pack_forget()
    tk.Label(window, text="Forecast loaded. Please select a file location for export.",
    font=('Cascadia Code', 9, 'bold'), fg="blue", bg="black").pack()
    button_file.pack()
    validpic.pack()


def label_complete():
    window.geometry("900x700")
    button_file.pack_forget()
    tk.Label(window, text="Forecast has been exported!",
    font=('Cascadia Code', 9, 'bold'), fg="green", bg="black").pack()
    button_file.pack()
    completepic.pack()


def get_temp(counter, url):
    forecast = get(url).text
    forecast = loads(forecast)
    forecast = forecast['properties']
    forecast = forecast['periods']
    number = len(forecast)
    forecast = forecast[counter]
    dayind = forecast['isDaytime']
    forecast = forecast['temperature']
    return forecast, number, dayind


def save():
    day = submit(1)
    night = submit(1)
    count = day[2]
    file = filedialog.asksaveasfile(initialdir = "C:/",
                                    filetypes = (("Text files",
                                                "*.txt*"),
                                                ("all files",
                                                "*.*")),
                                    defaultextension = "txt")
    x = 0
    file.write((str(day[3])) + " 7-Day Forcast" + '\n')
    while x < count / 2:
        if len(str((day[0][x]))) == 2:
            file.write("Day " + str(x + 1) + " High: " + str((day[0][x])) + "   |   Low: " + str(night[1][x]) + '\n')
        elif len(str((day[0][x]))) == 3:
            file.write("Day " + str(x + 1) + " High: " + str((day[0][x])) + "  |   Low: " + str(night[1][x]) + '\n')
        elif len(str((day[0][x]))) == 1:
            file.write("Day " + str(x + 1) + " High: " + str((day[0][x])) + "    |   Low: " + str(night[1][x]) + '\n')
        x += 1
    clear_screen()
    label_complete()



def submit(save_indicator):
    global daytemp, nighttemp, countnum, citystate
    if save_indicator == 0:
        try:
                y = country.get()
                nomi = Nominatim(y)
                x = entry.get()
                long = nomi.query_postal_code(x).latitude
                lat = nomi.query_postal_code(x).longitude
                city = nomi.query_postal_code(x).place_name
                state = nomi.query_postal_code(x).state_name
                cn = pc.countries.get(alpha_2=y).name
                title = str(city) + ", " + str(state) + ", " + str(cn)

                url = "https://api.weather.gov/points/" + str(long) + "," + str(lat)

                getstation = get(url).text

                pretty = loads(getstation)
                properties = pretty['properties']

                gridId = properties['gridId']
                gridX = properties['gridX']
                gridY = properties['gridY']

                forecasturl = "https://api.weather.gov/gridpoints/" + str(gridId) + "/" + str(gridX) + "," + str(gridY) + \
                              "/forecast"

                x = 0
                count = get_temp(x, forecasturl)[1]
                countnum = count
                daytemplist = []
                nighttemplist = []

                while x < count:
                    if get_temp(x, forecasturl)[2] is False:
                        nighttemplist.append(get_temp(x, forecasturl)[0])
                    else:
                        daytemplist.append(get_temp(x, forecasturl)[0])
                    x += 1

                clear_screen()
                label_validzip()
                daytemp = daytemplist
                nighttemp = nighttemplist
                citystate = title

        except (KeyError, ValueError):
            clear_screen()
            label_invalid()

    else:
        return daytemp, nighttemp, countnum, citystate


entryimage = ImageTk.PhotoImage(Image.open("images/thunderstorm.jpg"))
validimage = ImageTk.PhotoImage(Image.open("images/europewinter.webp"))
invalidimage = ImageTk.PhotoImage(Image.open
("images/foggy.jpg"))
completeimage = ImageTk.PhotoImage(Image.open("images/shutterstock.jpg"))

window.title("Entry Window")
window.geometry("800x600")
window.configure(bg="black")

label = tk.Label(window, text="Select Country:", bg="black", fg="white")
label.pack()

country = tk.StringVar()
countryvalues = sorted(
        [(country.alpha_2) for country in pc.countries],
        key=lambda x: x[1]
    )
countryvalues.remove('US')
countryvalues.insert(0, 'US')
countrydropdown = tk.OptionMenu(window, country, *countryvalues)
countrydropdown.configure(bg="black", fg="white")
countrydropdown.pack()

label = tk.Label(window, text="Enter Zip Code:", bg="black", fg="white")
label.pack()

entry = tk.Entry(window, bg="black", fg="white")
entry.pack()

button = tk.Button(window, text="Submit", command=lambda: submit(0), bg="black", fg="white")
button.pack()

button_file = tk.Button(window, text="Export", command=save, bg="black", fg="white")

entrypic = tk.Label(window, image=entryimage)
entrypic.pack()

validpic = tk.Label(window, image=validimage)

invalidpic = tk.Label(window, image=invalidimage)

completepic = tk.Label(window, image=completeimage)

window.mainloop()





