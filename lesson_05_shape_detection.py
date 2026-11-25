
import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 700, 3), dtype=np.uint8)

# Draw a white rectangle
cv2.rectangle(
    image,
    (50, 50),
    (200, 200),
    (255, 255, 255),
    -1
)

# Draw a white circle
cv2.circle(
    image,
    (350, 125),
    75,
    (255, 255, 255),
    -1
)

# Draw a white triangle
triangle = np.array([
    [500, 200],
    [600, 200],
    [550, 50]
], dtype=np.int32)

cv2.fillPoly(image, [triangle], (255, 255, 255))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a binary image
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Find contours
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = image.copy()

for contour in contours:

    # Calculate contour perimeter
    perimeter = cv2.arcLength(contour, True)

    # Approximate contour with a polygon
    epsilon = 0.05 * perimeter
    approx = cv2.approxPolyDP(
        contour,
        epsilon,
        True
    )

    # Count polygon vertices
    vertices = len(approx)

    # Classify shape
    if vertices == 3:
        shape = "Triangle"

    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)

        aspect_ratio = w / float(h)

        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    else:
        shape = "Circle"

    # Draw approximated polygon
    cv2.drawContours(
    result,
    [approx],
    -1,
    (0, 255, 0),
    2
)

    # Get position for text
    x, y, w, h = cv2.boundingRect(contour)

    cv2.putText(
        result,
        shape,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    print("Detected shape:", shape)
    print("Number of vertices:", vertices)
    print("--------------------")

# Save results
cv2.imwrite("lesson_05_original.jpg", image)
cv2.imwrite("lesson_05_result.jpg", result)

print("Shape detection completed!")
