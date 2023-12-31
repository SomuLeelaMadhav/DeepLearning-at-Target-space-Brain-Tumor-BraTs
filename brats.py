##### Model which i created, and Its code is not mentioned here ####




!pip install tensorflow

import os
import random
import nibabel as nib
import matplotlib.pyplot as plt

# Define the path to your dataset folder in Google Drive
dataset_folder = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/'
# Get a list of all NIfTI files in the folder
nii_files = [f for f in os.listdir(dataset_folder) if f.endswith('.nii.gz')]

# Shuffle the list of NIfTI files
random.shuffle(nii_files)

# Choose up to 10 random NIfTI files, or all if there are fewer than 10
num_files_to_display = min(10, len(nii_files))
random_files = nii_files[:num_files_to_display]

# Display the random images
plt.figure(figsize=(15, 8))
for i, file_name in enumerate(random_files):
    file_path = os.path.join(dataset_folder, file_name)
    img = nib.load(file_path).get_fdata()

    plt.subplot(2, 5, i + 1)
    plt.imshow(img[:, :, img.shape[2] // 2], cmap='gray')
    plt.title(f'Image {i+1}')
    plt.axis('off')

plt.tight_layout()
plt.show()

import nibabel as nib
import matplotlib.pyplot as plt

# Define the path to your NIfTI image
image_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/BraTS20_Training_002/BraTS20_Training_002_flair.nii'

# Load the NIfTI image
img = nib.load(image_path).get_fdata()

# Display the image
plt.imshow(img[:, :, img.shape[2] // 2], cmap='gray')
plt.title('BraTS20_Training_002_flair.nii')
plt.axis('off')
plt.show()

import nibabel as nib
import matplotlib.pyplot as plt

# Define the path to your NIfTI image
image_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/BraTS20_Training_002/BraTS20_Training_002_t1.nii'

# Load the NIfTI image

img = nib.load(image_path).get_fdata()
# Display the image
plt.imshow(img[:, :, img.shape[2] // 2], cmap='gray')
plt.title('BraTS20_Training_002_flair.nii')
plt.axis('off')
plt.show()


##### Model which i created, and Its code is not mentioned here ####


import os
import nibabel as nib
import matplotlib.pyplot as plt

# Define the base path to the BraTS dataset
base_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData'

# Define the folder name you want to display (e.g., "002")
folder_name = 'BraTS20_Training_002'

# Create the full path to the specified folder
folder_path = os.path.join(base_path, folder_name)

# Get a list of all NIfTI files in the specified folder
nii_files = [f for f in os.listdir(folder_path) if f.endswith('.nii')]

# Display the images in the folder
plt.figure(figsize=(15, 8))
for i, file_name in enumerate(nii_files):
    file_path = os.path.join(folder_path, file_name)
    img = nib.load(file_path).get_fdata()

    plt.subplot(1, len(nii_files), i + 1)
    plt.imshow(img[:, :, img.shape[2] // 2], cmap='gray')
    plt.title(f'{file_name}')
    plt.axis('off')

plt.tight_layout()
plt.show()

import os
import nibabel as nib
import matplotlib.pyplot as plt

# Define the base path to the BraTS dataset
base_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData'

# Define the folder name you want to display (e.g., "002")
folder_name = 'BraTS20_Training_002'

# Create the full path to the specified folder
folder_path = os.path.join(base_path, folder_name)

# Get a list of all NIfTI files in the specified folder
nii_files = [f for f in os.listdir(folder_path) if f.endswith('.nii')]

# Display the images in the folder
plt.figure(figsize=(15, 8))
for i, file_name in enumerate(nii_files):
    file_path = os.path.join(folder_path, file_name)
    img = nib.load(file_path).get_fdata()

    plt.subplot(1, len(nii_files), i + 1)
    plt.imshow(img[:, :, img.shape[2] // 2])
    plt.title(f'{file_name}')
    plt.axis('off')

plt.tight_layout()
plt.show()

import nibabel as nib
import matplotlib.pyplot as plt

# Load the image using nibabel
image_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/BraTS20_Training_002/BraTS20_Training_002_flair.nii'
img = nib.load(image_path)

# Choose a slice to display (e.g., slice 80 in the z-axis)
slice_to_display = 80

# Extract the 2D slice from the 3D image
slice_img = img.get_fdata()[:, :, slice_to_display]

# Display the 2D slice
plt.imshow(slice_img, cmap='gray')
plt.axis('off')
plt.show()

import nibabel as nib
import matplotlib.pyplot as plt

# Load the image using nibabel
image_path = '/content/drive/MyDrive/Brats20/BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/BraTS20_Training_002/BraTS20_Training_002_t2.nii'
img = nib.load(image_path)

# Extract a 2D slice from the 3D image (e.g., slice 80 from the third dimension)
slice_to_display = 80
slice_img = img.get_fdata()[:, :, slice_to_display]

# Display the 2D slice in color
plt.imshow(slice_img)
plt.axis('off')
plt.show()

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained model
model = keras.models.load_model('/content/brain_tumor_model_updated.h5')

# Load and preprocess the sample image
img_path = '/content/BraTS2020_TestingData_023.jpeg'  # Replace with the actual path to your sample image
img = Image.open(img_path)
img = img.resize((128, 128))  # Resize the image to match the model's input shape
img = img.convert('L')  # Convert the image to grayscale
img = np.array(img)
img = img.reshape(1, 128, 128, 1)  # Reshape to (1, 128, 128, 1)

# Make predictions
predictions = model.predict(img)

# Decode the predictions (if you have class labels)
# Replace class_labels with the actual labels your model uses
class_labels = ['No Tumor', 'Tumor']
predicted_class = class_labels[np.argmax(predictions)]

# Create a nice visualization
plt.imshow(img[0, :, :, 0], cmap='gray')
plt.title(f"Predicted Class: {predicted_class}")
plt.axis('off')  # Turn off axis labels
plt.show()

