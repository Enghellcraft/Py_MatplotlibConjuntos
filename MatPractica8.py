from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

PGO = 5
PG = 20 - PGO
PO = 8 - PGO
GO = 10 - PGO
P = 30 - PG - PO - PGO
G = 42 - PG - GO - PGO
O = 21 - PO - GO - PGO
T = P + G + O + PG + PO + GO + PGO
U = 80
NC = U - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Perros', 'Gatos', 'Otros'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(P)
diagram.get_label_by_id('110').set_text(PG)
diagram.get_label_by_id('111').set_text(PGO)
diagram.get_label_by_id('010').set_text(G)
diagram.get_label_by_id('011').set_text(GO)
diagram.get_label_by_id('001').set_text(O)
diagram.get_label_by_id('101').set_text(PO)

plt.text(0.65, 0.45, s="Perros y Gatos sin Otros = " + str(PG), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.35, s="Solo Perros = " + str(P), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.25, s="Sin Mascotas = " + str(NC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.05, s="Otros con Perros y\n Otros con gatos\n pero no ambos = " + str(PO + GO), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.05, s="A union B union C = " + str(T), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudio Mascotas")
plt.axis('on')
plt.show()