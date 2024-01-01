import cv2
import easyocr

reader=easyocr.Reader(['en','mr'])

img=cv2.imread('sign21.jpg')
result=reader.readtext(img)
spacer=100
for i in result:
    top_left=tuple(i[0][0])
    bottom_right=tuple(i[0][2])
    text=i[1]
    img=cv2.putText(img,text,top_left,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),2)
    spacer+=15

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()