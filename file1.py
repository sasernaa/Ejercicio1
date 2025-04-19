while(1 != 0):
    retirar = int(input("Ingrese la cantidad que desea retirar: "))
    if(retirar < 0):
        print("El numero digitado es negativo")
    else:
        billetes_de_5 = 0
        billetes_de_2 = 0
        billetes_de_1 = 0
        mensaje = "Recibira:"
            
        #Voy a repartir los billetes de 5

        billetes_de_5 = int(retirar/5)
        if(billetes_de_5 != 0):
            mensaje += f"\n{billetes_de_5} billetes de 5"

        retirar = retirar - (billetes_de_5*5)

        #Voy a repartir los billetes de 2

        billetes_de_2 = int(retirar/2)
        if(billetes_de_2 != 0):
            mensaje += f"\n{billetes_de_2} billetes de 2"
        retirar = retirar - (billetes_de_2*2)

        #Voy a repartir los billetes de 1

        billetes_de_1 = retirar
        if(billetes_de_1 != 0):
            mensaje += f"\n{billetes_de_1} billetes de 1"
        print(mensaje)

    