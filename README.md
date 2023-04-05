# Proyecto de Reducción de Tamaño de Imágenes

El objetivo de este proyecto es reducir el tamaño de las imágenes haciendo uso de dos algoritmos diferentes. Uno de ellos utiliza el escalamiento de imágenes con librerías como NumPy para la operación de matrices y Matplotlib para la visualización de las imágenes. El otro algoritmo es sin pérdida de calidad, utilizando el algoritmo de Huffman para reducir el tamaño del archivo sin perder información.

## Algoritmo de Huffman

El algoritmo de Huffman es un algoritmo de compresión sin pérdida de datos que utiliza la frecuencia de aparición de cada símbolo en un archivo para construir un árbol binario que asigna códigos cortos a los símbolos más comunes y códigos largos a los menos comunes. Este árbol se utiliza para comprimir el archivo, reemplazando los símbolos con sus códigos correspondientes. La decodificación se realiza simplemente siguiendo las ramas del árbol hasta encontrar los símbolos correspondientes a los códigos.

## Escalamiento de Imágenes

El escalamiento de imágenes es un proceso mediante el cual se ajusta el tamaño de una imagen a una escala menor o mayor. En este proyecto, se utiliza el escalamiento para reducir el tamaño de las imágenes y así reducir el peso del archivo. Para el escalamiento, se utiliza la librería NumPy para realizar las operaciones de matriz necesarias y Matplotlib para visualizar las imágenes resultantes.

## Requisitos

- NumPy
- Matplotlib
- heapq

## Instalación

1. Clona el repositorio desde GitHub:

* git clone https://github.com/tu_usuario/proyecto-reduccion-imagenes.git

2. Instala las dependencias requeridas:

* pip install numpy
* pip install matplotlib
* pip install heapq

## Uso

1. Ejecuta el archivo "escalamiento.py" para reducir el tamaño de la imagen utilizando el algoritmo de escalamiento:
```bash
 python escalamiento.py
```
2. Si deseas reducir el tamaño de la imagen sin pérdida de calidad, utiliza el archivo "leer_csv.py" para aplicar el algoritmo de Huffman:
```bash
 python leer_csv.py
```
## Contribución

Se aceptan contribuciones al proyecto. Si deseas contribuir, por favor sigue las siguientes pautas:

1. Haz un fork del repositorio.
2. Crea una rama nueva para tus cambios: `git checkout -b feature-nueva`.
3. Haz los cambios y crea una confirmación (commit): `git commit -m "Agrega nueva funcionalidad"`.
4. Haz un push de la rama a tu fork: `git push origin feature-nueva`.
5. Crea una solicitud de extracción (pull request) al repositorio original.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

## Autoría

Este proyecto fue desarrollado por Juan Carlos Castro. Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi perfil en GitHub. ¡Gracias por utilizar mi proyecto!```
