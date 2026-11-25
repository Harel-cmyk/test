
import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 700, 3), dtype=np.uint8)

# Draw three white shapes
cv2.rectangle(image, (50, 50), (200, 200), (255, 255, 255), -1)

cv2.circle(image, (350, 125), 75, (255, 255, 255), -1)

triangle = np.array([
    [500, 200],
    [600, 200],
    [550, 50]
], dtype=np.int32)

cv2.fillPoly(image, [triangle], (255, 255, 255))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find contours
contours, hierarchy = cv2.findContours(
    gray,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours and bounding boxes
result = image.copy()

for i, contour in enumerate(contours):

    area = cv2.contourArea(contour)

    x, y, w, h = cv2.boundingRect(contour)

    cv2.drawContours(result, [contour], -1, (0, 255, 0), 3)

    cv2.rectangle(
        result,
        (x, y),
        (x + w, y + h),
        (0, 0, 255),
        2
    )

    print(f"Object {i + 1}")
    print("Area:", area)
    print("Bounding Box:", x, y, w, h)
    print("----------------")

# Save images
cv2.imwrite("contours_original.jpg", image)
cv2.imwrite("contours_result.jpg", result)

print("Contours detected:", len(contours))

