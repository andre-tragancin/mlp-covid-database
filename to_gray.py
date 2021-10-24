import cv2

class toGray:
    
    def image_to_gray(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)