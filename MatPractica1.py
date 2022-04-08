M={5,20,3,10}
A={46,20,10,14}
B={0,3,10,14}
U={1}

#Muestro los conjuntos
print(f"Los conjuntos son: /n M={M}, A={A}, B={B} y U={U}\n")
#Funcion in

print("Funcion in. Busco si 5 esta en el conjunto M: ")
print(5 in M, end=" \n")

#Funcion len
print("Funcion len. Muestro el modulo de A: ")
print(len(A))

#Funcion not
print("Funcion not. Muestro si 10 no esta en B: ")
print(10 not in B, end= "\n")

#Funcion add
print("Funcion add. Añado un elemento al conjunto U: ")
print(U.add('x'), end=" \n")

#Funcion remove
print("Funcion remove. Elimino un elemento al conjunto U: ")
print(U.remove('x'), end=" \n")

#Funcion intersection
print("Funcion intersection. Muestro la interseccion entre B y A: ")
print(B&A, end=" \n")

#Funcion union
print("Funcion union. Muestro la union entre M y A: ")
2
print(M|A, end=" \n")

#Funcion diferencia -
print("Funcion diferencia. Aplico la funcion diferencia entre A y B: ")
print (A-B, end=" \n")

#Funcion ^
print("Funcion diferencia. Aplico la funcion diferencia simetrica entre A y B: ")
print(A^B, end= " \n")

#Funcion issubset
print("Funcion issubset. Muestro si M es un subconjunto de A: ")
print(M.issubset(A), end=" \n")
