"""Dada una cantidad en pesos, obtener la equivalencia en dolares asumiendo
que la unidad cambiaria es un dato desconocido"""

pesos=float(input("Ingrese la cantidad en en pesos-> "))
tasa=float(input("Digite la tasa de cambio->"))
tasaC=(pesos)/tasa
print(f"el cambio de pesos a dolares equivale a {tasaC}")