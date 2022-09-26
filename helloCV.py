import sys
import cv2

print('hello, openCV', cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.imwrite('cat_gray.png', img)

cv2.namedWindow('CAT_image', cv2.WINDOW_NORMAL)
cv2.imshow('CAT_image', img)

while True:
    if cv2.waitKey() == 27:
        break

cv2.destroyAllWindows()
