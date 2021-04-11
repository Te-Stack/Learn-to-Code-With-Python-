class WeatherForecast():
    def __init__(self,temperatures):
        self.temperatures = temperatures
    
    @staticmethod
    def convert_from_fahrenheit_to_celsuis(fahr):
        calculation = (5/9) * (fahr - 32)
        return round(calculation, 2)

    def in_celcuis(self):
        Quincy = [ self.convert_from_fahrenheit_to_celsuis(temp) for temp in self.temperatures ]
        return Quincy




wf = WeatherForecast([100,90,41,52])
print(wf.in_celcuis())


print(WeatherForecast.convert_from_fahrenheit_to_celsuis(100))


