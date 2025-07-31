def CalcMenu(a,b,resultado,mcd,mcd1):
    print("CALCULO DE MCD")
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    r1 = a % 2
    r2 = b % 2
    mcd = r1,r2



def CadenaRepetida(palabra,resultado,n,r=1):
    palabra = input("Ingrese una palabra: ")
    n = int(input("Cuantas veces desea repetirlo? "))



def ContarLetras(n,palabra):
    if n <= 1:
        return palabra
    else:
        return palabra + CadenaRepetida(palabra, n - 1)



def CalcDigitosNnumero(d):
    d = int(input("digite un numero"))


def menu():
    print("*************MENU*************")
    print("1. Calcular el MCD de dos numeros")
    print("2. Cadena repetida N veces")
    print("3. Contar cuantas veces aparece una letra en una cadena")
    print("4. Convertir un numero decimal a binario")
    print("5. Calcular cuantos digitos tiene un numero")


def ejecutar_opcion(opcion):
    match opcion:
        case 1:
             print(f"\nEl MCD de ambos numeros es: ")
        case 2:
            print(f"\nResultado ")
        case 3:
            palabra = input("Ingrese una palabra: ")
            n = int(input("¿Cuántas veces desea repetirla?: "))
            resultado = CadenaRepetida(palabra, n)
            print("Resultado:", resultado)
        case 4:
            print(f"\nResultado:")
        case 5:
            print(f"\nResultado:")
        case 0:
            print(f"\nResultado:")

def main():
    opcion = 0
    while opcion != 5:
        menu()
        try:
            opcion = int(input("Elige una opción (1-5): "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor ingresa un número válido.")