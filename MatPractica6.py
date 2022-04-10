from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

LIC = 50
LC = 62 - LIC
LI = 58 - LIC
CI = 98 - LIC
L = 80 - LC - LI - LIC
C = 110 - LC - CI - LIC
I = 125 - LI - CI- LIC
T = L + C + I + LC + LI + CI + LIC
U = 150
NC = U - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Laptop', 'Celular', 'Ipod'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(L)
diagram.get_label_by_id('110').set_text(LC)
diagram.get_label_by_id('111').set_text(LIC)
diagram.get_label_by_id('010').set_text(C)
diagram.get_label_by_id('011').set_text(CI)
diagram.get_label_by_id('001').set_text(I)
diagram.get_label_by_id('101').set_text(LI)

plt.text(0.59, 0.45, s="Estudiantes solo con un Celular = " + str(C), size=6, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.52, -0.60, s="Total de \n Estudiantes \n = " + str(T), size=8, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.82, -0.52, s="Estudiantes sin Dispositivos = " + str(NC), size=6, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.52, -0.42, s="Estudiantes con Ipod y Laptop\n sin Celular  = " + str(LI), size=8, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(1.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudiantes con Dispositivos")
plt.axis('on')
plt.show()