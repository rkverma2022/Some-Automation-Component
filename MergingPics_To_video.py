import cv2
import os

# Directory containing the images
image_folder = "D:\Project\pics"

# Video file name and format (e.g., 'output.mp4')
video_name = 'gradient.mp4'

# Frame rate (number of frames per second)
frame_rate = 10

# Get a list of all image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Initialize the video writer
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

# Loop through the images and add them to the video
for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    video.write(img)

# Release the video writer and close the video file
video.release()

print(f"Video '{video_name}' created successfully.")
