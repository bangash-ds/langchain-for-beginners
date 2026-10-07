from langchain_groq import ChatGroq
from dotenv import load_dotenv
import time
load_dotenv()


def compare_models():
    print("compare AI models\n")

    prompt = "Explain recursion in programming in one sentence"
    models = ["openai/gpt-oss-120b", "openai/gpt-oss-20b", "qwen/qwen3.8-27b"]

    for model_name in models:
        print(f"Testing {model_name}")
        print("-" * 50)


        llm = ChatGroq(
            model=model_name,
            temperature=0
        )

    
        start_time = time.time()
        response = llm.invoke(prompt)
        duration = (time.time() - start_time) * 1000
        
        
        print(f"Response: {response.content}")
        print(f"Time:  {duration:.0f}ms")

    print("\n Comparison complete!")
    print("\n Key Observations:")
    print("   - openai/gpt-oss-120b and qwen/qwen3.8-27b are more capable and detailed")
    print("   - openai/gpt-oss-20b is faster and correct but missing a key idea")
    print("   - Choose based on your needs: speed vs. capability")
    


if __name__ == "__main__":
    compare_models()

