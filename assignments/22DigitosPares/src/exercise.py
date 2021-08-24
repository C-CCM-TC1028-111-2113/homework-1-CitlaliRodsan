def main():
    #escribe tu código abajo de esta línea
    
    num = input("Dame un número: ")
    
    if int(num[0])%2==0:
        if int(num[1])%2==0:
            if int(num[2])%2==0:
                if int(num[3])%2==0:
                    par=4
            else:
                par=3
        else:
            par=2
    else:
        par=1

    print("El número de dígitos pares es:", par)

if __name__ == '__main__':
    main()
