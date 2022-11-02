# Import Library
import cv2

# Read an Image
img = cv2.imread("./img/img2.jpg")

# Converting to GrayScale
grayscaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold to Black and White
thresImg = cv2.threshold(grayscaleImg, 100, 255, cv2.THRESH_BINARY)[1]

# Write Image into File
cv2.imwrite("./output/thresholdimage.png", thresImg)

# Show the written image
cv2.imshow("THRESHOLD", thresImg)

# Hold until closed and then destroy all
cv2.waitKey(0)
cv2.destroyAllWindows()
