#-----------------------------------------------------
#   OpenAI API Script
#
#   Description:
#       Provides CLI access to OpenAI via API
#
#   Usage: 
#       python GPT4.py
#
#   Parameters:
#       This script has no parameters.
#
#   History:
#   Date        Author      Description
#   2023-05-10  A. Walker   Initial Creation
#   2023-05-13  A. Walker   Add comments
#-----------------------------------------------------

# Import necessary libraries
import requests
import json
import os
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variable for OpenAI API key
# Make sure the key is set in your environment!
# Examples:
# On Powershell use `$env:OPENAI_API_KEY = "API_KEY_HERE"`
# Command Prompt use `set OPENAI_API_KEY="API_KEY_HERE"`
# On Unix terminals use `export OPENAI_API_KEY="API_KEY_HERE"`
_ = load_dotenv(find_dotenv())  # Read local .env file

# Get OpenAI API key from environment variables
API_KEY = os.getenv('OPENAI_API_KEY')
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Set OpenAI API key for the OpenAI Python library
openai.api_key  = API_KEY

# Print available models
print("Models:")
print("1. GPT 3.5 Turbo")
print("2. GPT 4")

# Ask the user which model they want to use
try:
    model_num = input("Which model would you like to use? ")

    if model_num == "1":
        model = "gpt-3.5-turbo"
    elif model_num == "2":
        model = "gpt-4"
    else:
        print("Invalid selection, please try again.")
        
except:
    quit()

# Define function to generate chat completions
def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    """
    This function generates a response from the OpenAI Chat API given the 
    input messages.

    Args:
        messages (list): A list of message objects. Each object should be a 
                         dict with 'role' and 'content' keys.
        model (str): The name of the model to use.
        temperature (float): The temperature parameter for the API request.
        max_tokens (int, optional): The max_tokens parameter for the API request.

    Returns:
        str: The content of the message from the model.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
        
# Prompt the user to enter a prompt
prompt_content = input("Enter your prompt: ")

# Initialize messages list
messages = []

# Ask the user if they want to include a system message
system_message = input("Would you like to add a system message? ")
if system_message.lower() == "yes" or system_message.lower() == "y":
    system_content = input("Input system message: ")
    messages = [
    {"role": "system", "content": system_content},
    {"role": "user", "content": prompt_content}
    ]
    
elif system_message.lower() == "no" or system_message.lower() == "n":
    messages = [
    {"role": "user", "content": prompt_content}
    ]

# Generate a response using the OpenAI Chat API
response_text = generate_chat_completion(messages)

# Print the generated response
print(response_text
