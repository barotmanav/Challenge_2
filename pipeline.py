def run_pipeline(
    user_task,
    planner,
    researchers,
    synthesizer,
    coordinator
):
    """
    Runs the full multi-agent research workflow.
    """

    plan = planner.run(user_task=user_task)

    if "subtasks" not in plan or "success_criteria" not in plan:
        raise ValueError("Planner output is incomplete")

    research_results = []

    for subtask, agent in zip(plan["subtasks"], researchers):
        result = agent.run(
            subtask_description=subtask["description"],
            expected_output=subtask["expected_output"]
        )
        research_results.append(result)

    synthesis = synthesizer.run(
        research_summaries=research_results
    )

    decision = coordinator.run(
        synthesis=synthesis,
        success_criteria=plan["success_criteria"]
    )

    return synthesis, decision
