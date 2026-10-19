from collections import deque
import deque
cola_reproduccion=deque()
cola_reproduccion.append("1.analogia")
cola_reproduccion.append("2.historial de amor")
cola_reproduccion.append("3.historia entre tus dedos")

#MOSTARR LAS CANCIONES EN ESPERA
print("Canciones en espera")
for cancion in cola_reproduccion:
    print(" _",cancion)
    print("Iniciando reproduccion")
#el reproductor procesa la cola cancion por cancion

while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"sonando ahora{cancion_actual}")
    time.sleep(1) 
    print(f"Finalizo:{cancion_actual}")

    print(f"quedan(len{cola_reproduccion}) canciones en la cola")
    print("la cola de reproduccion han terminado.")