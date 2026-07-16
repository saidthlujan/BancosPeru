# ===========================================
# PROGRAMA: CAJERO AUTOMÁTICO
# Autor: (Escribir nombre del estudiante)
# ===========================================

saldo = 1000
pin_correcto = "1234"

print("===================================")
print("     BIENVENIDO AL CAJERO")
print("===================================")

pin = input("Ingrese su PIN: ")

if pin == pin_correcto:

    while True:

        print("\n===== MENÚ =====")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\nSu saldo es: S/ {saldo}")

        elif opcion == "2":

            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= saldo:
                saldo = saldo - monto
                print("Retiro realizado correctamente.")
                print(f"Nuevo saldo: S/ {saldo}")
            else:
                print("Saldo insuficiente.")

        elif opcion == "3":

            deposito = float(input("Ingrese el monto a depositar: "))
            saldo = saldo + deposito

            print("Depósito realizado correctamente.")
            print(f"Nuevo saldo: S/ {saldo}")

        elif opcion == "4":

            print("Gracias por utilizar el cajero.")
            break

        else:
            print("Opción no válida.")

else:
    print("PIN incorrecto.")