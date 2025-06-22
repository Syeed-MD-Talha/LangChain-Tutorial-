!pip install -qU "langchain[google-genai]"

api_key="Your google api key"

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai",api_key=api_key)

model.invoke("What is the capital of Bangladesh?").content