# Weather App with Zip Code and Country Lookup

This Python app allows users to retrieve weather information based on a provided zip code and country. It uses the `weather.com` API, and utilizes several libraries such as `tkinter`, `requests`, `json`, `PIL`, `pgeocode`, and `pycountry` for the following functionalities:

- **Tkinter**: Provides the graphical user interface (GUI) for the user to input their zip code and country.
- **Requests**: Handles API calls to weather.com to retrieve weather data.
- **JSON**: Parses the data returned from the weather.com API.
- **Pillow (PIL)**: Used to display any weather-related images (like icons or backgrounds) in the app.
- **Pgeocode**: Retrieves latitude and longitude coordinates for the user-provided zip code and country.
- **Pycountry**: Helps with validating and converting country codes into a standardized format.

### How It Works

1. **User Input**: The user provides a zip code and a country code (e.g., "US" for the United States).
2. **Coordinates Retrieval**: The app uses `pgeocode` to fetch the latitude and longitude for the given zip code and country.
3. **Weather Data**: Using the retrieved coordinates, the app makes an API call to weather.com to fetch the weather data.
4. **Display**: The app displays the weather information in the GUI, including the temperature, humidity, and weather conditions. If available, weather icons are displayed using `Pillow` (PIL).

### Folder Structure
```/alex-website
├── /images
│   └── europewinter.webp # Europe winter image
│   └── foggy.jpg         # Foggy image
│   └── shutterstock.jpg  # Shutterstock image
│   └── thunderstorm.jpg  # Thunderstorm image
├── README.md             # Project description (this file)
└── weatherapi.py         # Main .py
```
### Requirements

Make sure to install the following Python libraries before running the application:

```bash
pip install tkinter requests json Pillow pgeocode pycountry
