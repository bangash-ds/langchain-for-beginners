from dotenv import load_dotenv
import os 
from langchain_groq import ChatGroq

load_dotenv()  # reads your .env file


# calling llm
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0

)

response = llm.invoke("Reply with exactly: Setup Successful!")
print(response.content)








