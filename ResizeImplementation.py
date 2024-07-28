import cv2
import numpy as np


def bilinear_interpolation(image, x, y):

    # Convert to integer
    x1 = int(x)
    y1 = int(y)
    # Make sure they are within image bounds
    x2 = min(x1 + 1, image.shape[0] - 1)
    y2 = min(y1 + 1, image.shape[1] - 1)

    # Get pixel values at the corners
    Q11 = image[x1, y1]
    Q12 = image[x1, y2]
    Q21 = image[x2, y1]
    Q22 = image[x2, y2]

    # Interpolation
    R1 = (x2 - x) * Q11 + (x - x1) * Q12
    R2 = (x2 - x) * Q21 + (x - x1) * Q22
    return (y2 - y) * R1 + (y - y1) * R2


def resize_image(image_path, new_height, new_width):
    # Read image and convert it into grey scale
    image = cv2.imread(image_path, 0)

    # Check if the image path is valid
    if image is None:
        print("Invalid path")
        return

    # Get original image height and width
    height, width = image.shape[:2]

    # Calculate coefficients
    a = height / new_height
    b = width / new_width

    print("Coefficients: a = ", a, "& b = ", b)
    # fill a new array with zeros (initial value), the array is of size new_height and new_width
    resized_image = np.zeros((new_height, new_width), dtype=np.uint8)

    # Iterate the new image and calculate the interpolated value for each pixel, assign to the new array to fill it
    for i in range(new_height):
        for j in range(new_width):
            x = i * a
            y = j * b
            resized_image[i, j] = bilinear_interpolation(image, x, y)

    # Show the resized image
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Method to get the height and width of the original image
def original_image(image_path):
    image = cv2.imread(image_path, 0)

    # Check if the path is valid
    if image is None:
        print("Invalid path")
        return

    # Get original image dimensions
    height, width = image.shape[:2]
    print("The height and width for the original image are:\nheight: ", height, " width: ", width)


def main():
    # Let the user enter the path of the image then show the width and height of the image
    image_path = input("Enter the path to the image: ")
    original_image(image_path)

    # Continue if path is valid
    if cv2.imread(image_path, 0) is not None:
        user_input_valid = False
        while not user_input_valid:
            new_height = input("Enter the new height for the image to resize: ")
            new_width = input("Enter the new width for the image to resize: ")

            # Check if inputs are digits
            if new_height.isdigit() and new_width.isdigit():
                new_height, new_width = int(new_height), int(new_width)
                user_input_valid = True
            else:
                print("Invalid input. enter integers for height and width.")
        # Call resize method with user inputs
        resize_image(image_path, new_height, new_width)


if __name__ == "__main__":
    main()

