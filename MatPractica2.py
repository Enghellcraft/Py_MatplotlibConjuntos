from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

T = 600
N = 100
FI = 50
F = 450 + FI
I = T - (N +F -FI)

plt.figure(figsize=(6,4), facecolor='gray')

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Frances', 'Ingles', 'Ninguno'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(F)
diagram.get_label_by_id('110').set_text(FI)
diagram.get_label_by_id('010').set_text(I)
diagram.get_label_by_id('001').set_text(N)

diagram.get_patch_by_id('011').set_alpha(1.0)
diagram.get_patch_by_id('011').set_color('white')
diagram.get_label_by_id('011').set_text('Ninguno')
diagram.get_patch_by_id('111').set_alpha(1.0)
diagram.get_patch_by_id('111').set_color('white')
diagram.get_label_by_id('111').set_text('Ninguno')
diagram.get_patch_by_id('101').set_alpha(1.0)
diagram.get_patch_by_id('101').set_color('white')
diagram.get_label_by_id('101').set_text('Ninguno')

plt.text(0.59, 0.45, s="Estudiantes de solo Ingles = " + str(I), size=6, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-0.62, -0.52, s="Total de \n Estudiantes \n = " + str(T), size=8, ha="right", va="top", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(5.0)
c[2].set_lw(3.0)

plt.title("Estudios de Lenguas en un Colegio")
plt.axis('on')
plt.show()