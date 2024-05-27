asterisco = int(input("Ingresa la altura de la piramide: "))
k = 0
for i in range(1, asterisco+1):
    for space in range(1, (asterisco-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1  
    k = 0
    print()
print("la altura de la piramide es=", asterisco)
