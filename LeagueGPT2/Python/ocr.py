import pytesseract
from PIL import Image
import os

def extract_messages_from_image(image_path):
    image = Image.open(image_path)
    ocr_text = pytesseract.image_to_string(image)

    # Split the OCR text into individual lines.
    lines = ocr_text.splitlines()

    # Filter and extract lines containing [Team] or [All] tags.
    team_messages = [line for line in lines if "[Team]" in line]
    all_messages = [line for line in lines if "[All]" in line]

    return team_messages + all_messages

def main():
    # Process all image files in the current directory.
    for filename in os.listdir("."):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            messages = extract_messages_from_image(filename)

            # Append the extracted messages to the messages.txt file.
            with open("messages.txt", "a") as messages_file:
                messages_file.write('\n'.join(messages) + '\n')

if __name__ == "__main__":
    main()
