# Hide output from commands
$VerbosePreference = 'SilentlyContinue'

# Install required packages
pip install Flask
pip install pdfminer.six
pip install python-dotenv
pip install sseclient

# Set environment variable
$env:OPENAI_API_KEY = "API_KEY_HERE"

# Run the Python script
python app.py

# Wait for user input to close the script
Write-Host "Press any key to continue ..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
