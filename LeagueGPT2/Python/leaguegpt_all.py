import os
import openai

def send_message_to_chatgpt(api_key, messages):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response['choices'][0]['message']['content']

def read_last_line_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
    return None

def main():
    # Replace 'your_api_key' with your actual OpenAI API key.
    api_key = "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"

    # Replace 'messages_all.txt' with the name of your messages file with [ALL].
    messages_file_name = "messages_all.txt"

    # Your intro message to ChatGPT.
    intro_message = "I am playing a game of league of legends and I need you to respond to my teammate's messages for me, try not to be overly polite and try to keep your messages to one or two sentences so that they can be easily sent through the game chat. Please assume that what I'm saying is an ingame message I need you to respond to. While you are responding as me try to act as a toxic league player would. Do not use quotation marks or any other unneeded formatting in your messages. Everything you send to me will be what is put into the game. You should try to make clever comebacks and all your responses should be funny in some way."

    # Read the last message from messages_all.txt.
    last_message = read_last_line_from_file(messages_file_name)

    if last_message:
        # Prepare messages for ChatGPT, including the intro message and the last user message.
        messages = [{"role": "system", "content": intro_message}, {"role": "user", "content": last_message}]

        # Send messages to ChatGPT.
        response = send_message_to_chatgpt(api_key, messages)

        # Save ChatGPT's response to the output text file.
        with open("response_all.txt", "w") as file:
            file.write(response)

if __name__ == "__main__":
    main()
