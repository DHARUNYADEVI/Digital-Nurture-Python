class TemperatureConverter:
    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9
converter = TemperatureConverter()
print(
    "25°C =",
    converter.celsius_to_fahrenheit(25),
    "°F"
)
print(
    "77°F =",
    converter.fahrenheit_to_celsius(77),
    "°C"
)