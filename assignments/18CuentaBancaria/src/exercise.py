def main():
    #escribe tu código abajo de esta línea
    
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    mes = saldo-(cheques*13)+ingresos-egresos
    final = mes-(mes*0.075)

    print("El saldo final de la cuenta es:", final)
    
if __name__ == '__main__':
    main()
