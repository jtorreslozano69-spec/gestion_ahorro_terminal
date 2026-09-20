import os
import sys
from decimal import Decimal

os.system("chcp 65001 > nul")

#aca puedes cambiar los nombres de las variables

losahorros = 0.00
Vueltos = 0.00
historial = []

#puedes cambiar los nombres de las opciones
while True: 
    print ("\n====GESTION AHORRO====\n1.Guardar dinero\n2.Retirar dinero\n3.Ver mi saldo\n4.historial\n5.salir")


    Accion_Principal = input ("elige una acción (1, 2, 3, 4 o 5): ")

    #opcion guardar dinero

    if Accion_Principal == "1":
        print ("Elegistes cuenta ahorro")

        while True:
                monto_a_guardar = float (input("Monto a guardar (cancela con 0): "))
            
                if monto_a_guardar == 0:
                    print ("Regresando")
                    break

                losahorros = losahorros + monto_a_guardar
                Vueltos = Vueltos + float(losahorros*0.10)
                print (f"monto a guardar {monto_a_guardar}")
                print (f"monto total {losahorros}")
                print (f"monto a vuelto {Vueltos}" )
                historial.append (f"se guardo {monto_a_guardar}, el total es de {losahorros}")
                break

    #opcion gastar dinero

    elif Accion_Principal == "2":
        print ("Elegistes retirar dinero")

        while True:
                monto_a_retirar =  float (input ("monto a retira (cancela con 0): "))

                if monto_a_retirar == 0:
                    print("regresando")
                    break

                losahorros=losahorros-monto_a_retirar
                print (f"el retiro fue de {monto_a_retirar}")
                print (f"monto total {losahorros}")
                historial.append (f"se retiro {monto_a_retirar}, el total es de {losahorros}")
                break

    elif Accion_Principal== "3":
        print("Aca vas a ver tu saldo de las cuentas")

        while True:
            Total = Vueltos + losahorros
            print (f"cuenta de ahorro: {losahorros}/S\ncuenta de vueltos: {Vueltos}/S\nTotal: {Total}")
            break
    elif Accion_Principal =="4":
        print("elegistes historial")

        if len(historial) == 0:
             print("No hay historial")
        else:
            for transaccion in historial:
                 print(transaccion)
        input("\nPresiona 3 para volver al menu principal: ")
    
    elif Accion_Principal =="5":
            os.system("cls")
            print("ADIOS")
            break

    else:
     print("OPCION INVALIDA")
     break