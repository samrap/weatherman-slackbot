class WeatherFormatter:
    def __init__(self, location, weather):
        self.location = location
        self.weather = weather

    def format_for_temperature(self):
        return "It is currently {}ºF in {}".format(
            self.get_temperature(),
            self.location
        )

    def format_for_weather(self):
        response = self.format_for_temperature()
        response += "\nMostly {} with {} humidity and {} wind.".format(
            self.get_detailed_status(),
            self.get_humidity_level(),
            self.get_wind_level()
        )

        return response

    def get_temperature(self):
        return int(round(self.weather.get_temperature('fahrenheit')['temp']))

    def get_detailed_status(self):
        return self.weather.get_detailed_status()

    def get_humidity_level(self):
        return str(self.weather.get_humidity()) + '%'

    def get_wind_level(self):
        wind = self.weather.get_wind('miles_hour')

        if wind['speed'] > 30:
            return 'strong'
        elif wind['speed'] < 30 and wind['speed'] > 12:
            return 'moderate'
        else:
            return 'light to no'
