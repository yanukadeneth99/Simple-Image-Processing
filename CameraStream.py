# Importing CV Library
import cv2

# Initialising Camera
vs = cv2.VideoCapture(0)

# Infinite While Loop
while True:
    _, img = vs.read()  # Reading each frame
    cv2.imshow("Video Stream", img)  # Show each frame image to user

    # Reading Key
    key = cv2.waitKey(1) & 0xFF

    # Exit the Camera is pressed Q
    if key == ord("q"):
        break

# Release the Camera and destroy all windows
vs.release()
cv2.destroyAllWindows()
