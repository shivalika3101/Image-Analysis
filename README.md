# Image Analysis

This project is a simple desktop image-processing app built with Python and Tkinter. It lets you open an image and apply basic analysis or editing operations through buttons in a graphical interface.

## Features

- Convert an image to grayscale
- Flip an image horizontally or vertically
- Rotate an image by 90 degrees
- Show image size, width, and height
- Blur an image
- Split an image into red, green, and blue channels
- Apply threshold-based point processing
- Paste one image onto another
- Detect image outlines
- Crop the image to its top-left quarter
- Print the image histogram

## Requirements

- Python 3.10 or newer is recommended
- The Python packages listed in `requirements.txt`

## Setup

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run The App

Start the GUI with:

```powershell
python "Image Analysis.py"
```

## How To Use

1. Run the script.
2. In the first window, click `click here to proceed`.
3. In the main image analysis window, choose any operation.
4. Pick an image file when the file dialog opens.
5. The selected operation will display the result in a new image preview or print details to the console.

## Notes

- If a feature prints information such as image properties or histogram values, check the terminal where you launched the script.
- Some features open multiple preview windows because they show both the original and processed versions.
- If you cancel the file picker, the action will safely stop without crashing.
