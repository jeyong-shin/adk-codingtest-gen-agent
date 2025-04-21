from google.adk.agents import Agent
from ...constants.constants import MODEL_GEMINI_2_5_PRO
from .prompts import INSTRUCTION

test_case_generator_agent = Agent(
    name="test_case_generator_agent",
    model=MODEL_GEMINI_2_5_PRO,
    description="An agent that generates python code that generates coding test cases.",
    instruction=INSTRUCTION,
    output_key="test_case_generator_output",
)