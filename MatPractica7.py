from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

ABC = 8
AB = 7 
AC = 8 
CB = 4 
A = 3 
B = 8
C = 12 
T = A + B + C + AB + AC + CB + ABC
U = 6 + T
NC = U - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('A', 'B', 'C'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(A)
diagram.get_label_by_id('110').set_text(AB)
diagram.get_label_by_id('111').set_text(ABC)
diagram.get_label_by_id('010').set_text(B)
diagram.get_label_by_id('011').set_text(CB)
diagram.get_label_by_id('001').set_text(C)
diagram.get_label_by_id('101').set_text(AC)

plt.text(0.65, 0.45, s="Conjunto A = " + str(A), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.35, s="Conjunto C = " + str(C), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.25, s="Complemento de A = " + str(U - A), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.15, s="A interseccion B = " + str(AB), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.05, s="A union B union C = " + str(T), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.05, s="Complemento de A intersecion C = " + str(U - AC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.15, s="A interseccion B interseccion C = " + str(ABC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.35, s="Complemento de A interseccion \n Complemento de B interseccion \n Complemento de C = " + str((U - A)+(U - B)+(U - C)), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudio ABC")
plt.axis('on')
plt.show()