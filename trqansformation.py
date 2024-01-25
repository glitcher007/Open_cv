import cv2 as cv
import numpy as np


img=cv.imread('C:\OpenCV-modules\cat.jpg')


cv.imshow('Cat',img)
def translate(img,x,y):
    
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)

#-x-> left
#-y=>up
#x=>right
#y=>down



translated=translate(img,-20,30)
cv.imshow('Translated',translated)
    
    
#rotation


def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
        
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimemsions=(width,height)
    return cv.warpAffine(img,rotMat,dimemsions)


rotated=rotate(img,-45)

cv.imshow('Rotated',rotated)


#resizing

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)


cv.waitKey(0)
