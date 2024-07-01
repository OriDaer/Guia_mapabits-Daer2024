#marca de imgMA
from PIL import Image

rutaImg=input('Ingrese ruta de la imagen ')
# c:\Users\orida\Desktop\GuiaMapaBits\Guia_mapabits-Daer2024\arcoiris.jpg
rutaMAgua=input('Ingrese ruta de la imagen de marca de agua: ')
# c:\Users\orida\Desktop\GuiaMapaBits\Guia_mapabits-Daer2024\marcadeagua.png
print('A continuación la opciones para insertar su marca de agua:\n1-Superior izquierda\n2-Superior derecha\n3-Inferior izquierda\n4-Inferior derecha')
numLugar = input('Ingrese el número que desea: ')
def verificaNum(numLugar):#crqueo que lo ingresado sea un numero
    if numLugar.isdigit(): #isdigt()ve si lo q ingresaste fue un num positivo
        numLugar = int(numLugar)
        if(numLugar>4):
            print(f'Número {numLugar} no es valido como opción')
        marcaDeAgua()
    else:
        print('Error: Debes ingresar un número entero positivo.')

def marcaDeAgua(rutaImg,rutaMAgua):
    img= Image.open(f'{rutaImg}')
    imgMA = Image.open(f'{rutaMAgua}')
    imgCopy = img.copy()#copia de imagen original
    imgMACopy=imgMA.copy()#copia img marca de agua
    #achico img de mara de agua
    numDiv=6
    newWidth=int(imgMACopy.width / numDiv)
    newHeight=int(imgMACopy.height / numDiv)
    imgMACopy = imgMACopy.resize((newWidth,newHeight))#achico img de m d imgMA

    if(numLugar==1):#superior izq
        supIzqXY=50
        imgCopy.paste(imgMACopy, (supIzqXY, supIzqXY)) #a img le pego mde imgMA en posicion 50 50 superior izq 
        imgCopy.save('ImgConMarcaDeAgua.png')

    if(numLugar==2):#superior der
        supDerX=imgCopy.width-imgMACopy.width-50
        supDerY=50
        imgCopy.paste(imgMACopy, (supDerX, supDerY)) 
        imgCopy.save('ImgConMarcaDeAgua.png')

    if(numLugar==3):#inferior izq
        infIzqX=50
        infIzqY=imgCopy.height-imgMACopy.height-50
        imgCopy.paste(imgMACopy, (infIzqX, infIzqY)) 
        imgCopy.save('ImgConMarcaDeAgua.png')

    if(numLugar==4):#inferior der
        infDerX=imgCopy.width-imgMACopy.width-50
        infDerY= imgCopy.height-imgMACopy.height-50
        imgCopy.paste(imgMACopy, (infDerX, infDerY))
        imgCopy.save('ImgConMarcaDeAgua.png')

