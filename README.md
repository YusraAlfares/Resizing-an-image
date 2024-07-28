# Image resizing using python 
This is a python code using Bilinear interpolation to resize an image. 
Bilinear interpolation is a type of interpolation used to estimate the value of a function at a specific point, given its known values at surrounding points.

## Methods in the code

1- bilinear_interpolation(image, x, y)
This method performs bilinear interpolation to calculate the pixel value at a specific coordinate (x, y) in the image.

Parameters:

image: The original image array.
x: The x-coordinate (horizontal position).
y: The y-coordinate (vertical position).

Process:
Converts x and y to integer to find the surrounding pixel coordinates.
Ensures the coordinates are within the image bounds.
Retrieves the pixel values at the corners of the cell containing (x, y).
Performs interpolation in the x-direction followed by the y-direction to compute the final interpolated pixel value.

2- resize_image(image_path, new_height, new_width)
This method resizes the image to the specified dimensions using bilinear interpolation.

Parameters:

image_path: The file path of the original image (given by the user).
new_height: The desired height of the resized image (given by the user).
new_width: The desired width of the resized image (given by the user).

Process:
Reads the image and convert it to grayscale.
Validates the image path.
Calculates the coefficients (a & b).
Initializes an array for the resized image.
Iterates over each pixel in the resized image and compute its value using bilinear interpolation.
Displays the resized image.

3- original_image(image_path)
This method displays the original dimensions of the selected image.

Parameters:

image_path: The file path of the original image.

Process:
Reads the image and convert it to grayscale.
Validates the image path.
Prints the height and width of the original image.

