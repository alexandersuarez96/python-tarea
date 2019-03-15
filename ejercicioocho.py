"""Diseña un programa que pida el valor del lado de un cuadrado y
muestre el valor de su perímetro y el de su área"""

lado=float(input("ingrese un lado del cuadrado "))
p=lado*4
area=lado**2
print ("el perimetro del cuadrado es {} y su area es de {} metros".format(p,area))