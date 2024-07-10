import random
import csv
import statistics

#opcion 1
def asignar_sueldos_aleatorios(trabajadores_sueldos, trabajadores):

    if not trabajadores_sueldos:
        for trabajador in trabajadores:
            sueldo=random.randint(300000,2500000)
            trabajadores_sueldos[trabajador]= sueldo

        print("\nSueldos asignados correctamente!")
        print("volviendo al menú principal...")
        return trabajadores_sueldos
    
    else:
        print("\nLos sueldos ya estan Asignados, volviendo al menú principal...")
        return
    
#opcion 2
def clasificar_sueldos(trabajadores_sueldos):
    if not trabajadores_sueldos:
        print("\nDebe asignar los sueldos de los trabajadores antes de clasificar los sueldos!")
        print("volviendo al menú principal...")
        return
    
    else:
        
        total=0
        cont_800=0
        cont_800_2000=0
        cont_2000=0

        for trabajador,sueldo in trabajadores_sueldos.items():
            if sueldo<800000:
                cont_800=cont_800+1
                total = total + sueldo
            elif sueldo>=800000 and sueldo<=2000000:
                cont_800_2000=cont_800_2000+1
                total = total + sueldo
            elif sueldo>2000000:
                cont_2000=cont_2000+1
                total = total + sueldo

        print(f"\nSueldos menores a 800000 TOTAL: {cont_800}")
        print("Nombre del empleado\tSueldo")
        for trabajador,sueldo in trabajadores_sueldos.items():
            if sueldo<800000:
                print(f"{trabajador}\t\t{sueldo}")
                
        print(f"\nSueldos entre 800.000 y 2.000.000 TOTAL: {cont_800_2000}")
        print("Nombre del empleado\tSueldo")
        for trabajador,sueldo in trabajadores_sueldos.items():
            if sueldo>=800000 and sueldo<=2000000:
                print(f"{trabajador}\t\t{sueldo}")
                
        print(f"\nSueldos mayores a 2.000.000 TOTAL: {cont_2000}")
        print("Nombre del empleado\tSueldo")
        for trabajador,sueldo in trabajadores_sueldos.items():
            if sueldo>2000000:
                print(f"{trabajador}\t\t{sueldo}")

        print(f"\nEl total de sueldos es: {total}")
        print("\nvolviendo al menú principal...")

#opcion 3
def ver_estadisticas(trabajadores_sueldos):

    if not trabajadores_sueldos:
        print("\nDebe asignar los sueldos de los trabajadores antes de ver sus estadisticas!")
        print("volviendo al menú principal...")
        return
    
    else:
        min_max(trabajadores_sueldos)
        promedio(trabajadores_sueldos)
        media_geometrica(trabajadores_sueldos)
        print("\nvolviendo al menú principal...")
    return

def min_max(trabajadores_sueldos):

    trabajador_min=None
    min=2000000
    trabajador_max=None
    max=300000

    for trabajador,sueldo in trabajadores_sueldos.items():

        # menor
        if sueldo <= min:
            min = sueldo
            trabajador_min = trabajador

        # mayor
        if sueldo >= max:
            max = sueldo
            trabajador_max = trabajador

    print(f"\nEl sueldo mas bajo pertenece a: {trabajador_min}")
    print(f"Su sueldo es de: ${min}")

    print(f"\nEl sueldo mas alto pertenece a: {trabajador_max}")
    print(f"Su sueldo es de: ${max}")
    return

def promedio(trabajadores_sueldos):

    total=0 
    cont=0
    for trabajador, sueldo in trabajadores_sueldos.items():
        total = total + sueldo
        cont=cont+1
    prom = total/cont

    print(f"\nEl promedio de los sueldos es: ${prom}")
    return

def media_geometrica(trabajadores_sueldos):

    # total=1 
    # cont=0
    # for trabajador, sueldo in trabajadores_sueldos.items():
    #     total = total * sueldo
    #     cont=cont+1
    # media_geo=(total**cont/2)//1

    # print(f"\nLa media geometica de los sueldos es: ${media_geo}")
    # return

    total=[] 
    cont=0
    for trabajador, sueldo in trabajadores_sueldos.items():
        total.append(sueldo)
        cont=cont+1
    
    media_geo=statistics.geometric_mean(total)

    print(f"\nLa media geometica de los sueldos es: ${media_geo}")
    return


#opcion 4
def reporte_sueldos(trabajadores_sueldos):

    if not trabajadores_sueldos:
        print("\nDebe asignar los sueldos de los trabajadores antes de crear un reporte sueldos!")
        print("volviendo al menú principal...")
        return
    
    else:
        with open("archivo.csv","w",newline="") as archivo:
            escritor = csv.writer(archivo,delimiter=" ")

            escritor.writerow("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")

            for trabajador,sueldo in trabajadores_sueldos.items():

                descuento_salud=sueldo*0.07
                descuento_AFP=sueldo*0.12
                sueldo_liquido=sueldo-(descuento_salud+descuento_AFP)
                
                escritor.writerow(f"{trabajador},{sueldo},{descuento_salud},{descuento_AFP},{sueldo_liquido}")

    

        print("\nNombre empleado\t\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
        for trabajador,sueldo in trabajadores_sueldos.items():

            descuento_salud=sueldo*0.07
            descuento_AFP=sueldo*0.12
            descuento_salud=int(descuento_salud)
            descuento_AFP=int(descuento_AFP)
            sueldo_liquido=sueldo-(descuento_salud+descuento_AFP)

            print(f"{trabajador}\t\t{sueldo}\t\t{descuento_salud}\t\t{descuento_AFP}\t\t{sueldo_liquido}")
        
        print("\nReporte de sueldos Generado con exito!")
        print("volviendo al menú principal...")
        return