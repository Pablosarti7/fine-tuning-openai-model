from openai import OpenAI
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the client with API key from environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Upload the training file
with open("coffee_shop_finetune.jsonl", "rb") as file:
    training_file = client.files.create(
        file=file,
        purpose="fine-tune"
    )


job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model="gpt-4o-mini-2024-07-18"
)

