## PRACTICAS ESTRUCTURAS DE DATOS
### DOCENTE: M.T.I NORMA G.R


# Crear lista inicial
estudiantes = ["Ana", "Carlos", "Diana"]
print("Lista inicial:", estudiantes)

# Inserciones
estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")
print("Lista actualizada:", estudiantes)

# Búsqueda y acceso por índice
print("Primer estudiante:", estudiantes[0])
print("Tercer estudiante:", estudiantes[2])
print("Índice de Diana:", estudiantes.index("Diana"))

# Operaciones de slicing
print("Primeros 3:", estudiantes[:3])
print("Últimos 2:", estudiantes[-2:])
print("Orden inverso:", estudiantes[::-1])
