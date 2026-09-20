from prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from models import ollama_model
from agents import delegate_to_subagent1, delegate_to_subagent2
import logging
from langchain.messages import HumanMessage

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# asking user for their requirements for their wedding
logging.info("asking user for their requirements...")
user_requirements = input("Please enter your requirements and preferences for your wedding\n")

#updating the system prompt 
updated_system_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements)

#creating main agen
logging.info("initializing main wedding planner agent...")
main_wedding_planner_agent = create_agent(model=ollama_model,
                                          tools=[delegate_to_subagent1, delegate_to_subagent2],
                                          name="MainWeddingPlannerAgent",
                                          system_prompt=updated_system_prompt)

#invoke main agent
logging.info("invoking main wedding planner agent...")
main_wedding_planner_agent.invoke({"messages": [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})

# printing the response of the main agent
print("\nMain wedding planner agent's response: ")
print(main_wedding_planner_agent["message"][-1])