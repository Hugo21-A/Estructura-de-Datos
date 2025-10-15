c = int(input("Inserta el numero que quieras en factorial: "))

res = 1 #iniciamos la cuenta en 1 

for i in range(1, c + 1): #hacemos un rango o array para las comparativas
    res *= i #multiplicamos el resultado hasta que el tango llegue o sea igual a i que seria 1 descendiendo 
print (f"el factorial de {c} es {res}") #se imprime el resultado 

    