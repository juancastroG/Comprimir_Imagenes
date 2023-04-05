from huffman import HuffmanCom
import os

ruta_carpetas    = 'rutas/' #Aqui iria la direccion de la carpeta en la que tengan los csv
nombres_carpetas = os.listdir(ruta_carpetas) #me extrae una lista con el nombre de los archivos dentro de esa carpeta
print(nombres_carpetas)

for carpeta in nombres_carpetas: #Un ciclo para iterar atraves de la lista con elnombre de cada archivo
	ruta_completa = ruta_carpetas + carpeta #la direccion o path de cada archivo completo
	print('ruta completa de cada archivo: ',ruta_completa)
	h = HuffmanCom(ruta_completa) #inicializa lavariable path con la ruta de cada archivo
	ruta_salida = h.compress() #invoca al metodo compress para comprimir(codificar) la informacion
	print("Ruta de archivo comprimido: " + ruta_salida)
	
	ruta_decodificacion = h.decompress(ruta_salida) #invoca al metodo decompress para poder descomprimir(decodificar) el archivo
	print("Ruta de archivo comprimido: " + ruta_decodificacion)

