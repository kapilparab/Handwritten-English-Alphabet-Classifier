import cv2

img_path = ''
output_path = ''

# Read image
img = cv2.imread(img_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize Image
result = cv2.resize(gray, (28,28), interpolation = cv2.INTER_AREA)

# Invert image (black to white, white to black)
result = cv2.bitwise_not(result)

# Write new image
cv2.imwrite(output_path, result)