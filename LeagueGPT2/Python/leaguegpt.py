import os
import openai

def send_message_to_chatgpt(api_key, messages):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" for the most capable model.
        messages=messages
    )

    return response['choices'][0]['message']['content']

def read_last_line_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Reverse the lines to read from the end of the file
        reversed_lines = reversed(lines)
        for line in reversed_lines:
            stripped_line = line.strip()
            if stripped_line:  # Check if the line is not empty
                return stripped_line
    return None


def main():
    # Replace 'your_api_key' with your actual OpenAI API key.
    api_key = "your_api_key"

    # Replace 'messages.txt' with the name of your messages file.
    messages_file_name = "messages.txt"

    # Your intro message to ChatGPT.
    intro_message = "I am playing a game of league of legends and I need you to respond to my teammate's messages for me, try not to be overly polite and try to keep your messages to one or two sentences so that they can be easily sent through the game chat. Please assume that what I'm saying is an ingame message I need you to respond to. While you are responding as me try to act as a toxic league player would. Do not use quotation marks or any other unneeded formatting in your messages. Everything you send to me will be what is put into the game. You should try to make clever comebacks and all your responses should be funny in some way."

    # Read the last message from messages.txt.
    last_message = read_last_line_from_file(messages_file_name)
    print("\nLast Message:", last_message, "\n")

    if last_message:
        # Prepare messages for ChatGPT, including the intro message and the last user message.
        messages = [
            {"role": "system", "content": intro_message},
            {"role": "user", "content": last_message}
        ]


        # Send messages to ChatGPT.
        response = send_message_to_chatgpt(api_key, messages)
        print("Response: ", response, "\n")

        # Save ChatGPT's response to the output text file.
        with open("response.txt", "w") as file:
            file.write(response)

        # Print last_message and intro_message from the messages list
        print("Last Message from Messages List:", messages[1]["content"])
        print("\n")
        print("Intro Message from Messages List:", messages[0]["content"])

if __name__ == "__main__":
    main()
