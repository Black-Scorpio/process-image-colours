# Disassemble the Colours!

This is a Flask web application that allows users to upload an image and analyze the most common colors in the image. The application resizes the image to a maximum of 800x600, clusters similar colors, and displays the most common colors along with their hex codes.

## Features

- Drag and drop or click to upload an image.
- Image resizing to a maximum of 800x600 while maintaining the aspect ratio.
- Clustering of similar colors using KMeans.
- Display of the most common colors and their hex codes.
- Responsive and user-friendly interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Black-Scorpio/process-image-colours.git
    cd process-image-colours
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to:

    ```
    http://127.0.0.1:5000
    ```

## Instructions to Use

1. **Drag and drop an image** into the designated area or **click to upload** an image.
2. The image will be resized to a maximum of 800x600 if necessary.
3. The application will process the image and display the most common colors and their hex codes below the image.

## Customization

Feel free to customize the styling and functionality as per your requirements. The main logic for handling image upload, processing, and displaying colors is in `app.py`, `styles.css`, and `script.js`.


