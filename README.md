# Fun-Cam

**Fun-Cam** is a fun, interactive Python project that uses OpenCV to create a webcam feed with real-time **disco lights** and a **birthday message**. It also integrates face detection, allowing the effects to overlay dynamically on the video feed.

## Features
- **Real-time webcam feed** with dynamic overlays
- **Disco lights** randomly generated on the screen
- **Happy Birthday message** displayed in the center of the video
- **Face detection** using Haar Cascade to avoid covering faces with effects
- Simple and fun interactive experience

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Fun-Cam.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Fun-Cam
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```bash
   python happy_birthday.py
   ```

2. The webcam will open, displaying real-time video with disco lights and a "Happy Birthday" message. 

3. To exit, press **'q'**.

## Code Overview

- **add_disco_lights(frame)**: Adds randomly generated rectangles (disco lights) on the frame with random colors.
- **Face Detection**: Uses OpenCV’s Haar Cascade classifier to detect faces and ensure they are not covered by the disco lights.
- **Text Overlay**: Displays a "Happy Birthday" message in the center of the screen using OpenCV’s `putText` function.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required libraries using the `requirements.txt` file:

```bash
opencv-python
numpy
```
