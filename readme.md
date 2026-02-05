🧠 Collaborative Multi-Agent Research System
Token-Efficient AI Collaboration via Compressed Context Sharing
📌 Overview

This project implements a collaborative research system composed of multiple AI agents that coordinate on complex research tasks while minimizing token usage.

Instead of sharing full conversation histories between agents, the system uses compressed, structured context (JSON summaries) to reduce cost, latency, and context explosion — without sacrificing output quality.

The design mirrors how human research teams collaborate:
clear roles, concise reporting, and explicit uncertainty.

🎯 Problem Statement

Multi-agent LLM systems often suffer from:

Exponentially growing context windows

High token costs

Redundant information sharing

Reduced reliability due to uncontrolled memory


The uniqueness of our project is how we handle context. Instead of letting multiple agents share full conversation histories, we restrict communication to compressed, structured summaries. This mirrors how human research teams actually work and allows us to significantly reduce token usage while preserving key findings, limitations, and open questions. We also measure this efficiency rather than just claiming it



Goal:
Design a system where agents collaborate effectively without sharing raw dialogue or chain-of-thought, while preserving research quality.

✅ Key Contributions

🧩 Role-based agent architecture (Planner, Researcher, Synthesizer, Coordinator)

📦 Compressed context sharing using strict JSON schemas

🔒 Explicit separation between internal reasoning and user-facing output

📉 Token usage evaluation to quantify efficiency gains

🖥️ Desktop dashboard for human interaction (optional UI layer)

🏗️ System Architecture
User Task
   ↓
Planner Agent
   ↓
Research Agents (parallel, isolated)
   ↓
Synthesizer Agent
   ↓
Coordinator Agent
   ↓
Final Answer Renderer
   ↓
User

Important Design Principle

Agents never see full conversations.
They only receive compressed summaries relevant to their role.

🧠 Agent Roles
1. PlannerAgent

Decomposes the research objective

Produces independent, non-overlapping subtasks

2. ResearchAgent(s)

Execute exactly one subtask

Report only findings, evidence, and limitations

No speculation or verbosity

3. SynthesizerAgent

Merges research outputs

Identifies agreements, conflicts, and open questions

4. CoordinatorAgent

Decides whether research is complete

Recommends next actions if needed

5. Final Answer Renderer

Converts internal JSON into a human-readable research summary

Hides internal agent mechanics from the user

📂 Project Structure
collaborative_agents/
│
├── llm.py          # LLM interface + token tracking
├── prompts.py      # All agent prompts (centralized)
├── agents.py       # Generic agent execution logic
├── pipeline.py     # Multi-agent orchestration
├── main.py         # Programmatic entry point
├── desktop.py      # Desktop UI (Tkinter)
└── eval.py         # Token & quality evaluation

🔍 Compressed Context Strategy
❌ Naive Approach

Agents share full outputs

Context grows linearly

Token usage explodes

✅ This System

Agents share only structured summaries

No raw chain-of-thought

No redundant context

Deterministic information flow

Example internal message:

{
  "key_findings": ["Transformer models dominate recent work"],
  "limitations": ["Low-resource languages underrepresented"],
  "confidence_level": "medium"
}

📊 Evaluation Methodology
Metrics Used
1. Token Usage

Total tokens consumed during task execution

Measured directly via LLM API usage stats

2. Output Quality (Human-Aligned)

Core findings preserved

Limitations explicitly stated

Open questions retained

No hallucinated conclusions

Why Not BLEU / ROUGE?

These metrics do not reflect research usefulness.
Human-aligned evaluation better matches real-world expectations.

🧪 Example Evaluation Claim

Compressed context sharing significantly reduces token usage
while preserving research conclusions and uncertainty awareness.

🖥️ Desktop Dashboard (Optional)

A lightweight Tkinter UI allows users to:

Enter a research task

Run the multi-agent system

View the final research summary

Inspect the system’s decision (stop / continue)

The UI is a thin interaction layer and does not modify AI logic.

🚫 What This System Does NOT Do

❌ No autonomous self-looping

❌ No hidden memory

❌ No chain-of-thought exposure

❌ No personality simulation

❌ No framework dependency (AutoGPT / LangChain)

This is an engineering system, not a demo.

🧠 Design Philosophy

Intelligence is not in the model alone —
it emerges from constraints, structure, and coordination.

The LLM is treated as a service, not an agent with autonomy.

🏁 Conclusion

This project demonstrates how multi-agent LLM systems can scale responsibly by:

Reducing cost

Improving clarity

Preserving research rigor

Remaining interpretable and testable

It reflects real-world AI system design, not prompt-driven theatrics.

📌 Usage
python main.py


or  for UI Interface 

python desktop.py