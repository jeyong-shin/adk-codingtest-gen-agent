from google.adk.agents import BaseAgent, LoopAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from typing import AsyncGenerator

from ..problem_generator.agent import problem_generator_agent
from ..problem_critic.agent import problem_critic_agent
from ..problem_quality_checker.agent import problem_quality_checker_agent


class CheckStatusAndEscalate(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        status = ctx.session.state.get("problem_quality_checker_output", "fail")
        should_stop = (status == "pass")
        yield Event(author=self.name, actions=EventActions(escalate=should_stop))


problem_loop_agent = LoopAgent(
    name="problem_loop_agent",
    description="A loop agent that generates coding problems.",
    max_iterations=5,
    sub_agents=[problem_generator_agent, problem_critic_agent, problem_quality_checker_agent, CheckStatusAndEscalate(name="stop_checker")],
)
