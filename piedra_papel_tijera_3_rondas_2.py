#-----------------------PIEDRA, PAPEL O TIJERA-------------------------#
# 04/04/2021
# Santiago, Chile
# Eddie Casañas
#----------------------------------------------------------------------#


#SE IMPORTA LA LIBRERIA "random" PARA GENERAR NUMEROS ALEATORIOS:
import random as rd

#SE DEFINE LA FUNCION "maquina", LA CUAL GENERARA NUMEROS ALEATORIOS DEL 0 AL 2:
def maquina():
	
	#"randrange" PERMITE GENERAR NUMEROS ALEATORIOS EN CIERTO RANGO
	jugada = rd.randrange(0,3)
	
	#SI EL NUMERO QUE APARECE ALEATORIAMENTE ES 0, DEVUELVE "piedra"
	if jugada == 0:
		return "piedra"
	
	#SI EL NUMERO QUE APARECE ALEATORIAMENTE ES 1, DEVUELVE "papel"
	if jugada == 1:
		return "papel"
		
	#SI EL NUMERO QUE APARECE ALEATORIAMENTE ES 2, DEVUELVE "tijera"
	if jugada == 2:
		return "tijera"


#SE DEFINE LA FUNCION "mi_jugada", QUE REPRESENTARA LA JUGADA DEL USUARIO
def mi_jugada():
									
	#SE ESTABLECE UN CONTADOR EMPEZANDO EN CERO:
	i = 0
	
	#MIENTRAS EL CONTADOR SEA MENOR QUE 3, SE EJECUTARA EL SIGUIENTE CODIGO:
	while i < 3:
		
		#SE GUARDA LA FUNCION "maquina" EN LA VARIABLE "python"
		python = maquina()
						
		#SE LE DA UNA OPCION AL JUGADOR:
		accion = input("\nElige entre piedra, papel o tijera: ")
		
		
		#DISTINTAS FORMAS DE GANAR, PERDER Y EMPATAR
		
			#EMPATE = 0 PUNTOS
			#VICTORIA = 1 PUNTO
			#PERDIDA = 0 PUNTOS
			
		if accion.lower().strip() == python:
			puntos = 0			
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Nadie recibe puntos")
			
			#SE GUARDAN LOS RESULTADOS EN UNA LISTA DEL JUGADOR Y EN OTRA DE LA MAQUINA:
			puntuacion.append(puntos)
			python_puntos.append(puntos)
			
			#SE LE SUMA LA UNIDAD AL CONTADOR PARA QUE SE PUEDA SALIR DEL BUCLE:
			i += 1
			
		#SE HACE LO MISMO CON LAS DEMAS ALTERNATIVAS:
		elif accion.lower().strip() == "piedra" and python == "tijera":
			puntos = 1
			puntos_maquina = 0
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para el usuario")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		elif accion.lower().strip() == "piedra" and python == "papel":
			puntos = 0
			puntos_maquina = 1
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para la maquina")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		elif accion.lower().strip() == "papel" and python == "piedra":
			puntos = 1
			puntos_maquina = 0
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para el usuario")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		elif accion.lower().strip() == "papel" and python == "tijera":
			puntos = 0
			puntos_maquina = 1
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para la maquina")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		elif accion.lower().strip() == "tijera" and python == "papel":
			puntos = 1
			puntos_maquina = 0
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para el usuario")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		elif accion.lower().strip() == "tijera" and python == "piedra":
			puntos = 0
			puntos_maquina = 1
			print("\n\tUsuario: " + accion.lower().strip())
			print("\tMaquina: " + python)
			print("\n-Punto para la maquina")
			puntuacion.append(puntos)
			python_puntos.append(puntos_maquina)
			i += 1
			
		#SI ALGUNO DE LOS DOS CONSIGUE 2 PUNTOS, SE TERMINA EL BUCLE:
		if sum(puntuacion) == 2 or sum(python_puntos) == 2:
			break
					

#SE CREA UNA FUNCION QUE MUESTRE LOS RESULTADOS Y QUE 
#DE LA OPCION AL JUGADOR DE SEGUIR JUGANDO O RETIRARSE:

def resultados():
	print("\nRESULTADOS:\n")
	
	
	#SE SUMA EL CONTENIDO DE LAS DOS LISTAS PARA VER QUIEN TIENE MAS PUNTOS:
	print("Usuario: " + str(sum(puntuacion)))
	print("Maquina: " + str(sum(python_puntos)))

	if sum(puntuacion) == sum(python_puntos):
		print("\nEmpate")

	elif sum(puntuacion) > sum(python_puntos):
		print("\nGanaste")
		
	elif sum(puntuacion) < sum(python_puntos):
		print("\nPerdiste")

	#SE LE DA LA OPCION AL JUGADOR DE SEGUIR JUGANDO O ABANDONAR:
	opcion = input("\n¿Desea volver a jugar? (y/n)")
	if opcion == "y":
		
		puntuacion.clear()
		python_puntos.clear()
		mi_jugada()		
		resultados()
		
				
#SE CREA LA LISTA DE PUNTOS DEL USUARIO:
puntuacion = []

#SE CREA LA LISTA DE PUNTOS DE LA MAQUINA:
python_puntos = []	

#SE LLAMAN A LAS FUNCIONES PARA PODER EJECUTAR EL PROGRAMA:
mi_jugada()
resultados()
