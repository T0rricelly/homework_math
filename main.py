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

Anguloa= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
Angulob= math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
Anguloc= 180-(Anguloa+Angulob)

if Anguloa==90 or Angulob==90 or Anguloc==90:
    print(f"su triangulo tiene un angulo de 90°\es un triangulo rectanguulo\nAngulo A--> {Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C--> {Anguloc}°")
elif Anguloa>90 or Angulob>90 or Anguloc>90:
    print(f"Su triangulo tiene un angulo mayor a 90°\nes un triangulo obtusangulo\Angulo A--> {Anguloa}°\nAngulo B-->{Angulob}°\nAngulo C-->{Anguloc}°hhhh")
else:
    print(f"Su triangulo no tiene angulos mayores o iguales a 90°\es un angulo acutangulo\nAngulo A-->{Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C-->{Anguloc}°")