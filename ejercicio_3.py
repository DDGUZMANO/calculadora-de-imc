nombre = input("Hola, ingrese su nombre por favor: ")
respuesta = input(f"Que bueno que estas acá. {nombre}, Deseas conocer su indice de masa corporal??: ")
if respuesta == "si" or respuesta =="Si" or respuesta == "SI" or respuesta == "sI":
    peso = int(input(f'{nombre} ingresa tu peso en Kg por favor: '))
    estatura = float(input (f'ahora ingresa tu estatura en metros por favor: '))
    print('tu indice de masa corporal es: ')
    imc = peso / (estatura**2)
    print(round(imc,2))
    
else: print("vuelva cuando tenga ganas de conocer su IMC")
if imc <= 18.5:
    print(f"Tienes que ganar peso =(")
elif imc > 18.5 and imc <= 24.9:
    print("Tu peso es ideal xD")
elif imc > 24.9 and imc <= 29.9:
    print(f"{nombre}, tienes sobre peso. Toca hacer dieta :(")
else: print("Nooo... Esos son niveles de obesidad. Vamos!! dieta y ejercicio desde ya!")





