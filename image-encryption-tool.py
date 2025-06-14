from PIL import Image
import random

def encrypt_image(image_path, output_path, key=10):
    img = Image.open(image_path)
    pixels = img.load()
    
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Add a key to each RGB value (mod 256 to stay in valid range)
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    img.save(output_path)
    print("Encryption done.")

def decrypt_image(image_path, output_path, key=10):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Subtract the key to reverse encryption
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print("Decryption done.")

# Example usage:
# encrypt_image("original.jpg", "encrypted.jpg", key=25)
# decrypt_image("encrypted.jpg", "decrypted.jpg", key=25)
