x = 10  

def fun():
	global x
	x = 20  
	experimental_variable = 0
	print(x)

fun()
print(x)

#Aquí intento acceder a experimental_variable declarada dentro de la funcion pero como estoy llamando desde afuera me sale el error de variable no definida
print(f"{experimental_variable}")