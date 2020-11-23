#List: slower
#Numpy: made for HDA

#Task 1: Color Detection
#Load the image
#RGB to HSV conversion
#Set color to detect (low, up)
#Create a masked image using HSV and color
#Get the pixels from actual image for which mask is 255.
#Save the image
"""
import cv2
import numpy as np
image = cv2.imread('cs_banner.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow('Input', image)
cv2.imshow('HSV', hsv)
#low = np.array([140, 150, 0])
#up = np.array([179, 255, 255])

#Red + Pink
low = np.array([100, 50, 50])
up = np.array([140, 255, 255])

img_masked = cv2.inRange(hsv, low, up)
cv2.imshow('Masked Image', img_masked)

img_output = cv2.bitwise_and(image, image, mask=img_masked)
cv2.imshow('Output Image', img_output)

#Task: Get me all color except Red: Focus on low and up
#Task: Directly apply on RGB and don't convert it into HSV.
"""
"""
#Task 2: Image Resize
import cv2

image = cv2.imread('player.jpg')
#print(image.shape)
h = image.shape[0]
w = image.shape[1]
print(f'Height:{h},Width:{w}')

height = int(input('Enter Height:'))
width = int(input('Enter Width:'))

img_new = cv2.resize(image, (height, width))
cv2.imshow('Input', image)
cv2.imshow('Resized', img_new)

#Aspect Ratio:
asp = width/w
dim = (width, int(h*asp))
img_new1 = cv2.resize(image, dim)
cv2.imshow('Proper Resized', img_new1)
cv2.imwrite('resized_player.jpg',img_new1)

#Try to automate the task: for multiple images

"""
#Task 3: ROI Extraction from Image
import cv2

ref = []


def click_crop(event, x,y, flags, param):
    global ref, crop
    if event == cv2.EVENT_LBUTTONDOWN:
        ref = [(x,y)]
        
    elif event == cv2.EVENT_LBUTTONUP:
        ref.append((x,y))
        cv2.rectangle(image, ref[0], ref[1], (0,0,0),3)
        cv2.imshow("image", image)


image = cv2.imread('cs_banner.jpg')
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback("image", click_crop)
while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(0)
    if key == ord('c'):
        break
    elif key == ord('r'):
        image = clone.copy()
        
if len(ref) == 2:
    crop = clone[ref[0][1]:ref[1][1],ref[0][0]:ref[1][0]]
    cv2.imshow('Cropped', crop)
    key = cv2.waitKey(0)
    if key == ord('s'):
        cv2.imwrite('cropped.jpg', crop)
        print('Cropped Image Saved....')
cv2.destroyAllWindows()
#Task: Try to get multiple crops.


