import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)


blank[:]=0,0,255


#cv.imshow('Green',blank)
'''
cv.rectangle(blank,(0,0),(350,350),(0,355,0),thickness=-1)
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,355),thickness=2)


cv.imshow('Circle',blank)

cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(350,350,350))


cv.imshow('Line',blank)
'''
cv.putText(blank,'hello it',(0,355),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,355,0),2)

cv.imshow('Text',blank)



cv.waitKey(0)

