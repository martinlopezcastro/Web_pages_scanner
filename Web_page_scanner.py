import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="objetivo")
parser = parser.parse_args()

def main():
	if parser.target:
		try:
			objetivo = requests.get(url=parser.target)
			header = dict(objetivo.headers) 
			for x in header:
				print(x+ " : "+header[x])
		except:
			print("No me pude conectar :(")
	else:
		print("Error escribio mal el comando para ejecutar el programa")
		print("")
		print("Escriba 1 para obtener ayudar: ")
		print("Escriba 2 para salir")
		opcion = input("Eliga una opcion: ")
		if opcion==1:
			print("")
			print("Ejemplo:")
			print("")
			print("-t https://github.com")
			print("")
			print("La url es de ejemplo")
			print("")
			print("Entonces:")
			print("")
			print("Python Web_page_scanner.py -t (url a ingresar, no ingrese la url con parentesis)")
			print("")
			print("Python depende si tiene python 3 y 2 entonces tiene que especificar python 3")
			print("")
			print("Pero si tiene solo una version de python solo escriba python")
		elif opcion==2:
			exit()
if __name__ == '__main__':
	main()
