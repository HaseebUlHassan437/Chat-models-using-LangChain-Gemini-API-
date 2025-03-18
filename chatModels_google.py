# Import the ChatGoogleGenerativeAI class for interacting with Google's Gemini models
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the load_dotenv function to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize the Google Generative AI model using Gemini-1.5-Pro
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Invoke the model with a query asking for the most popular political leader of Pakistan
result = model.invoke('most popular political Leader of Pakistan')

# Print the content of the response from the AI model
print(result.content)
