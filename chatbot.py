import google.generativeai as genai

# Set your actual API key here
API_KEY = "AIzaSyDe8ZihcIwN5p-CoswCCUCbE4TgpdCzS1s"

# Configure the API key for generative AI
genai.configure(api_key=API_KEY)  # Pass the API key as a string, not a list

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

def getresponseFrommodel(user_input):
    # Generate content using the provided user input
    response = model.generate_content(user_input)  # Use the variable, not the string literal
    return response.text  # Ensure that the response is accessed correctly

# Get input from the user
user_input = input("Enter your prompt=")

# Generate the output from the model
output = getresponseFrommodel(user_input)

# Print the output
print(output)
