import cv2 as cv

img=cv.imread('C:\OpenCV-modules\cat.jpg')

def rescaleFrame(frame,scale=1.75):
    width=int(frame.shape[1]* scale)
    height=int(frame.shape[0]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
 
 
capture = cv.VideoCapture('C:\OpenCV-modules\cute_cat_-_3092 (540p) (1).mp4')
while True:
    isTrue, frame = capture.read()
    
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break


capture.release()
cv.destroyAllWindows()
#cv.waitKey(0)

