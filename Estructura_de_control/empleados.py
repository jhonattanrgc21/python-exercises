# Modulos
import os

# Entrada
n = int(input("Ingrese la cantidad de empleados> ")) # Cantidad de empleados de la empresa

# Proceso 
empleados_h = 0 # Cantidad de empleados hombres
empleados_f = 0 # Cantidad de empleados femeninos
hom_casados = 0 # Hombres casados que ganan mas de 10.000
muj_viudas = 0 # Cantidad de mujeres viudas que ganan 5000
acum_edad = 0 # Acumulador de edad de los hombres
cont_casadas = 0 # Cantidad de mujeres casadas
cont_divorciadas = 0 # Cantidad de mujeres divorciadas
cont_viudas = 0 # Cantidadde mujeres viudas
for i in range(n):
    os.system("clear")
    print("Empleado", (i + 1))

    # Validacion de la edad
    while True:
        edad = float(input("\nIngrese la edad: ")) # Ingresos del empleado
        if edad > 0:
            break

    # Validacion del valor del sueldo
    while True:
        sueldo = float(input("\nIngrese su sueldo: ")) # Ingresos del empleado
        if sueldo > 0:
            break
        
    # Mmenu del estado civil
    while True:
        print("Estado civil del empleado")
        print("1- Soltero/a")
        print("2- Casado/a")
        print("3- Divorciado/a")
        print("4- Viudo/a") 
        estado_c = int(input("Seleccion: ")) # Estado civil del empleado
        if estado_c > 0 and estado_c < 5:
            break
    
    # Mmenu del genero del empleado
    while True:
        print("\nGenero del empleado")
        print("1- Masculino")
        print("2- Femenino")
        sexo = int(input("Seleccion: ")) # Sexo del empleado
        if sexo > 0 and sexo < 3:
            break
    
    
    if sexo == 1:
        empleados_h += 1
        acum_edad += edad
        if estado_c == 2 and sueldo > 10000:
            hom_casados += 2
    else:
        empleados_f += 1
        if estado_c == 2:
            cont_casadas += 1
        elif estado_c == 3:
            cont_divorciadas += 1
        elif estado_c == 4:
            cont_viudas += 1
            if sueldo == 5000:
                muj_viudas += 1

# Salida
os.system("clear")
print("Total de empleados femeninos:", empleados_f)
print("Hombres casados que ganan mas de 10.000:", hom_casados)
print("Mujeres viudas que ganan 5000:", muj_viudas)
print("Edad promedio de los hombres:", (acum_edad / empleados_h))
print("Procentaje de mujeres casadas:", (cont_casadas / empleados_f) * 100)
print("Procentaje de mujeres divorciadas:", (cont_divorciadas / empleados_f) * 100)
print("Procentaje de mujeres viudas:", (cont_viudas / empleados_f) * 100)