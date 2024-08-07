from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class SimpleImageEncryptor:
    def __init__(self, key):
        self.key = key

    def _xor_pixels(self, pixels):
        return np.bitwise_xor(pixels, self.key)

    def process_image(self, image_path, output_path, operation):
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            pixels = np.array(img)
            if operation == 'encrypt':
                processed_pixels = self._xor_pixels(pixels)
            elif operation == 'decrypt':
                processed_pixels = self._xor_pixels(pixels)
            else:
                raise ValueError("Operation must be 'encrypt' or 'decrypt'")
            processed_image = Image.fromarray(processed_pixels.astype('uint8'))
            processed_image.save(output_path)
            return processed_image

def get_user_input():
    while True:
        try:
            key = int(input("Please enter the encryption key (a number): "))
            return key
        except ValueError:
            print("Invalid key. Please enter a valid integer.")

def get_operation():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
        if choice in ['e', 'd']:
            return 'encrypt' if choice == 'e' else 'decrypt'
        else:
            print("Invalid choice. Please type 'e' for encrypt or 'd' for decrypt.")

def get_image_paths():
    input_path = input("Please enter the path of the input image: ")
    output_path = input("Please enter the path for the output image: ")
    return input_path, output_path

def display_images(input_path, output_path, input_title, output_title):
    def display_image(image_path, title):
        img = Image.open(image_path)
        plt.imshow(img)
        plt.title(title)
        plt.axis('off')
        plt.show()

    display_image(input_path, input_title)
    display_image(output_path, output_title)

def main():
    key = get_user_input()
    operation = get_operation()
    input_image_path, output_image_path = get_image_paths()

    encryptor = SimpleImageEncryptor(key)
    processed_image = encryptor.process_image(input_image_path, output_image_path, operation)
    
    operation_title = "Encrypted Image" if operation == 'encrypt' else "Decrypted Image"
    print(f"The image has been {operation}ed and saved to {output_image_path}.")
    display_images(input_image_path, output_image_path, "Original Image", operation_title)

if __name__ == "__main__":
    main()
