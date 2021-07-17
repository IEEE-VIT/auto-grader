import cv2
import numpy as np


def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(
        *sorted(zip(cnts, boundingBoxes), key=lambda b: b[1][i], reverse=reverse)
    )

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


# Functon for extracting the box
def box_extraction(img_for_box_extraction_path, cropped_dir_path):

    print("Reading image..")
    image = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
    img = cv2.resize(image, (750, 1000))
    # img = cv2.flip(img, 1)
    (thresh, img_bin) = cv2.threshold(
        img, 228, 255, cv2.THRESH_BINARY_INV
    )  # Thresholding the image

    print("Storing binary image to ./samples/processed/Image_bin.jpg..")
    cv2.imwrite("./samples/processed/Image_bin.jpg", img_bin)

    print("Applying Morphological Operations..")
    # Defining a kernel length
    kernel_length = np.array(img).shape[1] // 40

    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation to detect verticle lines from an image
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
    cv2.imwrite("./samples/processed/verticle_lines.jpg", verticle_lines_img)

    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    cv2.imwrite("./samples/processed/horizontal_lines.jpg", horizontal_lines_img)

    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.5
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(
        verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0
    )
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(
        img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )

    # For Debugging
    # Enable this line to see verticle and horizontal lines in the image which is used to find boxes
    print(
        "Binary image which only contains boxes: ./samples/processed/img_final_bin.jpg"
    )
    cv2.imwrite("./samples/processed/img_final_bin.jpg", img_final_bin)
    # Find contours for image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    # Sort all the contours by top to bottom.
    (contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")

    print("Output stored in Output directiory!")

    idx = 0
    results = np.array([])
    for c in contours:
        # Returns the location and width,height for every contour
        x, y, w, h = cv2.boundingRect(c)

        # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
        if w > 10 and h > 10 and w < 26 and h < 26:
            idx += 1
            new_img = img[y : y + h, x : x + w]
            new_img = cv2.resize(new_img, (28, 28))
            # new_img = 255 - new_img
            (new_thresh, new_img) = cv2.threshold(new_img, 200, 255, cv2.THRESH_BINARY_INV)
            results = np.append(results, new_img)
            # new_idx = (19*(int((idx-1)/19)+1))-idx+1+(19*(int((idx-1)/19)))
            cv2.imwrite(cropped_dir_path + str(idx) + ".png", new_img)
    return results.reshape(-1,28,28,1)

    # For Debugging
    # Enable this line to see all contours.
    # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    # cv2.imwrite("./Temp/img_contour.jpg", img)
