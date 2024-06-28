from PIL import Image
nomImg=input('Ingrese nombre de la imagen local ')
coordInic=input('Ingrese coordenada inicial de imagen ')
ancho=int(input('Ingrese el ancho de la imagen '))
alto=int(input('Ingrese el alto de la imagen '))
xInic=int(coordInic.split(',')[0])
yInic=int(coordInic.split(',')[1])
anchoTotal=xInic-ancho
altoTotal=yInic-alto
#hacer que chequee que sea con, la coord inicial
img=Image.open(nomImg)
newImg=img.crop(xInic,yInic,anchoTotal,altoTotal)
newImg.save('IMGRecort.jpeg')

"""catIm = Image.open('mariposa.jpg')
catCopyIm = catIm.copy()
faceIm = catIm.crop((25, 45, 95, 140))
faceIm.save('copiaCortada.png')"""