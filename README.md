# GPT-Chat Web Application

This repository hosts a web application that utilizes OpenAI's GPT-3 or GPT-4 to generate responses to user queries. Users can optionally include a system message to provide context for the AI, or upload a PDF from which the application will extract text and add to the user query.


# Features

• User-friendly interface for querying the OpenAI API

• Support for both GPT-3.5-turbo and GPT-4 models

• Ability to add system messages to provide context to the AI

• Upload and extract text from PDFs to include in the query

• One-click install-and-run on Windows


# Installation

• To install the necessary dependencies, use pip:

  • pip install flask pdfminer.six sseclient requests openai python-dotenv
  
  `This is not necessary if using the provided Powershell script for Windows`


# Setup

• You will need an API key from OpenAI. Once you have it, create a .env file in the root directory and add the following line:

  • OPENAI_API_KEY=your_api_key_here
  
  `Replace your_api_key_here with your actual OpenAI API key.`
  
• Optionally, you can set an environment variable manually, as happens in the provided Powershell script for Windows


# Usage

• To run the application simply execute the provided Powershell script, or run the Python script with a command line interface:

  • python app.py
  
  • By default, the application will be hosted at http://localhost:5000.


# Routes

• GET / - Renders the index page.

• POST /query - Accepts form data with fields model_num (1 for GPT-3.5-turbo, 2 for GPT-4), user_query (the user's query), system_message (optional message to provide context), and pdf-upload (optional PDF to extract text from). Returns a JSON response with the field gpt_response containing the AI's response.


# Contributing

• Contributions are welcome! Please feel free to submit a pull request.


# License

• This project is licensed under the MIT License.
