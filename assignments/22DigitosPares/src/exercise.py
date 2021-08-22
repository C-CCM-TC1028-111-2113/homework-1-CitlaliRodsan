def main():
    #escribe tu código abajo de esta línea
    pass

    num=input("Dame un número: ")
    if int(num[0])%2==0:
        if int(num[1])%2==0:
            if int(num[2])%2==0:
                if int(num[3])%2==0:
                    print("El número de dígitos pares es: 4")
            else:
                print("El número de dígitos pares es: 3 ")
        else:
            print("El número de dígitos pares es: 2 ")
    else:
            print("El número de dígitos pares es: 1 ")

if __name__ == '__main__':
    main()
