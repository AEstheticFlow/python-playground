import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

# https://home.openweathermap.org/api_keys
# API key = 9d9e0a8320ac66db9dcc5173257fed92
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # --- Widgets ---
        self.city_label = QLabel("Enter a city name:", self)
        self.city_line = QLineEdit(self)
        self.weather_button = QPushButton("Get weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.describe_label = QLabel(self)

        self.initUI()
        
    def initUI(self):
        """Set up UI layout and styling."""
        # --- Layout ---
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_line)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.describe_label)
        self.setLayout(vbox)

        # --- Alignment ---
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_line.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.describe_label.setAlignment(Qt.AlignCenter)

        # --- Object Names (used for targeted CSS) ---
        self.city_label.setObjectName("city_label")
        self.city_line.setObjectName("city_line")
        self.weather_button.setObjectName("weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.describe_label.setObjectName("describe_label")

        # --- Styling with Qt Style Sheets ---
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_line{
                font-size: 40px;            
            }
            QPushButton#weather_button{
                font-size: 30px;
                font-weight: bold;           
            }
            QLabel#temp_label{
                font-size: 75px;      
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;          
            }
            QLabel#describe_label{
                font-size: 50px;         
            }
        """)

        # --- Signal Connection (Button -> Fetch Weather) ---
        self.weather_button.clicked.connect(self.get_weather)

    # ------------------------------
    # Fetching and Handling Weather
    # ------------------------------
    def get_weather(self):
        """Fetch weather data from OpenWeather API."""
        api_key = "9d9e0a8320ac66db9dcc5173257fed92"
        city_name = self.city_line.text().strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()     # Raises HTTPError for bad responses
            data = response.json()          # Data is now a dictionary we can work with
            # print(data)

            if data["cod"] == 200:          # Successful response
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")

        except requests.exceptions.RequestException as req_error:     # Final resort
             self.display_error(f"Request Error:\n{req_error}")
        

    # ------------------------------
    # UI Helpers
    # ------------------------------
    def display_error(self, message):
        """Display error message inside the temp_label."""
        self.temp_label.setStyleSheet("font-size: 40px; color: red;")
        self.temp_label.setText(message)

        self.emoji_label.clear()        # To clear any remains from a previous successful req
        self.describe_label.clear()
    

    def display_weather(self, data):
        """Update UI with fetched weather data."""
        # print(data)

        # --- Temperature (Kelvin → Celsius) ---
        # I'm accessing a key inside a key in `data` dict
        temp_k = data["main"]["temp"] 
        temp_c = temp_k - 273
        self.temp_label.setStyleSheet("font-size: 75px; color: black;")
        self.temp_label.setText(f"{temp_c:.0f}°C")

        # --- Weather Description ---
        # I'm accessing a key inside a list inside a key in `data` dict
        weather_description = data["weather"][0]["description"]
        self.describe_label.setText(weather_description)

        # --- Emoji (Based on Weather ID codes) ---
        # I'm accessing a key inside a list inside a key in `data` dict
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))


    @staticmethod
    def get_weather_emoji(weather_id):
        """Map OpenWeather condition codes to emojis."""
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""        
        
# ------------------------------
# Application Entry Point
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=Q4377DH5Jso&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=90