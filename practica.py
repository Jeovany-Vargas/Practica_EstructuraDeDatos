historial_navegador=[]
#operacion apilada
historial_navegador.append("google.com")
historial_navegador.append("youtube.com")
historial_navegador.append("wikipedia.org")
print("pagina actual en pantalla:", pagina_actual)

#operacion cima (TOP-PEEK)
pagina_actual=historial_navegador[-1]
print("pagina actual en pantalla:",pagina_actual)

#operacion para desapilar(POP)
pagina_cerrada=historial_navegador.pop()
print("Saliendo de:",pagina_cerrada)
print("historial despues de presionar atras", historial_navegador)

#Operacion Tamaño (SIZE)
total_paginas=len(historial_navegador)
print("pagina guardadas",total_paginas)

#Operacion vacia (EMPTY)
sin_paginas=len(historial_navegador)==0
print("¿el historial esta vacio",sin_paginas)