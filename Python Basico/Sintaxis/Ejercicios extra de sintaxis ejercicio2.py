
time_in_seconds = 0
base_time = 600


time_in_seconds = int(input("Ingrese el tiempo en segundos " ) )

if time_in_seconds < base_time:
    print (f"Le faltan {base_time - time_in_seconds} para llegar a 10 minutos")
elif time_in_seconds > base_time:
    print ("Mayor")
else:
    print ("Igual")
    