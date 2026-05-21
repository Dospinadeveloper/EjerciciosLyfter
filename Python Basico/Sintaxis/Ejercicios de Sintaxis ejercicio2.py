first_name = input("Escribe tu nombre: ")
last_name = input("Escribe tu apellido: ")
age = int(input("Escribe tu edad: "))

# Etapa de vida
if age < 2:
    stage = "un bebé"
elif age < 12:
    stage = "un niño"
elif age < 14:
    stage = "un preadolescente"
elif age < 18:
    stage = "un adolescente"
elif age < 26:
    stage = "un adulto joven"
elif age < 60:
    stage = "un adulto"
else:
    stage = "un adulto mayor"


print(f"Hola {first_name} {last_name}, según tu edad, eres {stage}.")