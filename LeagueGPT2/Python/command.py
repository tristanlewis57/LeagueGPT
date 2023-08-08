import subprocess
import time
import pyperclip
import winsound
import re

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines


def clean_response():
    # Read the response text from response.txt.
    with open("response.txt", "r") as file:
        response_text = file.read()

    # Find the index of the first semicolon.
    first_semicolon_index = response_text.find(":")
    if first_semicolon_index != -1:
        # Remove everything before the first semicolon, including the semicolon itself.
        cleaned_response = response_text[first_semicolon_index + 1:].strip()
    else:
        cleaned_response = response_text.strip()

    return cleaned_response

def main():
    last_line_number_file = "last_line_number.txt"
    last_line_number = 0

    while True:
        # Step 1: Run the screenshot script.
        print("screenshot")
        subprocess.run(["python", "screenshot.py"])

        # Step 2: Run the OCR script.
        print("OCR")
        subprocess.run(["python", "ocr.py"])

        # Step 3: Read extracted lines from the messages.txt file.
        extracted_lines = read_lines_from_file("messages.txt")

        # Step 4: Check for new lines since the last iteration.
        with open(last_line_number_file, "r") as file:
            last_line_number = int(file.read().strip())

        num_lines = len(extracted_lines)
        num_new_lines = num_lines - last_line_number

        print(num_new_lines)
        print(num_lines)
        print(last_line_number)

        if num_new_lines > 0:
            # Step 5: Run the GPT script only if there are new lines.
            print("GPT")
            subprocess.run(["python", "leaguegpt.py"])

            # Step 6: Update the last_line_number file with the current line number.
            last_line_number = num_lines
            with open(last_line_number_file, "w") as file:
                file.write(str(last_line_number))

            cleaned_response = clean_response()
            pyperclip.copy(cleaned_response)
            print(cleaned_response)

            # Step 7: Copy the cleaned response text to the clipboard.
            pyperclip.copy(cleaned_response)
            winsound.Beep(500, 200)

        # Time delay (in seconds) between each iteration.
        time.sleep(1)  # Adjust the delay time as needed.

if __name__ == "__main__":
    main()
