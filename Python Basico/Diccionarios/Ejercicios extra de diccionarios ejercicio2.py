employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"}
]

grouped = {}

for emp in employees:
    dept = emp["department"]
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(emp)

import pprint
pprint.pprint(grouped)
