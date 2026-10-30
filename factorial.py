 def play(numero):
     intento = int(input("Adivina el numero: "))

     if intento == numero:
         print("Correcto')
    elif intento < numero:
       print("El numero es mayor")
    else:
       print("El numero es menor")

    play(10)
