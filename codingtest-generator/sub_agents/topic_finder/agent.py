from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ...constants.constants import MODEL_GPT_4O
from .prompts import INSTRUCTION

topic_finder_agent = Agent(
    name="topic_finder_agent",
    model=LiteLlm(MODEL_GPT_4O),
    description="An agent that generates coding test topics.",
    instruction=INSTRUCTION,
    output_key="topic_finder_output",
)