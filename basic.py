import cv2 as cv
img=cv.imread('C:\OpenCV-modules\cat.jpg')
#cv.imshow('Cat',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#cv.imshow('Gray',gray)
# blur 

blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

#cv.imshow('Blur',blur)


#edges cascade

canny=cv.Canny(blur,125,125)


#cv.imshow('Canny Edges', canny)


#dilated 

dilated=cv.dilate(canny,(1,1),iterations=1)
cv.imshow('Dilated',dilated)

#ERODING

eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)



resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)



cv.imshow('Resized',resized)


cropped=resized[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)

