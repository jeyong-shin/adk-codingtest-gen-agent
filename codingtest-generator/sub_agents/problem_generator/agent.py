from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ...constants.constants import MODEL_GPT_4O
from .prompts import INSTRUCTION

problem_generator_agent = Agent(
    name="problem_generator_agent",
    model=LiteLlm(MODEL_GPT_4O),
    description="An agent that generates coding test problems.",
    instruction=INSTRUCTION,
    output_key="problem_generator_output",
)