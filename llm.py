import google.generativeai as genai
import time
import random
from google.api_core import exceptions

class LLM:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.total_tokens = 0

    def generate(self, prompt):
        retries = 0
        max_retries = 5
        base_delay = 2
        
        while True:
            try:
                if "gemini" in self.model:
                
                    model_instance = self.client.GenerativeModel(self.model)
                    response = model_instance.generate_content(prompt)
                    
                    if hasattr(response, "usage_metadata"):
                        self.total_tokens += response.usage_metadata.total_token_count
                    
                    return response.text
                else:
                    
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0
                    )

                    usage = response.usage
                    self.total_tokens += usage.total_tokens

                    return response.choices[0].message.content
                    
            except exceptions.ResourceExhausted as e:
                # Handle Rate Limit (429) specifically
                retries += 1
                if retries > max_retries:
                    raise e
                
                wait_time = (base_delay * (2 ** retries)) + random.uniform(0, 1)
                print(f"[LLM] Rate limit hit. Retrying in {wait_time:.2f}s...")
                time.sleep(wait_time)
                
            except Exception as e:
                # General retry for other transient errors
                if "429" in str(e): # Sometimes e is not explicit ResourceExhausted
                    retries += 1
                    if retries > max_retries:
                        raise e
                    
                    wait_time = (base_delay * (2 ** retries)) + random.uniform(0, 1)
                    print(f"[LLM] Connection error/Rate limit. Retrying in {wait_time:.2f}s...")
                    time.sleep(wait_time)
                else:
                    raise e
