import openai
import os
from dotenv import load_dotenv
load_dotenv()

def getAboutMe(physical: str, ending: str):
    try:
        # Apply your OpenAI API Key
        openai.api_key = os.getenv("OPEN_AI_KEY")

        # Define the prompt
        prompt = f'Make a sentence out of this in natural language on more than 200 words {physical}. {ending} '

        # Generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    except Exception as e:
        print("Error Message:", e)
        return [None,str(e)]

    return [response["choices"][0]["text"],None]
