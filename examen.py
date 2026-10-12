# crear lista
estudiantes = ["Ana", "carlos", "Diana"]
print("Lista inicial:", estudiantes)

#agregar a elena y insercion de beatriz
estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")
print("Lista actualizada:", estudiantes)

#busqueda por indice
print("Primer estudiante:", estudiantes[0])
print("Tercer estudiante:", estudiantes[2])
print("Índice de Diana:", estudiantes.index("Diana"))
print("Primeros 3:", estudiantes[:3])
print("subgrupo 1 al 3:", estudiantes[1:4])
print("Últimos 2:", estudiantes[-2:])
print("Orden inverso:", estudiantes[::-1])

