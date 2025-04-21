from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import agent_tool

from .prompts import INSTRUCTION
from .constants.constants import MODEL_GEMINI_2_5_FLASH

from .sub_agents.topic_finder.agent import topic_finder_agent
from .sub_agents.problem_loop.agent import problem_loop_agent
from .sub_agents.problem_solver.agent import problem_solver_agent
from .sub_agents.test_case_generator.agent import test_case_generator_agent


agent_search = Agent(
    name="google_search_agent",
    model=MODEL_GEMINI_2_5_FLASH,
    description="An agent that performs Google searches.",
    instruction="Perform a Google search.",
    tools=[google_search]
)


root_agent = Agent(
    name="codingtest_generator_agent",
    model=MODEL_GEMINI_2_5_FLASH,
    description="An agent that generates coding tests for software engineers.",
    instruction=INSTRUCTION,
    tools=[agent_tool.AgentTool(agent=agent_search)],
    sub_agents=[topic_finder_agent, problem_loop_agent, problem_solver_agent,test_case_generator_agent],
    output_key="codingtest_generator_output",
)