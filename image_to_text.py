# Reference
# (reference) https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/

# Used openCV to open image in ram, 
# than used 'Python-tesseract' by Google it will used for recognise texts from images.

import pytesseract
from PIL import Image

# Tesseract executable path   "vary upon installation as per system."
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    lines = text.split('\n')
    lines = [line for line in lines if line.strip() != '']

    final_text = ''

    for i in lines:
        final_text += i + " "
    return final_text


# it only executes when running it self, not execute if import by other module.
if __name__ == "__main__":
    image_path = 'Images\\Amitabh Bachchan.png'
    extracted_text = extract_text_from_image(image_path)
    print(extracted_text)
