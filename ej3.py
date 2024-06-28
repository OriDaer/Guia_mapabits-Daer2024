from PIL import Image
ruta=input('Ingrese ruta de la imagen ')
angulo=int(input('Imgrese angulo para rotacion de imagen '))
img=Image.open(f'{ruta}')
nombreArchivOrig= ruta.split('\\')[-1]
extensionOrig=img.format.lower()
# C:\\Users\\orida\\Desktop\\Programacion\\Guia_mapabits\\cat.jpeg

img.rotate(angulo,expand=True).save(f'{nombreArchivOrig}Rot.{extensionOrig}')