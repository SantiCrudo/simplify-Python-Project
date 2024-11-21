#Consultar y registrar MASCOTAS

import os

REGISTRAR = 1
CONSULTAR = 2
SALIR = 0

def mostrar_menu():
    os.system("cls")
    print(f"""          Mis Mascotas 
    {REGISTRAR}) Registrar una mascota
    {CONSULTAR}) Consultar mascotas
    {SALIR}) Salir""")

def registrar_mascota(mascotas):
    os.system("cls")
    print("                 Registrar Mascota")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso: "))
    tipo = input("Tipo: ")
    mascotas.append( (nombre,edad,peso,tipo) )

def consultar_mascotas(mascotas):
    os.system("cls")
    print("                 Mis Mascotas")
    if len(mascotas) == 0:
        print("Aun no has registrado mascotas")
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad}")
            print(f"Peso: {peso}")
            print(f"Tipo: {tipo}")
            print("___________" * 8)

def main():
    mis_mascotas = []
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input("Selecciona una opcion: "))
        if opc == REGISTRAR:
            registrar_mascota(mis_mascotas)
        elif opc == CONSULTAR:
            consultar_mascotas(mis_mascotas)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opcion no valida")
        input("Presiona enter para continuar...")

    input("Nos vemos")

if __name__ == "__main__":
    main()


