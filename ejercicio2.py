n = int(input("Escribir numero: ")) 

a,b = 0,1 #definimos a y b como 0 y 1 para futuras sumas 

print ("Serie de Fibonacci") #aqui imprimimos la serie 
 
if n < 1:
    print ("Numero demasiado pequeño")
elif n >= 1:
    print (a) #se imprime la secuencia de 1
    print (b) #Secuencia del numero 2 

#Empezamos con el bucle
for i in range(2,n):
    c = a + b #aqui hacemos la suma en una variable diferente que en este caso es c
    print (f"{a} + {b} = {c}")
    #se ocupa f para llamar a otras variables en la impresion, asi vemosnla suma que hace el programa
    a, b = b, c #aqui seria el resultado de 