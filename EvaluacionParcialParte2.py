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
    if r == n:
        return n
    else:
        return resultado *= n


def ContarLetras(l,palabra):
    print("Bienvenido al conteo de letra: ")
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese la letra que desea ver cuantas veses se repite: ")


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
             print(f"\nEl MCD de ambos numeros es {mcd2}")
        case 2:
            print(f"\nResultado {CadenaRepetida(n) * CadenaRepetida(r)}")
        case 3:

        case 4:

        case 5:

        case _:

def main():
    opcion = 0
    while opcion != 5:
        menu()
        try:
            opcion = int(input("Elige una opción (1-5): "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor ingresa un número válido.")