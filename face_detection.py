# library
import cv2

# face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


# face detection function
def detect_face(img):

    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in face_rects:

        cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,0,255), 2)

    return face_img

# open the webcam
cap = cv2.VideoCapture(r'C:\Users\admin\Documents\CV_Ubaid\object detection\dog and boy.mp4')




# apply the face detection
while True:
    ret, frame = cap.read(0)
    frame = rescale_frame(frame, percent=25)
    frame = detect_face(frame)
    cv2.imshow('Webcam Face Detect', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()