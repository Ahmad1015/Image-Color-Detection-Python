# Project Overview
This project is a Python-based tool that detects the most common pixel colors in an image and displays detailed information about them, including their RGB values, hex codes, and their frequency in the image. Additionally, it visualizes these colors for better understanding.

## Features
- Color Detection: Identifies and counts the most common pixel colors in an image.
- Hex Code Conversion: Converts RGB values to hex color codes.
- Percentage Calculation: Calculates the percentage of each detected color relative to the total number of pixels.
- Color Visualization: Displays the most common colors in separate windows for easy visualization.
## Technology Stack
- Programming Language: Python
- Libraries:
  - numpy for handling image data as arrays
  - PIL (Python Imaging Library) for image processing
  - collections.Counter for counting pixel occurrences
## Setup Instructions
### Prerequisites
- Python 3.8+
- Required Python libraries (numpy, PIL)
## Installation
1. Clone the repository:
```bash
https://github.com/Ahmad1015/Image-Color-Detection-Python.git
cd Image-Color-Detection-Python
```
2. Install the required Python packages:
```bash
pip install numpy pillow
```
## Usage
Run the main script:
```bash
python main.py
```
## View the output:

The script will display the most common pixel colors along with their hex codes, counts, and percentages. Additionally, it will open windows showing these colors.

## Project Structure
- main.py: The main script that runs the program and contains the color detection logic.
Functions
- main(): The main function that calls the detect_image function.
- detect_image(): Detects the most common pixel colors in an image and displays their information.
- visualize_color(rgb): Creates and displays a color image with the given RGB values.
- rgb_to_hex(rgb): Converts an RGB tuple to a hex color code.
## Example Output
```
Enter the Path or the name of the Image File: example.jpg
Pixel color: (255, 255, 255), Hex Code: #ffffff, Count: 1500, Percentage: 30.00%
Pixel color: (0, 0, 0), Hex Code: #000000, Count: 1000, Percentage: 20.00%
...
