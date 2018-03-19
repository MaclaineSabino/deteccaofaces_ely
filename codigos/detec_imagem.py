import cv2

classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('imagens/pessoas4.jpg')
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

faces_detectadas = classificador.detectMultiScale(imagem_cinza,minNeighbors=9,minSize=(70,70))



for x,y,l,a in faces_detectadas:
    cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,255),2)






cv2.imshow('foto',imagem)
cv2.waitKey()