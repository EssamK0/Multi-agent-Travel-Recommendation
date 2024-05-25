from autogen import AssistantAgent, GroupChatManager, UserProxyAgent
from autogen.agentchat import GroupChat

config_list = [
    {
        "api_base": "http://localhost:1234/v1",
        "api_type": "open_ai",
        "api_key": "NULL",
    }
]

llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 600,
              "temperature": 0,}

admin = UserProxyAgent(
    name="admin",
    human_input_mode="NEVER",
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
                      Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
    llm_config=llm_config,
    code_execution_config=False,
)

Flights = AssistantAgent(
    name="Flights",
    llm_config=llm_config,
    system_message="Flights. Provide information and suggestions for the best flight options."""
)

Hotels = AssistantAgent(
    name="Hotels",
    llm_config=llm_config,
    system_message="""
    Hotels. Offer recommendations for suitable accommodations.".
""",
)

Attractions = AssistantAgent(
    name="Attractions",
    system_message="""
Attractions. Suggest local attractions and activities for the traveler.
""",
    llm_config=llm_config,
)

TravelPlanner = AssistantAgent(
    name="TravelPlanner",
    llm_config=llm_config,
    system_message="""TravelPlanner. Propose a travel plan considering inputs from Flights, Hotels, Attractions, and ensure it meets the traveler's preferences.
""",)


critic = AssistantAgent(
    name="critic",
    system_message="""critic. Thoroughly review the travel plan and offer feedback. Ensure the plan is well-balanced and addresses the traveler's needs.""",
    llm_config=llm_config,
)
groupchat = GroupChat(
    agents=[admin, Flights, Hotels, Attractions, TravelPlanner, critic],
    messages=[],
    max_round=500,
)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

admin.initiate_chat(
    manager,
    message=""" 
Plan a trip to a beautiful destination. Consider flight options, hotel accommodations, and local attractions.
""",
)