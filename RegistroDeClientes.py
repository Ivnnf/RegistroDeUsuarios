

listaRut=[]
listName=[]
listMail=[]
listEdad=[]
listFecha=[]
listComensales=[]

opcion=1

while opcion >0 and opcion <4:
    print("1.- Registrar Cliente")
    print("2.- Registro de reserva")
    print("3.- consultar cliente")
    print("4.- Salir")
    
    opcion=int(input(f"Eliga una opcion      \n    "))
    
    if opcion == 1:
        
        flagDatoCorrecto=False
        while flagDatoCorrecto==False:
            try:
                rut=int(input(f"Ingrese su rut   \n    "))
                listaRut.append(rut)
            except:
                  print("Rut Incorrecto")
            else:      
                if rut > 5000000 and rut < 99999999:
                      flagDatoCorrecto=True
                else:
                    print("Dato invalido")    
                      
        name=str(input(f"Ingrese su nombre:      \n    "))
        listName.append(name)
         
        mail=str(input(f"Ingrese su Mail            \n "))
        print(mail.find("@"))
        listMail.append(mail)      
        
        flagDatoCorrecto=False
        while flagDatoCorrecto==False:
            try:
                edad=int(input(f"Ingrese su edad       \n "))
                listEdad.append(edad)     
            except:
                print("Edad Invalida")
            else:
                if edad >18 and edad <110:
                    flagDatoCorrecto=True
                else:
                    print("La edad indicada debe ser entre 18 y 110 años")  
                              
        print("---------Cliente Registrado Exitosamente-----------") 
    
    if opcion == 2:
        
        reservar=1
        while reservar>0 and reservar <2:
            print("Desea hacer una reserva?")
            print("1.- Si  ")
            print("2.- No  ")
            reservar=int(input(f"Desea una reserva?      \n     "))
            
            if reservar==1:    
                rut01=int(input(f"Ingrese el rut registrado     \n    "))
                
                if rut01 in listaRut:
                    print("Usuario registrado")
                else:
                    print("Usuario No registrado")
                
                fechaReserva=str(input(f"Ingrese la fecha de la reserva:     \n "))      
                listFecha.append(fechaReserva)   
                
                reservaComensales=int(input(f"Ingre la cantidad de Comensales       \n     "))                                 
                listComensales.append(reservaComensales)
                
                print("---Reserva Guardada Exitosamente----")
                print(f"{listFecha}_{listComensales}comensales.")
    
    if opcion ==3:
        rut02=int(input("Ingrese el Rut del cliente a consultar"))
        if rut02 in listaRut:
            for i in range(len(listaRut)):
                if rut02==listaRut[i]:
                    print(f" Rut: {listaRut[i]}\nNombre: {listName[i]} \n Edad: {listEdad[i]}  \n Correo: {listMail[i]} \n Fecha de reserva: {listFecha[i]} \n Cantidad de comensales: {listComensales[i]}")
    
    if opcion==4:
        print("---------Cerrando sesion----------")