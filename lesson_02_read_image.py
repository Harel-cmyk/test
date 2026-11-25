
import cv2
import numpy as np

# Load image
image = cv2.imread("test_image.jpg")

if image is None:
    print("Error: Could not load image")
    exit()

# Basic image information
print("Image shape:", image.shape)
print("Image height:", image.shape[0])
print("Image width:", image.shape[1])
print("Number of channels:", image.shape[2])
print("Data type:", image.dtype)

# Read one pixel
pixel = image[100, 100]

print("Pixel at (100,100):", pixel)

# Convert BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save grayscale image
cv2.imwrite("grayscale.jpg", gray_image)

print("Images processed successfully!")
