
paciente = []

proceso = int(input("Ingrese su dni o -1 para terminar: "))
if proceso != -1:
    while proceso == 0:
        dni = 0
        paciente.append(dni)
        nombyapel = input("Ingrese el nombre y apellido del paciente: ")
        paciente.append(nombyapel)
        #dni = int(input("Ingrese el dni del paciente: "))
        #paciente.append(dni)
        mail = input("Ingrese el mail del paciente: ")
        paciente.append(mail)
        part = int(input("Ingrese 1 si es un particular o 2 si posee una obra social: "))
        paciente.append(part)
        proceso = int(input("Ingrese 0 para continuar o cualquier numero para terminar: "))
else:
    print(paciente)


