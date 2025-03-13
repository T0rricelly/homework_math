import math

def main(lado1, lado2, lado3):
    if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
        print("No es un triangulo valido")
    else:
        print("Es un triangulo")
        
# Datos 
a = int(input("Ingrese el valor del lado a: "))
b = int(input("Ingrese el valor del lado b: "))
c = int(input("Ingrese el valor del lado c: "))

main(a, b, c)