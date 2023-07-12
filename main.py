import os
import re
import image_to_text
import text_summarizer

def list_image_files(folder_path):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]  # Add more extensions if needed
    image_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension.lower() in image_extensions:
                image_files.append(os.path.join(root, file))

    return image_files

def replace_invalid_characters(filename):
    invalid_chars = r'[<>:"/\\|?*]'
    return re.sub(invalid_chars, '_', filename)

def get_valid_image_name(summary):
    name = ''
    counter = 0
    for word in summary.split():
        name += word.capitalize() + " "
        counter += 1
        if counter == 2:
            break

    return name.strip() + ".png"






folder_path = input("Enter the folder path to rename images: ")
image_files = list_image_files(folder_path)

for image_file in image_files:
    try:
        text = image_to_text.extract_text_from_image(image_file)
        summary = text_summarizer.get_summary(text)
        name = get_valid_image_name(summary)

        if '"\\"' in name or '/' in name or name in os.listdir():
            continue
        os.rename(image_file, os.path.join(folder_path, replace_invalid_characters(name)))
    except:
        pass