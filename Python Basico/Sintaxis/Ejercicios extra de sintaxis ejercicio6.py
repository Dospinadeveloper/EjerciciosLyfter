fahrenheit = 0
kelvin = 0

#para celsius a fahrenheit se multiplica x 1.8 + 32
#para celsius a kelvin se le suman 273.15

number = int(input("Ingrese temperatura en Celsius "))

fahrenheit = (number * 1.8) + 32
kelvin = number + 273.15


print (f"{number} Grados Celsius son {fahrenheit} Grados Fahrenheit y {kelvin} Grados Kelvin" )


print (f"Fahrenheit: {fahrenheit}" )
print (f"Kelvin: {kelvin}" )
