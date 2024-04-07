def menu():
    while True:
        try: 
            print('1: Localizar una cadena especificada.')
            print('2: Borrar una subcadena.')
            print('3: Insertar una subcadena en una posición especificada.')
            print('4: Sustituir una subcadena por otra.')
            opcion = int(input('Seleccion: '))
            
            if(opcion < 1 or opcion > 4): 
                print('Error, opcion invalida.')
                continue
            
            break
        except ValueError:
            print('Error, debe ingresar un numero entero.')
    return opcion

def buscar_subcadena(cad, sub_cad):
    index = cad.find(sub_cad)
    if(index == -1): print('{} no se encuentra en {}'.format(sub_cad, cad))
    else: print('La sub cadena se encuentra en la posicion: ', index + 1)

def borrar_subcadena(cad: str, sub_cad: str):
    cad = cad.replace(sub_cad, '')
    print(cad)

def agregar_subcadena(cad:str, sub_cad):
    while True:
        try:
            posicion = int(input('Ingrese la posicion a insertar:'))
            if(posicion < 1 or posicion > len(cad) ): print('Error, debe ser un numero 1 y  ', len(cad))
            break
        except ValueError:
            print('Error, deben ser un numero entero.')
    
    posicion -= 1    
    parte_inicial = cad[:posicion]
    parte_final = cad[posicion:]
    print(parte_inicial + sub_cad + parte_final) 
    

def remplazar_subcadena(cad:str, sub_cad):
    cad_old = input('Ingrese la cadena a remplazar del texto original: ')
    cad = cad.replace(cad_old, sub_cad)
    print(cad)

def main():
    opcion = menu()
    
    cad = input('Ingrese una frase: ')
    sub_cad = input('Ingrese una sub frase: ')
    
    if opcion == 1:
        buscar_subcadena(cad, sub_cad)
    elif opcion == 2:
        borrar_subcadena(cad, sub_cad)
    elif opcion == 3:
        agregar_subcadena(cad, sub_cad)
    else: remplazar_subcadena(cad, sub_cad)

if __name__ == '__main__':
    main()