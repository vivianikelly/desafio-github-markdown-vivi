class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32       

# Entrada do usuário
celsius = float(input())

fahrenheit = ConversorTemperatura.celsius_para_fahrenheit(celsius)
print(fahrenheit)