import google.generativeai as genai
from main import run_research
from llm import LLM


GOOGLE_API_KEY = "AIzaSyDTnzQ9utqb0nEZ8jWtnlL3b7QncB2hKiA"
genai.configure(api_key=GOOGLE_API_KEY)

def evaluate(task, mode_name):
    llm = LLM(client=genai, model="gemini-flash-latest")

    # NOTE: run_research internals (in main.py) create their OWN LLM instance. 
    # To truly evaluate with Gemini, main.py also needs to use this config,
    # or run_research needs to accept an llm instance.
    # For now, we update this file as requested.
    synthesis, decision = run_research(task)

    return {
        "mode": mode_name,
        "total_tokens": llm.total_tokens,
        "final_decision": decision
    }


def main():
    task = (
        "Survey methods for fake-news detection "
        "in low-resource languages"
    )

    compressed_result = evaluate(task, "compressed_context")

    print("\n=== EVALUATION RESULTS ===\n")
    print(f"Mode: {compressed_result['mode']}")
    print(f"Total Tokens Used: {compressed_result['total_tokens']}")
    print(f"Decision: {compressed_result['final_decision']}")


if __name__ == "__main__":
    main()
