# The code uses the OpenCV library for image processing.
# It defines a function select_roi to interactively select a region of interest (ROI) in an image
# using the cv2.selectROI function. The selected ROI is then used to crop the image and create a mask.
#
# The segment_vocal_cord_hole function loads an image in grayscale format, calls the select_roi function
# to select the ROI and create a mask. It then applies histogram equalization to enhance the contrast of the ROI image.
# After that, a thresholding operation is applied to obtain a binary image. Contours are then found in the binary image
# and filtered based on their area. A blank mask image is created, and the contour of the vocal cord hole
# is drawn on the mask using the filtered contours. Finally, the mask is applied to the original image
# using a bitwise operation to segment the vocal cord hole. The segmented vocal cord hole is displayed using cv2.imshow.

import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

# Example Usage
# python vc_segmenter.py --directory /data/images/frame40.png /home/guibo/repos

def select_roi(image):
    # Display the image and allow the user to draw a ROI
    roi = cv2.selectROI(image)

    # Crop the image based on the selected ROI
    cropped_image = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Create a mask with the same size as the original image
    mask = np.zeros_like(image)
    mask[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = 255

    return cropped_image, mask, roi

def segment_vocal_cord_hole(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Select the region of interest (ROI) and create a mask
    roi_image, roi_mask, roi = select_roi(image)

    # Apply histogram equalization to enhance contrast
    equalized = cv2.equalizeHist(roi_image)

    # Thresholding to obtain binary image
    threshold_value = 140  # Adjust threshold value as needed
    _, binary = cv2.threshold(equalized, threshold_value, 255, cv2.THRESH_BINARY)

    # Find contours of the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area
    min_area = 150  # Minimum contour area threshold
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    # Create a blank mask image for the region of interest
    mask = np.zeros_like(roi_image)

    # Draw the contour of the vocal cord hole on the mask
    cv2.drawContours(mask, filtered_contours, -1, (255), thickness=cv2.FILLED)

    # Apply morphological opening to remove small regions
    kernel_size = 1  # Adjust kernel size as needed
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Apply the mask to the original image using bitwise operation
    segmented_image = cv2.bitwise_and(roi_image, roi_image, mask=opened_mask)

    # Create a final image with the same size as the original image
    final_image = np.copy(image)
    final_image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = segmented_image

    # Display the final segmented vocal cord hole
    cv2.imshow("Segmented Vocal Cord Hole", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# It shows 6 different methods for tests
# Image operation using thresholding
def segment_vocal_methods(image_path):
    # Read the image file
    with open(image_path, 'rb') as f:
        image_data = f.read()
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Image operation using thresholding
    # image_path1 = 'data_source/reco_001/segmented_png/vocal_18 - 2.jpg'
    # image_path2 = 'data_source/reco_001/segmented_png/coin-detection.jpg'
    # img = cv2.imread(image_path1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # newimg - bitwise_not
    darker = cv2.equalizeHist(gray)
    ret,thresh = cv2.threshold(darker,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    newimg = cv2.bitwise_not(thresh)

    # Change the threshold value here
    threshold_value = 100

    # Simple Thresholding
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Adaptive Thresholding
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Otsu's Thresholding
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Close area
    # Noise removal using Morphological
    # closing operation
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE,
                               kernel, iterations=2)

    # Background area using Dilation
    bg = cv2.dilate(closing, kernel, iterations=1)

    # Finding foreground area
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02
                            * dist_transform.max(), 255, 0)


    # Display the results
    titles = ['Original', 'Simple Thresholding', 'Adaptive Thresholding', "Otsu's Thresholding", 'newimg', 'fg']
    images = [gray, binary, adaptive, otsu, newimg, fg]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Vocal Cord Hole Segmentation')

    # Add an argument for the image directory
    parser.add_argument('--directory', type=str, required=True, help='Path to the endoscopy image directory')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the image directory path from the command-line argument
    image_dir = args.directory

    # Perform vocal cord hole segmentation, show different methods
    segment_vocal_methods(image_dir)

    # Perform vocal cord hole segmentation
    segment_vocal_cord_hole(image_dir)