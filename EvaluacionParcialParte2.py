def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)

def opcion_mcd():
    print("CALCULO DE MCD")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = calcular_mcd(a, b)
    print(f"El MCD de {a} y {b} es: {resultado}")

def cadena_repetida(palabra, n):
    if n <= 1:
        return palabra
    else:
        return palabra + cadena_repetida(palabra, n - 1)

def opcion_cadena():
    palabra = input("Ingrese una palabra: ")
    n = int(input("¿Cuántas veces desea repetirla?: "))
    resultado = cadena_repetida(palabra, n)
    print("Resultado:", resultado)


def contar_letra(cadena, letra):
    if not cadena:
        return 0
    elif cadena[0] == letra:
        return 1 + contar_letra(cadena[1:], letra)
    else:
        return contar_letra(cadena[1:], letra)

def opcion_contar_letras():
    cadena = input("Ingrese una palabra o frase: ")
    letra = input("Ingrese la letra a contar: ")
    resultado = contar_letra(cadena, letra)
    print(f"La letra '{letra}' aparece {resultado} veces.")


def opcion_decimal_binario():
    numero = int(input("Ingrese un número decimal: "))
    if numero == 0:
        print("Resultado: 0")


def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

def opcion_contar_digitos():
    numero = int(input("Ingrese un número: "))
    resultado = contar_digitos(numero)
    print(f"El número tiene {resultado} dígito(s).")


def menu():
    print("\n************* MENÚ *************")
    print("1. Calcular el MCD de dos números")
    print("2. Cadena repetida N veces")
    print("3. Contar cuántas veces aparece una letra en una cadena")
    print("4. Convertir un número decimal a binario")
    print("5. Calcular cuántos dígitos tiene un número")
    print("0. Salir")


def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            opcion_mcd()
        case 2:
            opcion_cadena()
        case 3:
            opcion_contar_letras()
        case 4:
            opcion_decimal_binario()
        case 5:
            opcion_contar_digitos()
        case 0:
            print("Saliendo del programa...")
        case _:
            print("Opción no válida.")


def main():
    opcion = -1
    while opcion != 0:
        menu()
        try:
            opcion = int(input("Elige una opción (0-5): "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor ingresa un número válido.")

if __name__ == "__main__":
    main()