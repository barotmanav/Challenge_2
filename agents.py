import json

class Agent:
    def __init__(self, name, llm, prompt_builder):
        self.name = name
        self.llm = llm
        self.prompt_builder = prompt_builder

    def run(self, **kwargs):
        prompt = self.prompt_builder(**kwargs)
        raw_output = self.llm.generate(prompt)

        cleaned_output = raw_output.strip()

        # Remove Markdown code fences if present
        if cleaned_output.startswith("```"):
            cleaned_output = cleaned_output.strip("`")
            if cleaned_output.startswith("json"):
                cleaned_output = cleaned_output[4:].strip()

        try:
            return json.loads(cleaned_output)
        except json.JSONDecodeError:
            raise ValueError(
                f"{self.name} returned invalid JSON:\n{raw_output}"
            )
