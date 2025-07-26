paises={"Mexico","Brasil","España","Canada"}
print(paises)

varios={True,"UTD",33,3,14}
print(varios)

#Funciones u Operaciones
paises.add("México")
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")


#Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista
# y posteriormente mostrar en pantalla los email sin duplicar

resp="si"
emails=[]
while resp=="si":
    emails.append(input("Introduzca su email:"))
    resp=input("quiere agregar otro email?")

    print(emails)
    emails_set=set(emails)
    emails=list(emails_set)
    




