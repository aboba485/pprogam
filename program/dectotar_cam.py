import cv2 
import imutils
hog = cv2.HOGDescriptor ()
hog. setSVMDetector (cv2.HOGDescriptor_getDefaultPeopleDetector ( ))
cap = cv2.VideoCapture ('Codewisdom Video.mp4')
while cap. isOpened() :
    ret, image = cap.read()
    if ret:
        image = imutils. resize(image,
        width=min 
        (400, image. shape [1]))
        (regions, _) = hog.detectMultiScale
        (image,winStride=l padding= (4 scale=1.05)

        Code
        Wisdom
        for (x, y, w, h) in regions: cv2. rectangle(image, (X,
        (0, 0, 255),
        2)
        cv2.imshow("CodeWisdom", image) if cv2.waitkey (25) & OxFF == ord('g*):
        break
        else:
        break
cap.release()
cv2.destroyAllWindows()