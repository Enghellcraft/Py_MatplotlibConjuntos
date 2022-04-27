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

import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
A=15
B=20
C=3
D=5
E=14
F=47
G=0
NC=1

fig = plt.figure(figsize=(5,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Motos', 'Autos', 'Bicicletas'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(D)
diagram.get_label_by_id('110').set_text(B)
diagram.get_label_by_id('111').set_text(A)
diagram.get_label_by_id('010').set_text(C)
diagram.get_label_by_id('011').set_text(E)
diagram.get_label_by_id('001').set_text(G)
diagram.get_label_by_id('101').set_text(F)

ax.text(-0.55, -0.42, NC)

plt.title("Medios de Transporte Preferidos")
plt.axis('on')
plt.show()


