
A = {125, 52}
D = {257, 52}

print(f"Los Alumnos que hacen Algebra son: {A.difference(D)}")
print(f"Los Alumnos que hacen Deporte son: {D.difference(A)}")

DA = A.intersection(D)
print(f"Los Alumnos que hacen Deporte y estudian Algebra son: {DA}")

T = A.union(D)
print(f"El total de Alumnos es: {T}")

