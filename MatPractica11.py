from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

U = 500
mate = 329
fis = 186
quim = 295
mate_fis = 83 
mate_quim = 217
fis_quim = 63
MFQ = U - mate - fis - quim + mate_fis + mate_quim + fis_quim
MF = 83 - MFQ
MQ = 217 - MFQ
FQ = 63 - MFQ
M = 329 - MF - MQ - MFQ
F = 186 - MF - FQ - MFQ
Q = 295 - MQ - FQ - MFQ


fig = plt.figure(figsize=(8,5), facecolor='cyan')
ax = fig.add_subplot()

diagram = venn3(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1}, set_labels = ('Matematicas', 'Fisica', 'Quimica'))
for subset in ("111", "110", "101", "100","011", "010", "001"): diagram.get_label_by_id(subset).set_text(subset)

diagram.get_label_by_id('100').set_text(M)
diagram.get_label_by_id('110').set_text(MF)
diagram.get_label_by_id('111').set_text(MFQ)
diagram.get_label_by_id('010').set_text(F)
diagram.get_label_by_id('011').set_text(FQ)
diagram.get_label_by_id('001').set_text(Q)
diagram.get_label_by_id('101').set_text(MQ)

plt.text(0.65, 0.45, s="Los 3 Cursos = " + str(MFQ), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.35, s="Matematicas sin Quimica = " + str(M+MF), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.25, s="Fisica sin Matematicas = " + str(F+FQ), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, 0.05, s="Quimica sin Fisica = " + str(Q+MQ), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.15, s="Matematicas o Quimica \npero sin Fisica = " + str(M+Q+MQ), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.35, s="Matematicas y Quimica \npero sin Fisica = " + str(MQ), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.65, -0.55, s="Matematicas pero no \nQuimica ni Fisica = " + str(M), size=6, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))


c = venn3_circles(subsets={"111":1, "110":1, "101":1, "100":1,"011":1, "010":1, "001":1},color="#000000", alpha=1, linestyle="-",linewidth=2)
c[0].set_lw(3.0)
c[1].set_lw(3.0)
c[2].set_lw(3.0)

plt.title("Estudio Materias")
plt.axis('on')
plt.show()