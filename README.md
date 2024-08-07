## Simple Image Encryptor

## Description

The Simple Image Encryptor is a basic tool for encrypting and decrypting images using XOR-based encryption. This Python script leverages the Pillow library (`PIL`) for image processing, NumPy for pixel manipulation, and Matplotlib for displaying images. The tool provides a straightforward way to apply a symmetric encryption technique to image files, useful for learning about basic image encryption and decryption methods.

## Features

- **XOR Encryption/Decryption**: Utilizes the XOR operation to encrypt and decrypt image pixels, providing a simple form of symmetric encryption.
- **User Input**: Prompts the user for a numeric key, operation type (encrypt or decrypt), and file paths for input and output images.
- **Image Display**: Shows the original and processed images using Matplotlib for visual verification.
- **Flexible**: Supports any image format supported by Pillow, as long as it can be converted to RGB.

## Requirements

- Python 3.x
- Pillow (`PIL`) library
- NumPy library
- Matplotlib library

You can install the necessary Python packages using pip:

```bash
pip install pillow numpy matplotlib
```

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/aiwin2002/PRODIGY_CS_2.git

   cd PRODIGY_CS_2
   ```

2. **Run the Script**:

   Execute the script using Python. The script will prompt you for the required inputs:

   ```bash
   python imageencrypt.py
   ```

3. **Provide Input**:

   - **Key**: Enter a numeric key for encryption/decryption (a single integer).
   - **Operation**: Choose whether to encrypt or decrypt the image by typing 'e' or 'd'.
   - **Input Image Path**: Provide the path to the image you want to process.
   - **Output Image Path**: Specify the path where the processed image will be saved.

4. **View Results**:

   After processing, the script will display the original and processed images. Check the output path for the saved image.

## Example

```bash
Please enter the encryption key (a number): 123
Do you want to encrypt or decrypt an image? (e/d): e
Please enter the path of the input image: input_image.jpg
Please enter the path for the output image: output_image.jpg
```

The image `input_image.jpg` will be encrypted and saved as `output_image.jpg`. If you choose decryption (`d`), the script will decrypt the image and save it to the specified output path.
