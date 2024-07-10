#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

from dotenv import load_dotenv
load_dotenv()


openai.api_type = os.getenv("gpt-4o") #From Go to Azure AI Studio -> Playground then we can use the API into our application 
openai.api_base = os.getenv("https://lineaoai.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview") #From Go to Azure AI Studio -> Playground then we can use the API into our application 
openai.api_version = os.getenv("2024-05-13") #From Go to Azure AI Studio -> Playground then we can use the API into our application 
openai.api_key = os.getenv("2b66b4ac967246fba47d55e65f46ef9e") #From Go to Azure AI Studio -> Playground then we can use the API into our application 

completion_engine = os.getenv("OPENAI_COMPLETION_ENGINE")


def ask_azure_gpt(question):
    response = openai.Completion.create(
    engine=completion_engine,
    prompt=question,
    temperature=1,
    max_tokens=1000,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    return response["choices"][0]["text"].strip()
