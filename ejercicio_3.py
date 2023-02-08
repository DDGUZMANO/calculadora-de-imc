nombre = input("Hola, ingrese su nombre por favor: ")
peso = int(input(f'hola {nombre} ingresa tu peso en Kg por favor: '))
estatura = float(input (f'ahora ingressa tu estatura en metros por favor: '))
# respuesta = input('Quieres saber tu indice de masa corporal?')
print('tu indice de masa corporal es: ')
imc = peso / (estatura**2)
print(round(imc,2))





