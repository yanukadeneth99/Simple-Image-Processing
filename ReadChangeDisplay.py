# Import Library
import cv2

# Read an Image
img = cv2.imread("./img/img1.jpeg")

# Write the image and change format
cv2.imwrite("./output/img1.png", img)

# Show the image
cv2.imshow("CODE", img)

# Keep showing image then destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
