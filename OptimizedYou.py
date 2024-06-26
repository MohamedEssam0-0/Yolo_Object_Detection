import os
import cv2
import numpy as np
import time
from ultralytics import YOLO

def get_current_speed():
    return 50
def calculate_frames_per_second(speed_km_hr, base_speed=10, increment_speed=10):
    additional_frames = round((speed_km_hr - base_speed) / increment_speed)
    return 1 + additional_frames 
desired_fps = calculate_frames_per_second(get_current_speed()) 
model = YOLO('/mnt/sdcard/Yolo_Object_Detection/bestworking.pt')
class_names = model.names
cap = cv2.VideoCapture('/mnt/sdcard/Yolo_Object_Detection/p.mp4')
frame_id = 0
display_frame_counter = 0
original_fps = round(cap.get(cv2.CAP_PROP_FPS))
display_interval = max(1, round(original_fps / desired_fps))  
os.makedirs("saved_frames", exist_ok=True)

while True:
    ret, img = cap.read()
    if not ret:
        break


    if display_frame_counter % display_interval == 0:

        results = model(img)  
        if len(results) > 0:
            result = results[0]  
            boxes = result.boxes  
            names = result.names  

            
            filtered_boxes = [box for box in boxes.data if box[4] > 0.4]

            for box in filtered_boxes:
                class_id = int(box[5])  
                class_name = names[class_id]  
                if class_name != 'Manhole':
                    x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            cv2.imwrite(f"saved_frames/frame_{frame_id}.jpg", img)
            cv2.imshow('img', img)  

        
        


        
        
        
    frame_id += 1
    display_frame_counter += 1




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





cap.release()
cv2.destroyAllWindows()
