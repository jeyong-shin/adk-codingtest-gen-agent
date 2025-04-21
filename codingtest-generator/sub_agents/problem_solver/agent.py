from google.adk.agents import Agent
from ...constants.constants import MODEL_GEMINI_2_5_PRO
from .prompts import INSTRUCTION

problem_solver_agent = Agent(
    name="problem_solver_agent",
    model=MODEL_GEMINI_2_5_PRO,
    description="An agent that solves coding test problems with java, javascript, and python.",
    instruction=INSTRUCTION,
    output_key="problem_solver_output",
)