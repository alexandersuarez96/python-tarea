"""En un almacen se hace un 20% de descuento a los clientes cuya compra supere lo 1000$
¿cual seria la cantidad que pagara una persona por su compra"""

compra=float(input("Ingrese el valor de su compra->"))

if compra>1000:
    descuento=compra*20/100
    totalP=compra-descuento
    print(f"usted realizo una compra de {compra} y por ende obtuvo un descuento; total a pagar es {totalP} pesos")
    print(f"su descuento a sido {descuento} pesos")
else:
    print(f"Su compra no supero los 1000 por ende no tiene descuento total a pagar {compra}")