import cv2
import glob
# glob module - find path names of files
# cv2 - for image processing
# glob - finds all the path names
# matching a specified pattern according to the rules.


# 1. Create a list of files that has extension of JPG
images = glob.glob('*.jpg')

for image in images:
    # Read all image files from directory
    # 0 - gray color
    img = cv2.imread(image, 0)

    # Create a variable where we will store resized image
    # shape[1] - height. Divide original resolution by any numberic value
    # shape[0] - width.
    re = cv2.resize(img, (int(img.shape[1]/4), - int(img.shape[0]/4)))

    # Check out that images has been resized
    cv2.imshow("Checking", re)

    # Each image should be visible for 0.5 sec on screen
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    # Write resized file to the project directory
    cv2.imwrite("resized_"+image, re)