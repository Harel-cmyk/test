
import cv2
import numpy as np

# Create an empty image: height=400, width=600, 3 color channels
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw a red rectangle
cv2.rectangle(
    image,
    (50, 50),
    (250, 200),
    (0, 0, 255),
    3
)

# Draw a green circle
cv2.circle(
    image,
    (400, 150),
    70,
    (0, 255, 0),
    -1
)

# Add text
cv2.putText(
    image,
    "KIMA Computer Vision",
    (50, 300),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Print image information
print("Image shape:", image.shape)
print("Image data type:", image.dtype)

# Save the image
cv2.imwrite("lesson_01_output.jpg", image)

print("Image saved successfully!")
