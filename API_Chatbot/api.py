from google.generativeai import configure, GenerativeModel

# Configure with your API key
configure(api_key="AIzaSyAsskJ6QKtwVlTVw3Von1IWMkGuzzCVw4k")

# Initialize the model
model = GenerativeModel('gemini-1.5-flash')

# Use generate_content correctly
response = model.generate_content("What is the capital of France?")

# Print the result
print(response.text)
