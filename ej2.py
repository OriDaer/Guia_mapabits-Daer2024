from PIL import Image
nombreImg='mariposa.jpg'
img=Image.open(nombreImg)
img.show()
imgCopy=img.copy()
nombreImgLocal=f'imgCopiaLocal.{img.format}'
imgCopy.save(nombreImgLocal)
