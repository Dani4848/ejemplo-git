# Ejercicio 3
try:
    num = int(input("Ingrese un número entero: "))
    for repetición in range(num):
        print(num)
except ValueError:
    print("Ingrese un número entero")