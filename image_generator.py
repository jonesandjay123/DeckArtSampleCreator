import os
from dotenv import load_dotenv
import openai

def setup_openai_client():
    # Load environment variables from .env file
    load_dotenv()
    # Retrieve the API key from the environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    # Set up the OpenAI client with your API key
    openai.api_key = api_key

def generate_image(prompt):
    # Example call to the OpenAI API (details might need to be adjusted)
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.images[0]
