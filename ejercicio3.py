z = str(input("Inserte una palabra para invertir:"))#str es para definir una cadena, en input ponemos el input 
print (f"La palabra que ingresaste: {z}")

if len(z) == 1 or len(z) == 0: #comparamos la longitud de la cadena
    print (f"Tu palabra es muy corta o esta vacia, se imprime la misma palabra:{z}") #mandamos el mensaje de error 
else:
        palabra_invertida = z [::-1] #los dos puntos es para contar los elementos y el -1 recorre la secuencia de manera inversa
        print (f"La palabra inversa es: {palabra_invertida}") #imprime la palabra inversa