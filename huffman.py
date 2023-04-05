import heapq
import os

class HuffmanCom:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codigo = {}
		self.mapeo_reversa = {}

	class Nodo_class:
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.izq = None
			self.der = None

		# rehacemos las los metodos igual(eq) y menor que(lt) 
		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other, Nodo_class)):
				return False
			return self.freq == other.freq

	# functions para comprimir:

	def diccionario_frecuencia(self, texto):
		frecuencia = {}
		for caracter in texto:
			if not caracter in frecuencia:
				frecuencia[caracter] = 0
			frecuencia[caracter] += 1
		return frecuencia

	def crear_heap(self, frecuencia):
		for key in frecuencia:
			nodo = self.Nodo_class(key, frecuencia[key])
			heapq.heappush(self.heap, nodo)

	def unir_nodos(self):
		while(len(self.heap)>1):
			nodo1 = heapq.heappop(self.heap)
			nodo2 = heapq.heappop(self.heap)

			union = self.Nodo_class(None, nodo1.freq + nodo2.freq)
			union.izq = nodo1
			union.der = nodo2

			heapq.heappush(self.heap, union)


	def creacion_codificacion(self, raiz, codigo_actual):
		if(raiz == None):
			return

		if(raiz.char != None):
			self.codigo[raiz.char] = codigo_actual
			self.mapeo_reversa[codigo_actual] = raiz.char
			return

		self.creacion_codificacion(raiz.izq, codigo_actual + "0")
		self.creacion_codificacion(raiz.der, codigo_actual + "1")


	def hacer_codificacion(self):
		raiz = heapq.heappop(self.heap)
		codigo_actual = ""
		self.creacion_codificacion(raiz, codigo_actual)


	def codificacion_texto(self, texto):
		encoded_texto = ""
		for caracter in texto:
			encoded_texto += self.codigo[caracter]
		return encoded_texto


	def ayuda_codificacion(self, encoded_texto):
		almohadilla = 8 - len(encoded_texto) % 8
		for i in range(almohadilla):
			encoded_texto += "0"

		almohadilla_info = "{0:08b}".format(almohadilla)
		encoded_texto = almohadilla_info + encoded_texto
		return encoded_texto


	def get_byte_array(self, texto_codificado_relleno):
		if(len(texto_codificado_relleno) % 8 != 0):
			print("El texto codificado no se relleno correctamente ")
			exit(0)

		b = bytearray()
		for i in range(0, len(texto_codificado_relleno), 8):
			byte = texto_codificado_relleno[i:i+8]
			b.append(int(byte, 2))
		return b


	def compress(self):
		nombre_fichero, extension_fichero = os.path.splitext(self.path)
		ruta_salida = nombre_fichero +'_comprimido'+ ".bin"

		with open(self.path, 'r+') as file, open(ruta_salida, 'wb') as salida:
			texto = file.read()
			texto = texto.rstrip()

			frecuencia = self.diccionario_frecuencia(texto)
			self.crear_heap(frecuencia)
			self.unir_nodos()
			self.hacer_codificacion()

			encoded_texto = self.codificacion_texto(texto)
			texto_codificado_relleno = self.ayuda_codificacion(encoded_texto)

			b = self.get_byte_array(texto_codificado_relleno)
			salida.write(bytes(b))

		print("Comprimiendo...")
		return ruta_salida


	# Metodos de decodificacion


	def remover_relleno(self, texto_codificado_relleno):
		almohadilla_info = texto_codificado_relleno[:8]
		almohadilla = int(almohadilla_info, 2)

		texto_codificado_relleno = texto_codificado_relleno[8:] 
		encoded_texto = texto_codificado_relleno[:-1*almohadilla]

		return encoded_texto

	def decodificar_texto(self, encoded_texto):
		codigo_actual = ""
		decoded_text = ""

		for bit in encoded_texto:
			codigo_actual += bit
			if(codigo_actual in self.mapeo_reversa):
				caracter = self.mapeo_reversa[codigo_actual]
				decoded_text += caracter
				codigo_actual = ""

		return decoded_text


	def decompress(self, ruta_entrada):
		nombre_fichero, extension_fichero = os.path.splitext(self.path)
		ruta_salida = nombre_fichero + "_descomprimido" + ".csv"

		with open(ruta_entrada, 'rb') as file, open(ruta_salida, 'w') as salida:
			bit_string = ""

			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_texto = self.remover_relleno(bit_string)

			decompressed_text = self.decodificar_texto(encoded_texto)
			
			salida.write(decompressed_text)

		print("Descomprimiendo archivo...")
		return ruta_salida

