import numpy as np
from PIL import Image
from collections import Counter


def main():
    """
    The main function that calls the detect_image function.
    """
    detect_image()


def detect_image():
    """
    Detects the most common pixel colors in an image and displays their information.
    """
    image_path = input("Enter the Path or the name of the Image File: ")
    my_img = Image.open(image_path)
    img_array = np.array(my_img)
    my_list = []

    # Extract pixel values and create a list
    for row in img_array:
        for pixel in row:
            pixel_values = tuple(pixel)
            my_list.append(pixel_values)

    pixel_counter = Counter(my_list)
    most_common_pixels = pixel_counter.most_common(10)
    total_pixels = len(my_list)

    # Process and display most common pixel colors
    for pixel, count in most_common_pixels:
        hex_code = rgb_to_hex(pixel)
        percentage = (count / total_pixels) * 100
        print(f"Pixel color: {pixel}, Hex Code: {hex_code}, Count: {count}, Percentage: {percentage:.2f}%")
        visualize_color(pixel)


def visualize_color(rgb):
    """
    Creates and displays a color image with the given RGB values.
    """
    color_image = Image.new("RGB", (100, 100), rgb)
    color_image.show()


def rgb_to_hex(rgb):
    """
    Converts an RGB tuple to a hex color code.
    """
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


if __name__ == "__main__":
    main()
