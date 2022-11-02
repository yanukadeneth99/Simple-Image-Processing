# Importing CV2 Library
import cv2

# Read an Image
img = cv2.imread("./img/img1.jpeg")

# Greyscale the image
grayscaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Write the grayscale into file
cv2.imwrite("./output/grayscaleImg1.png", grayscaleImg)

# Show both the images
cv2.imshow("ORIGINAL", img)
cv2.imshow("GRAY SCALE", grayscaleImg)

# Hold until closed and then destroy all
cv2.waitKey(0)
cv2.destroyAllWindows()
