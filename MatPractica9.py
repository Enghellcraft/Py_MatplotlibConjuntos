from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

from Py_MatplotlibConjuntos.MatPractica1 import A

SC = 800 
S = 1950 - SC
M = 400 
C = 1500 - SC
T = S + M + C + SC
U = 3200
NC = U - T

fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Subte', 'Motos', 'Colectivos'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(S)
diagram.get_patch_by_id('110').set_alpha(1.0)
diagram.get_patch_by_id('110').set_color('white')
diagram.get_label_by_id('110').set_text('Ninguno')
diagram.get_patch_by_id('111').set_alpha(1.0)
diagram.get_patch_by_id('111').set_color('white')
diagram.get_label_by_id('111').set_text('Ninguno')
diagram.get_label_by_id('010').set_text(M)
diagram.get_patch_by_id('011').set_alpha(1.0)
diagram.get_patch_by_id('011').set_color('white')
diagram.get_label_by_id('011').set_text('Ninguno')
diagram.get_label_by_id('001').set_text(C)
diagram.get_label_by_id('101').set_text(SC)

plt.text(0.65, 0.45, s="Personas que solo usan Subte = " + str(S), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.25, s="Personas que usan \n maximo 2 medios \n de transporte = " + str(S+C+SC), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
ax.text(-0.55, -0.42, NC)

c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudio Medios de Transporte Urbano")
plt.axis('on')
plt.show()