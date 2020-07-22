from edge_detect import preprocess
from roi import roi
from detect_lane_lines import detect
from draw import draw_lines
import argparse
import cv2

args = parser.parse_args()

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    
    return cv2.addWeighted(initial_img, α, img, β, λ)

def laneDetection(image):
    
    img_canny = preprocess(image)
    img_roi = roi(img_canny)
    img_detect, lines = detect(img_roi)
    img_draw = draw_lines(img_detect, lines)
    detected_lane = weighted_img(img_draw, image)
    cv2.imshow("Lanes", detected_lane)

cap = cv2.VideoCapture("data/test_data_1.mp4")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    laneDetection(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break