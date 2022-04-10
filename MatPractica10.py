from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

BMU = 53
BM = 30 - BMU
BU = 16 - BMU
MU = 22 - BMU
B = 71 - BM - BU - BMU
M = 72 - BM - MU - BMU
U = 38 - BU - MU - BMU
T = B + M + U + BM + BU + MU + BMU
UN = 150
NC = UN - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Basica', 'Media', 'Universitaria'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(B)
diagram.get_label_by_id('110').set_text(BM)
diagram.get_label_by_id('111').set_text(BMU)
diagram.get_label_by_id('010').set_text(M)
diagram.get_label_by_id('011').set_text(MU)
diagram.get_label_by_id('001').set_text(U)
diagram.get_label_by_id('101').set_text(BU)

plt.text(0.65, 0.45, s="Solo Universitarios = " + str(U), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.35, s="Solo en 2 Niveles = " + str(BM+BU+MU), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.25, s="Sin Estudios = " + str(NC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudio Nivel Educativo")
plt.axis('on')
plt.show()