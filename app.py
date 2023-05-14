from flask import Flask, render_template, request, jsonify, Response
from pdfminer.high_level import extract_text
import sseclient
import requests
import openai
import json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

API_KEY = os.getenv('OPENAI_API_KEY')
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
openai.api_key  = API_KEY

app = Flask(__name__)
model = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    model_num = request.form["model_num"]
    user_query = request.form["user_query"]
    system_message = request.form["system_message"]
    pdf_file = request.files.get("pdf-upload")

    if model_num == "1":
        model = "gpt-3.5-turbo"
    elif model_num == "2":
        model = "gpt-4"
    else:
        return jsonify({"error": "Invalid model selection"})

    messages = []

    if system_message:
        messages.append({"role": "system", "content": system_message})
        
    # Extract text from PDF and append it to the user query
    if pdf_file:
        pdf_text = extract_text(pdf_file)
        user_query = f"""
        {user_query}
        Here is the text to analyze based on the aforementioned query,\
        delimited with triple backticks: ```{pdf_text}```
        """
    
    messages.append({"role": "user", "content": user_query})

    gpt_response = generate_chat_completion(messages, model)
    gpt_response = gpt_response.strip()
    return jsonify({"gpt_response": gpt_response})

def generate_chat_completion(messages, model=model, temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": 4000,
    }

#    if max_tokens is not None:
#        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    app.run(debug=True)
    
#
#You are a Computer Security & Investigations professor at a University, with 10+ years of /
#experience in penetration testing. You will provide advice on how a student can complete/
#their assignment. All code #blocks will be delimited with triple backticks, and all code /
#will be formatted and commented in accordance with the Google Style Guide.
#