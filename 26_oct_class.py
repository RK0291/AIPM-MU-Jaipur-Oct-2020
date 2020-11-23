import cv2

img_path = r'F:\Code Shala Feb 2020\Python Work\Python Lectures\Lecture Manipal Uni Jaipur Oct 2020\player.jpg'


"""
#Reading an image

img = cv2.imread(img_path)

print(type(img))
print(img[0,0])
print(img.shape, img.ndim, img.size)

#cv2.imshow('First Demo', img)

#grayscale: 0-255 (black to white)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img_gray[0,0])
print(type(img_gray))

print(img_gray.shape, img_gray.ndim, img_gray.size)
cv2.imwrite('player_gray.jpg',img_gray)

#display gray scale image
#cv2.imshow('First Demo of GrayScale', img_gray)

#hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
print(img_hsv[0,0])
print(type(img_hsv))

print(img_hsv.shape, img_hsv.ndim, img_hsv.size)
cv2.imwrite('player_hsv.jpg',img_hsv)
#display HSV image
#cv2.imshow('First Demo of HSV', img_hsv)

#negative
img_neg = cv2.bitwise_not(img)
print(img_neg[0,0])
print(type(img_neg))

print(img_neg.shape, img_neg.ndim, img_neg.size)
#cv2.imwrite('player_neg.jpg',img_neg)
#display Negative image
cv2.imshow('First Demo of Negative', img_neg)
#35: 00100011---> 11011100: 128+64+16+8+4 = 220

#If you press key s: your image gets saved.
#Otherwise, exit without saving
key = cv2.waitKey(0)
if key == 115: #Key s
    cv2.imwrite('player_neg_s.jpg',img_neg)
    print('Exit after saving')
else:
    print('Exit without saving')
cv2.destroyAllWindows()
"""
#Task 2:
#Extract part of an image (ROI):
#Reading an image

img1 = cv2.imread(img_path)
img = img1.copy()

cv2.imshow('First Demo', img)

f_ball = img[230:280, 275:325]
#print(f_ball.shape, f_ball.ndim, f_ball.size)
#cv2.imshow('Extract Ball', f_ball)

img[225:275, 50:100] = f_ball

img[220:270, 0:50] = f_ball
cv2.imshow('Updated Image', img)
cv2.imwrite('updated.jpg', img)
#More better approach??




