import examen_funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López"
                ,"Ana Martínez","Pedro Rodríguez",
                "Laura Hernández","Miguel Sánchez",
                "Isabel Gómez","Francisco Díaz","Elena Fernández"]

trabajadores_sueldos={}

while True:

    try:
        print("")
        print(" -------------------------- ")
        print("|      Menú Principal      |")
        print(" -------------------------- ")
        print("1. Asignar sueldos aleatorios") 
        print("2. Clasificar sueldos") 
        print("3. Ver estadísticas") 
        print("4. Reporte de sueldos") 
        print("5. Salir del programa")
        opcion_menu=int(input("---> "))

        if opcion_menu==1:
            fn.asignar_sueldos_aleatorios(trabajadores_sueldos, trabajadores)

        elif opcion_menu==2:
            fn.clasificar_sueldos(trabajadores_sueldos)

        elif opcion_menu==3:
            fn.ver_estadisticas(trabajadores_sueldos)

        elif opcion_menu==4:
            fn.reporte_sueldos(trabajadores_sueldos)

        elif opcion_menu==5:
            print("\nFinalizando programa...")
            print("Desarrollado por Jeremías Silva")
            print("RUT: 21.436.727-0\n")
            break


        else:
            print("\nPorfavor Ingrese una opción de menú valida (1, 2, 3...)")
    except:
        print("\nPorfavor Ingrese una opción de menú valida (1, 2, 3...)")


