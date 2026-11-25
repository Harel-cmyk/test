
import cv2

# Load image
image = cv2.imread("test_image.jpg")

if image is None:
    print("Error: Could not load image")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Edge Detection using Canny
edges = cv2.Canny(
    gray,
    100,
    200
)

edges_1 = cv2.Canny(gray, 30, 60)
edges_2 = cv2.Canny(gray, 100, 200)
edges_3 = cv2.Canny(gray, 200, 300)

cv2.imwrite("edges_low.jpg", edges_1)
cv2.imwrite("edges_medium.jpg", edges_2)
cv2.imwrite("edges_high.jpg", edges_3)

# Save results
cv2.imwrite("grayscale.jpg", gray)
cv2.imwrite("binary.jpg", binary)
cv2.imwrite("edges.jpg", edges)

print("Processing completed!")
print("Created: grayscale.jpg, binary.jpg, edges.jpg")
