from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ...constants.constants import MODEL_GPT_4_1
from .prompts import INSTRUCTION

problem_critic_agent = Agent(
    name="problem_critic_agent",
    model=LiteLlm(MODEL_GPT_4_1),
    description="An agent that criticize the generated problem.",
    instruction=INSTRUCTION,
    output_key="problem_critic_output",
)