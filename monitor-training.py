from openai import OpenAI
import json
from dotenv import load_dotenv
import os
import asyncio
import time

# Load environment variables from .env file
load_dotenv()

async def monitor_job(client, job_id):
    while True:
        job = client.fine_tuning.jobs.retrieve(job_id)
        print(f"Status: {job.status}")
        if job.status in ['succeeded', 'failed']:
            break
        await asyncio.sleep(60)  # Check every minute

async def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Upload the training file
    with open("coffee_shop_finetune.jsonl", "rb") as file:
        training_file = client.files.create(
            file=file,
            purpose="fine-tune"
        )

    # Create fine-tuning job
    job = client.fine_tuning.jobs.create(
        training_file=training_file.id,
        model="gpt-4o-2024-08-06",
        method={
            "type": "dpo",
            "dpo": {
                "hyperparameters": {"beta": 0.1},
            },
        },
    )
    
    print(f"Job created with ID: {job.id}")
    await monitor_job(client, job.id)

if __name__ == "__main__":
    asyncio.run(main())