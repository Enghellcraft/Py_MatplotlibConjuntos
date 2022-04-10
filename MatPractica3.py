from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles

T = 500
DA = 52
A = 125 - (DA)
D = 275 - (DA)
N = T - (D + A + DA)

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn2({"10": 1, "01": 1, "11": 1}, set_labels=("Deportes", "Algebra"))
diagram.get_label_by_id("10").set_text(D)
diagram.get_label_by_id("11").set_text(DA)
diagram.get_label_by_id("01").set_text(A)
venn2_circles(subsets=({"10": 1, "01": 1, "11": 1}), color="#000000", alpha=1, linestyle="-", linewidth=2)

plt.text(-0.2, 0.5, s="Total de Estudiantes = " + str(T), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.2, -0.6, s="Estudiantes de Ningun Grupo = " + str(N), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

plt.title ("Estudiantes de Alegrebra y Deportistas")
plt.axis('on')
plt.show()