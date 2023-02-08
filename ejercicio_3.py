nombre = input("Hola, ingrese su nombre por favor: ")
respuesta = input(f"Que bueno que estas acá. {nombre}, Deseas conocer su indice de masa corporal??: ")
if respuesta == "si" or respuesta =="Si" or respuesta == "SI" or respuesta == "sI":
    peso = int(input(f'{nombre} ingresa tu peso en Kg por favor: '))
    estatura = float(input (f'ahora ingressa tu estatura en metros por favor: '))
    print('tu indice de masa corporal es: ')
    imc = peso / (estatura**2)
    print(round(imc,2))
    
else: print("vuelva cuando tenga ganas de conocer su IMC")





