
A = [[10, 15],
     [20, 5]]

B = [[5, 12],
     [15, 8]]

total = [
    [A[0][0] + B[0][0], A[0][1] + B[0][1]],
    [A[1][0] + B[1][0], A[1][1] + B[1][1]]
]
precio = 50
ingresos = [
    [total[0][0] * precio, total[0][1] * precio],
    [total[1][0] * precio, total[1][1] * precio]
]
print("Matriz de ventas totales:")
for fila in total:
    print(fila)

print("\nMatriz de ingresos:")
for fila in ingresos:
    print(fila)
