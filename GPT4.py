import requests
import json
import os
import openai

### Load env variable for API key
###
### Be sure this is actually set! Examples:
###
### On Powershell use `$env:OPENAI_API_KEY = "API_KEY_HERE"`
### Command Prompt use `set OPENAI_API_KEY="API_KEY_HERE"`
### On Unix terminals use `export OPENAI_API_KEY="API_KEY_HERE"`

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

API_KEY = os.getenv('OPENAI_API_KEY')
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
openai.api_key  = API_KEY

print("Models:")
print("1. GPT 3.5 Turbo")
print("2. GPT 4")

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

def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
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
        
prompt_content = input("Enter your prompt: ")
messages = []
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

response_text = generate_chat_completion(messages)
print(response_text)