import os
import glob
import shutil

# Define the main folder path and subfolder paths
main_folder_path = 'mla.krishnakhopde_media'
images_folder = os.path.join(main_folder_path, 'Images')
videos_folder = os.path.join(main_folder_path, 'Videos')
others_folder = os.path.join(main_folder_path, 'Others')

# Create subfolders if they don't already exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(others_folder, exist_ok=True)

# Define file types to move
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
other_extensions = ('.pdf', '.docx', '.txt', '.json', '.xz')  # Add any other extensions you need

# Move image files
for ext in image_extensions:
    for file_path in glob.glob(os.path.join(main_folder_path, f'*{ext}')):
        shutil.move(file_path, images_folder)

# Move video files
for ext in video_extensions:
    for file_path in glob.glob(os.path.join(main_folder_path, f'*{ext}')):
        shutil.move(file_path, videos_folder)

# Move other files
for ext in other_extensions:
    for file_path in glob.glob(os.path.join(main_folder_path, f'*{ext}')):
        shutil.move(file_path, others_folder)

print("Files have been organized into 'Images', 'Videos', and 'Others' folders.")
