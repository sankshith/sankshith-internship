import cv2
import os
video_path = "C:\\Users\\DevAppSys Office\\Downloads\\WhatsApp Video 2024-01-29 at 11.18.49 AM.mp4"
output_folder = "D:\sankshith.m"
video_capture = cv2.VideoCapture(video_path)
if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()
frame_count = 0

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1
video_capture.release()
print(f"Frames saved to {output_folder}")
