from numpy import  genfromtxt
import matplotlib.pyplot as plt
import numpy as np


archivo = (input('escriba el nombre de la imagen que desea reducir: '))
tamano = int(input("Ingrese en cuanto desea reducir la imagen (2 = mitad): "))
ruta = 'rutas/'+archivo+'.csv'
imagen = genfromtxt(ruta, delimiter=',')
plt.imshow(imagen)
imagen
print(imagen.shape)

def reducir(img, factor):
    resultado = np.zeros((img.shape[0] // factor, img.shape[1] // factor))
    for i in range(resultado.shape[0]):
        for j in range(resultado.shape[1]):
            resultado[i,j] = np.mean(img[i*factor:(i+1)*factor,j*factor:(j+1)*factor])
    return resultado

def prueba():
    img = reducir(imagen, tamano)
    plt.figure()
    plt.imshow(img, cmap='gray', interpolation='none')
    
    plt.savefig("imagenes_comprimidas_con_perdida/{}_comprimida.jpg".format(archivo))
    plt.show()

if __name__ == '__main__':
    prueba()