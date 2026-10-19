from collections import deque
cola=deque()
#agregar elementos en la cola
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#sacar el primer elemento que llego
atendido=cola.popleft()
#mostrar resultados
print("Atendido",atendido)
print("cola restante:",cola)

