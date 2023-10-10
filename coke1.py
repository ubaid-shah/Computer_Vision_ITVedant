import cv2

img=cv2.imread(r'C:\Users\admin\Documents\CV_Ubaid\OPenCV\opencv_bootcamp_assets_NB1\coca-cola-logo.png',1)

cv2.imshow('coca cola',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

