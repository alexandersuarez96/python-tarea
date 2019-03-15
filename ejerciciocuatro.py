"""calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio,
si la formula es :numpulsaciones=(220-edad)/10"""
nombre=input("Digite su nombre-->")
edad=int(input("Ingrese su edad"))
numpulsaciones=(220-edad)/10
print(f"el numero de pulsaciones que deberia  tener {nombre} por cada 10 segundo es {numpulsaciones}")