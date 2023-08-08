def reset_messages_file(file_path):
    # Open the messages.txt file in write mode to clear its content.
    with open(file_path, "w") as file:
        file.write("")

def reset_last_line_number(file_path):
    # Set the last line number to 0 in the last_line_number.txt file.
    with open(file_path, "w") as file:
        file.write("0")

def main():
    # Replace 'messages.txt' with the name of your messages file.
    messages_file_path = "messages.txt"

    # Replace 'last_line_number.txt' with the name of your last line number file.
    last_line_number_file_path = "last_line_number.txt"

    # Reset the messages.txt file and the last line number to 0.
    reset_messages_file(messages_file_path)
    reset_last_line_number(last_line_number_file_path)

if __name__ == "__main__":
    main()
