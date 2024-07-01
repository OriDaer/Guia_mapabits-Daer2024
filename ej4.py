from PIL import Image
import os
import sys

ruta_directorio = './recortes'
def crear_directorio(ruta_directorio):#creando directorio llamado recortes
    if not os.path.exists(ruta_directorio):
        os.mkdir(ruta_directorio)
        os.chdir(ruta_directorio)
        #print(f'Se ha creado el directorio en: {ruta_directorio}')
    else:
        os.chdir(ruta_directorio)
        #print(f'El directorio en: {ruta_directorio} ya existe.')

nomImg=input('Ingrese nombre de la imagen local: ')

def imgExiste(nomImg):#verifico si la imagen existe
    return os.path.exists(nomImg)

def recImg(img):
    coordInic=input('Ingrese coordenada inicial de imagen ')
    xInic=int(coordInic.split(',')[0])
    yInic=int(coordInic.split(',')[1])

    """zona excede area"""
    if(xInic > img.width or yInic > img.height):
        print('los parametros ingresados estan por fuera de la imagen')
        sys.exit()

    ancho=int(input('Ingrese el ancho de la imagen '))
    if(xInic + ancho > img.width ):
        print('Se excedieron los parametros del area de imagen ')
        sys.exit()

    alto=int(input('Ingrese el alto de la imagen '))
    if (yInic + alto > img.height):
        print('Se excedieron los parametros del area de imagen ')
        sys.exit()

    newImg = img.crop((xInic, yInic, xInic+ancho, yInic+alto))

    crear_directorio(ruta_directorio)
    # Contar el número de archivos en la carpeta "recortes"
    num_recortes = len(os.listdir(ruta_directorio))
    newImg.save(f'recortes{num_recortes+1}.jpeg')

if imgExiste(nomImg):#confirmado que si exite la img 
    print("La imagen existe en la ruta especificada.")
    img = Image.open(nomImg)
    #print(img.size)
    recImg(img)

else:
    print('Error, no existe el archivo')