import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a black image with specified height and width
image_height, image_width = 400, 400
image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# Draw a filled white square on the image
cv2.rectangle(image, (50, 50), (150, 150), (255, 255, 255), -1)

# Draw a filled white circle on the image
cv2.circle(image, (300, 100), 50, (255, 255, 255), -1)

# Draw a filled white rectangle on the image
cv2.rectangle(image, (200, 200), (350, 300), (255, 255, 255), -1)

# Draw a wavy line using small filled circles
for x in range(0, 400):
    # Calculate the y-coordinate using a sine function for a wavy effect
    y = int(200 + 20 * np.sin(x * 0.1))
    cv2.circle(image, (x, y), 1, (255, 255, 255), -1)

# Save the created image to a file
cv2.imwrite('shapes.png', image)

# Display the created image using Matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.axis('off')  # Hide axis ticks and labels
plt.title('Shapes Image')  # Set the title of the plot
plt.show()  # Show the plot

# Load the saved image using OpenCV
image = cv2.imread('shapes.png')

# Convert the loaded image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')  # Use grayscale colormap
plt.axis('off')  # Hide axis ticks and labels
plt.title('Grayscale Image')  # Set the title of the plot
plt.show()  # Show the plot

# Apply a simple thresholding technique to create a binary image
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
plt.imshow(binary_image, cmap='gray')  # Use grayscale colormap
plt.axis('off')  # Hide axis ticks and labels
plt.title('Binary Image')  # Set the title of the plot
plt.show()  # Show the plot

# Display the histogram of pixel values
plt.figure(figsize=(12, 6))  # Set the figure size

# Subplot for the grayscale image
plt.subplot(1, 2, 1)
plt.title('Grayscale Image')  # Set the title for the grayscale image
plt.imshow(gray_image, cmap='gray')  # Display the grayscale image
plt.axis('off')  # Hide axis ticks and labels

# Subplot for the histogram
plt.subplot(1, 2, 2)
plt.title('Histogram')  # Set the title for the histogram
plt.hist(gray_image.flatten(), bins=256)  # Calculate and plot the histogram
plt.xlim([0, 256])  # Set x-axis limits to cover the full range of pixel values

plt.show()  # Show the plots

# Function to detect edges using the Canny edge detector
def detect_edges(image):
    # Apply Canny edge detection with specified thresholds
    edges = cv2.Canny(image, 100, 200)
    return edges  # Return the detected edges

# Detect edges in the grayscale image
edges = detect_edges(gray_image)

# Display the edges detected in the image
plt.figure(figsize=(6, 6))  # Set the figure size
plt.title('Edges Detected')  # Set the title of the plot
plt.imshow(edges, cmap='gray')  # Display the edges using grayscale colormap
plt.axis('off')  # Hide axis ticks and labels
plt.show()  # Show the plot