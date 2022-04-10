from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles

MN = 62
M = 89 - MN
N = 103 - MN
T = M + N + MN
U = 178
NC = U - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn2({"10": 1, "01": 1, "11": 1}, set_labels=("M", "N"))
diagram.get_label_by_id("10").set_text(M)
diagram.get_label_by_id("11").set_text(MN)
diagram.get_label_by_id("01").set_text(N)
venn2_circles(subsets=({"10": 1, "01": 1, "11": 1}), color="#000000", alpha=1, linestyle="-", linewidth=2)

plt.text(-0.22, 0.51, s="Total de Elementos en Conjuntos = " + str(T), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.22, 0.47, s="Elementos del Universo = " + str(U), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.22, -0.6, s="Elementos del Universo sin Conjunto= " + str(NC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

plt.title ("Universo de Conjuntos N y M")
plt.axis('on')
plt.show()