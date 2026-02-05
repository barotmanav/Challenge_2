from llm import LLM
from agents import Agent
from pipeline import run_pipeline
from prompts import (
    planner_prompt,
    research_prompt,
    synthesizer_prompt,
    coordinator_prompt,
    final_answer_prompt
)

import google.generativeai as genai

# Configure Google Gemini (Centralized)
GOOGLE_API_KEY = "AIzaSyDTnzQ9utqb0nEZ8jWtnlL3b7QncB2hKiA"
genai.configure(api_key=GOOGLE_API_KEY)

def build_llm():
    """
    Creates and returns a single LLM instance.
    """
    return LLM(
        client=genai, 
        model="gemini-flash-latest"
    )


def build_agents(llm):
    """
    Initializes all agents with their respective prompts.
    """

    planner = Agent(
        name="PlannerAgent",
        llm=llm,
        prompt_builder=planner_prompt
    )

    researchers = [
        Agent(
            name="ResearchAgent-1",
            llm=llm,
            prompt_builder=research_prompt
        ),
        Agent(
            name="ResearchAgent-2",
            llm=llm,
            prompt_builder=research_prompt
        )
    ]

    synthesizer = Agent(
        name="SynthesizerAgent",
        llm=llm,
        prompt_builder=synthesizer_prompt
    )

    coordinator = Agent(
        name="CoordinatorAgent",
        llm=llm,
        prompt_builder=coordinator_prompt
    )

    return planner, researchers, synthesizer, coordinator



def run_research(task: str):
    """
    Runs the full research pipeline for a given task.
    Returns:
        synthesis (dict)
        decision (dict)
    """

    llm = build_llm()
    planner, researchers, synthesizer, coordinator = build_agents(llm)

    synthesis, decision = run_pipeline(
        user_task=task,
        planner=planner,
        researchers=researchers,
        synthesizer=synthesizer,
        coordinator=coordinator
    )

    return synthesis, decision



def render_final_output(synthesis: dict) -> str:
    """
    Converts internal JSON synthesis into user-readable text.
    """

    llm = build_llm()
    prompt = final_answer_prompt(synthesis)
    return llm.generate(prompt)


def main():
    task = (
        "Survey methods for fake-news detection "
        "in low-resource languages"
    )

    synthesis, decision = run_research(task)
    final_output = render_final_output(synthesis)

    print("\n===== FINAL RESEARCH SUMMARY =====\n")
    print(final_output)

    print("\n===== SYSTEM DECISION =====\n")
    print(decision)


if __name__ == "__main__":
    main()
