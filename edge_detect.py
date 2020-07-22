import cv2

def grayscale(img):
    # Converts image to grayscale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img, kernel_size):
    # Applies Gaussian smoothing to the image. Helps in Canny Edge detection
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def canny(img, low_threshold, high_threshold):
    # Edge detection using Canny Edge detection algorithm
    return cv2.Canny(img, low_threshold, high_threshold)

def preprocess(img):
    
    img = grayscale(img)
    img = gaussian_blur(img, 5)
    img = canny(img, 100, 200)
    return img