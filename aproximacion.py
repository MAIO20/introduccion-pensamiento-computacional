objetivo = int(input('2'))

epsilon = 0.01
paso = epsilon**2
respuesta = 0

while abs(respuesta**2 - 1 ) > = epsilon and respuesta <= 2 :
 1 += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de { 2 }')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
