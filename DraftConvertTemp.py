# Lab 4b: Thermal converter
# Elizabeth Matos
# 2023-09-21
# 2023-09-24
# 2023-09-26 Conversion
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
# Helped from Chegg did not helped
# AI helped with the doctest
# 1. The program converts temps between any scale

def celsius_to_delisle(celsius):
    return 100 - (celsius * 3/2)

def delisle_to_celsius(delisle):
    return (100 - delisle) * 2/3

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_newton(celsius):
    return celsius * 33/100

def newton_to_celsius(newton):
    return newton * 100/33

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 9/5

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5/9

def celsius_to_reaumur(celsius):
    return celsius * 4/5

def reaumur_to_celsius(reaumur):
    return reaumur * 5/4

def celsius_to_romer(celsius):
    return celsius * 21/40 + 7.5

def romer_to_celsius(romer):
    return (romer - 7.5) * 40/21

def convert_temp():
    temp_celsius = float(input("Temperature to convert: "))
    start_scale = input("Starting scale (C, D, F, K, N, Ra, Re, Ro): ")
    target_scale = input("Target scale (C, D, F, K, N, Ra, Re, Ro): ")
    print()
    
    if start_scale == target_scale:
        print(f"{temp_celsius:.2f}° {start_scale} = {temp_celsius:.2f}° {target_scale}")
        return
    
    conversion_functions = {
        ('C', 'D'): celsius_to_delisle,
        ('D', 'C'): delisle_to_celsius,
        ('C', 'F'): celsius_to_fahrenheit,
        ('F', 'C'): fahrenheit_to_celsius,
        ('C', 'K'): celsius_to_kelvin,
        ('K', 'C'): kelvin_to_celsius,
        ('C', 'N'): celsius_to_newton,
        ('N', 'C'): newton_to_celsius,
        ('C', 'Ra'): celsius_to_rankine,
        ('Ra', 'C'): rankine_to_celsius,
        ('C', 'Re'): celsius_to_reaumur,
        ('Re', 'C'): reaumur_to_celsius,
        ('C', 'Ro'): celsius_to_romer,
        ('Ro', 'C'): romer_to_celsius,
        ('F', 'K'): lambda x: celsius_to_kelvin(fahrenheit_to_celsius(x)),
        ('D', 'Ra'): lambda x: celsius_to_rankine(delisle_to_celsius(x) + 33.34),
        ('N', 'Re'): lambda x: celsius_to_reaumur(newton_to_celsius(x)),
        ('K', 'Ra'): lambda x: celsius_to_rankine(kelvin_to_celsius(x)),
        # Example of lambda-> x = lambda a: a + 10 print(x(5)) outputs: 15
    }
    
    if (start_scale, target_scale) in conversion_functions:
        converted_temp = conversion_functions[(start_scale, target_scale)](temp_celsius)
        print(f"{temp_celsius:.2f}° {start_scale} = {converted_temp:.2f}° {target_scale}")
    else:
        print("Invalid input scales. Please choose from the supported scales.")
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    convert_temp()