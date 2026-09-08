
import cv2
import numpy as np
import csv
import math # Added this for the distance math!

video_name = 'chopin_waltz_left.mp4' 
video = cv2.VideoCapture(video_name)

cv2.namedWindow('Hand Tracker', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow('Hand Tracker', 1200, 400)

# 1. The Strict Boundary Dictionary
markers = {    
    'Green': [[45, 40, 30], [85, 255, 255], (0, 0, 255)],
    'Lime':  [[30, 120, 80], [42, 255, 255], (0, 255, 255)]
}

# 2. Setup the clean spreadsheet (Added 'Distance' column!)
csv_file = open('left_hand_data.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Frame', 'Green_X', 'Green_Y', 'Lime_X', 'Lime_Y', 'Distance'])

frame_count = 0

while True:
    ret, frame = video.read()
    if not ret: break
    frame_count += 1

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    row_data = [frame_count] 
    
    # We will temporarily store the coordinates here to do math on them later!
    points = {}

    # 3. Loop through the colors
    for name, data in markers.items():
        lower_bound = np.array(data[0])
        upper_bound = np.array(data[1])
        draw_color = data[2]
        
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
        
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        cx, cy = 0, 0 
        valid_blobs = []
        
        for c in contours:
            area = cv2.contourArea(c)
            if 20 < area < 10000: 
                valid_blobs.append(c)
        
        if valid_blobs:
            best_contour = max(valid_blobs, key=cv2.contourArea)
            M = cv2.moments(best_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 10, draw_color, -1)
        
        # Save the coordinates to our temporary dictionary and to the CSV row
        points[name] = (cx, cy)
        row_data.extend([cx, cy])
        
    # --- 4. THE DISTANCE MATH ---
    gx, gy = points['Green']
    lx, ly = points['Lime']
    
    # If both dots are successfully tracked (neither of them dropped out to 0)
    if gx != 0 and lx != 0:
        # Calculate distance and round to 2 decimal places
        distance = round(math.hypot(lx - gx, ly - gy), 2)
        row_data.append(distance) # Add the number to the CSV
        
        # Draw a line connecting the dots and display the number!
        cv2.line(frame, (gx, gy), (lx, ly), (255, 255, 255), 2)
        cv2.putText(frame, f"Dist: {distance}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        # If a dot is missing, leave the cell completely blank!
        row_data.append("") 
    # -----------------------------
        
    # Write the row and show the video
    writer.writerow(row_data)
    cv2.imshow('Hand Tracker', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'): break

video.release()
csv_file.close()
cv2.destroyAllWindows()