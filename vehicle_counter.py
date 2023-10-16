# Step 4 count the cars
cap=cv2.VideoCapture('video.mp4')

# line position

count_line_position=550

# min height and witdh of bounding box
min_witdh_rect=80
min_height_rect=80
# initialize the algorithm for subtractor

algo=cv2.createBackgroundSubtractorMOG2()


def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    
    return cx,cy



detect=[]

offset=6

counter=0



while True:
    ret,frame=cap.read()
    
    # write here
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(3,3),5)
    
    # apply algo on each frame
    
    img_sub=algo.apply(blur)
    
    dilat=cv2.dilate(img_sub,np.ones((3,3)))
    
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    
    dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    
    contour_shape,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    # draw the line
    
    cv2.line(frame,(25,count_line_position),(1200,count_line_position),(0,255,0),3)
    
    
    # draw rectangle
    
    for (i,c) in enumerate(contour_shape):
        (x,y,w,h)=cv2.boundingRect(c)
        
        validate_counter=(w>=min_witdh_rect) and (h>=min_height_rect)
        
        if not validate_counter:
            continue
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,"Vehicle Counter: "+str(counter),(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5)
        
        center=center_handle(x,y,w,h)
        
        detect.append(center)
        
        cv2.circle(frame,center,4,(0,0,255),-1)
        
        # to count the number of cars
        
        for (x,y) in detect:
            if y<(count_line_position+offset) and y>(count_line_position-offset):
                counter+=1
            
                cv2.line(frame,(25,count_line_position),(1200,count_line_position),(0,255,172),3)
            
                detect.remove((x,y))
            
                print('Vehicle Counter:'+str(counter))
            
    cv2.putText(frame,"Vehicle Counter: "+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
                
        
        

#     cv2.imshow('Video Original',dilatada)
    
    cv2.imshow('Video Original',frame)
    
    if cv2.waitKey(1)==13:
        break
        
cv2.destroyAllWindows()
cap.releasease()
    