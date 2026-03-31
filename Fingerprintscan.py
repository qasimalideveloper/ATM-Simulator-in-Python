import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image


def match_fingers(image_1_base64, image_2_base64, threshold=100):
    # Decode base64 strings to image arrays
    image_1_data = base64.b64decode(image_1_base64)
    image_2_data = base64.b64decode(image_2_base64)
 

   # Convert image data to OpenCV format
    image_1 = cv2.imdecode(np.frombuffer(image_1_data, np.uint8), cv2.IMREAD_GRAYSCALE)
    image_2 = cv2.imdecode(np.frombuffer(image_2_data, np.uint8), cv2.IMREAD_GRAYSCALE)

    # Create a SIFT object
    sift = cv2.SIFT_create()

    # Find key points and descriptors for both images
    keypoints_1, descriptors_1 = sift.detectAndCompute(image_1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image_2, None)

    # Initialize a Brute-Force Matcher
    bf = cv2.BFMatcher()

    # Match keypoint descriptors
    matches = bf.knnMatch(descriptors_1, descriptors_2, k=2)

    # Apply ratio test to select good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Calculate the matching score
    matching_score = len(good_matches)
    print(f"Matching Score: {matching_score}")

    # Check if the matching score exceeds the threshold
    if matching_score >= threshold:
        print("Fingerprints match!")
        return True
    else:
        print("Fingerprints do not match.")
        return False
    
with open("textfile (3).txt", "r") as file:
    image_1_base64 = file.read()
with open("textfile (2).txt", "r") as file:
    image_2_base64 = file.read()

match_fingers(image_1_base64,image_2_base64)
    