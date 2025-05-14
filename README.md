# Background Removal and Replacement using DeepLabv3

## Overview
This project uses the **DeepLabv3** model from PyTorch to perform background removal and replacement. The person is segmented out from the foreground image and replaced with a custom background image.

## Technologies Used
- **Python**: Programming language
- **PyTorch**: Pre-trained DeepLabv3 model
- **OpenCV**: Image processing tasks
- **NumPy**: Array manipulation
- **PIL (Pillow)**: Image handling

## Usage

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/background-removal.git
cd background-removal

### Step 2: Install Dependencies
```bash
pip install torch torchvision opencv-python numpy Pillow

### Step 3: Prepare Images

Ensure you have:

foreground.jpg: The image with the foreground (person).

background.jpg: The image to replace the background.

### Step 4:  Run the Program
```bash
python virtual-bg.py

This will process the input and generate output.jpg with the new background.
