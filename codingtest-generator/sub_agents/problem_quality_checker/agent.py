from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ...constants.constants import MODEL_GPT_4_1
from .prompts import INSTRUCTION

problem_quality_checker_agent = Agent(
    name="problem_quality_checker_agent",
    model=LiteLlm(MODEL_GPT_4_1),
    description="An agent that checks the quality of a coding problem.",
    instruction=INSTRUCTION,
    output_key="problem_quality_checker_output",
)