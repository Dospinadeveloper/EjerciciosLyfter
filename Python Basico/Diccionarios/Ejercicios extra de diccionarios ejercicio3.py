products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

totals = {}

for item in products:
    cat = item["category"]
    price = item["price"]
    # Si la categoría ya existe, suma el precio; si no, la crea con valor 0 y suma.
    totals[cat] = totals.get(cat, 0) + price

print(totals)
