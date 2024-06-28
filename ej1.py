from PIL import Image
ruta=input('ingrese la ruta local de la imagen ')
#C:\\Users\\orida\\Desktop\\Programacion\\Guia_mapabits\\cat.jpeg
def infoImagen(ruta):
    imagen=Image.open(f'{ruta}')
    imagen.show()
    nombreImg=ruta.split('\\')[-1]
    extension=imagen.format
    resolucion=imagen.size
    cantPixeles= imagen.height * imagen.width
    ubicRuta=imagen.filename
    print('____________________________________')
    print('|  Propiedad      |  Valor          |')
    print('____________________________________')
    print('|Nombre de imagen |',nombreImg,'    |')
    print('____________________________________')
    print('|  Formato imagen |',extension,'    |')
    print('____________________________________')
    print('|Resolucion imagen|',resolucion,'   |')
    print('____________________________________')
    print('| Cantidad pixeles|',cantPixeles,'  |')
    print('____________________________________')
    print('|    Ruta imagen  |',ubicRuta,'     |')
    print('____________________________________')