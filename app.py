from PIL import Image
import os

# Set the path to the data folder
data_folder = r'D:\BSCS\FYP\Mushroom Data'

# Function to resize images and save them
def resize_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        print(folder_path)
        for file in files:
            # Check if the file is an image (you may want to add more image extensions)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                try:
                    # Open the image file
                    img = Image.open(file_path)
                    # Resize the image to 224 x 224 (you can adjust this size as needed)
                    resized_img = img.resize((224, 224))
                    # Save the resized image
                    resized_img.save(file_path)
                    # # Optionally remove the original photo
                    # os.remove(file_path)
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")

# Iterate through each folder inside the data folder
for i in range(4):
    folder_path = os.path.join(data_folder, str(i))
    print(folder_path)
    resize_images(folder_path)


print("All images resized successfully!")