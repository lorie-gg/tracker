import cv2
import numpy as np

def nothing(x):
    pass

# 1. Load your short test video
video = cv2.VideoCapture('chopin_waltz_left.mp4')

# 2. Create the window and the slider controls
cv2.namedWindow('Color Picker')
cv2.createTrackbar('Low H', 'Color Picker', 0, 179, nothing)
cv2.createTrackbar('High H', 'Color Picker', 179, 179, nothing)
cv2.createTrackbar('Low S', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('High S', 'Color Picker', 255, 255, nothing)
cv2.createTrackbar('Low V', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('High V', 'Color Picker', 255, 255, nothing)

while True:
    ret, frame = video.read()
    
    # If the video ends, loop it back to the beginning!
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0) 
        continue

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3. Read the current positions of all the sliders
    l_h = cv2.getTrackbarPos('Low H', 'Color Picker')
    h_h = cv2.getTrackbarPos('High H', 'Color Picker')
    l_s = cv2.getTrackbarPos('Low S', 'Color Picker')
    h_s = cv2.getTrackbarPos('High S', 'Color Picker')
    l_v = cv2.getTrackbarPos('Low V', 'Color Picker')
    h_v = cv2.getTrackbarPos('High V', 'Color Picker')

    # 4. Apply the slider values to the mask
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([h_h, h_s, h_v])
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # 5. Show the original video and the pure black-and-white mask
    cv2.imshow('Original Video', frame)
    cv2.imshow('The Mask', mask)

    # Press 'q' to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()