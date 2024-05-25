# About
This project adopts Autogen multi-agents, comprising 5 assistant agents alongside 1 user proxy agent. What sets our project apart is the deliberate choice not to utilize GPT. Instead, we employ open-source LLMs such as Llama and Zephyr, leveraging LM Studio to run these models locally. Our approach aligns with a Trip Advisor use case, assigning specific roles—such as Flights, Hotels, Attractions, and more—to each assistant, thereby ensuring specialized functionalities within the system.

## Requirement Specification
- Python Version: We are utilizing Python version 3.10 (64-bit)
- Pip Install:
- ```bash
  pip install pyautogen
- LM Studio: LM Studio is an easy-to-use desktop app for experimenting with local and open-source Large Language Models (LLMs).
- Download LM Studio
- 
## System Design
Configuration and Initialization
The system's architecture revolves around the following key components:

- Admin Agent: Manages interactions and ensures tasks are completed to satisfaction.
- Assistant Agents: Each agent specializes in a specific domain:
- Flights: Provides information and suggestions for flight options.
- Hotels: Recommends suitable accommodations.
- Attractions: Suggests local attractions and activities.
- TravelPlanner: Proposes comprehensive travel plans based on inputs from other agents.
- Critic: Reviews the travel plan to ensure it meets the traveler's needs.
- 
## Code Structure
- Import necessary modules from Autogen.
- Define the configuration for the LLMs including API base, type, and key.
- Set up the Admin agent with specific parameters to manage the overall interaction.
- Initialize each assistant agent (Flights, Hotels, Attractions, TravelPlanner, Critic) with their respective roles and system messages.
- Create a GroupChat to manage the communication between agents.
- Initiate the chat via the Admin agent to start the travel planning process.
- Usage
- Install Required Packages:
```bash
 pip install pyautogen
```
-Download and Setup LM Studio:
### Follow the instructions to download and set up LM Studio.

-Run the Script:
Execute the provided Python script to start the multi-agent travel recommendation system.

-Important Notes
-Ensure LM Studio is properly configured and running locally to enable communication with the open-source LLMs.
-The UserProxyAgent's human_input_mode is set to "NEVER" to automate responses based on predefined satisfaction criteria.
-The GroupChatManager orchestrates the interactions among the agents, ensuring a cohesive and well-rounded travel recommendation is generated.
-The system is designed to handle up to 500 interaction rounds to refine and finalize the travel plan.
-By leveraging specialized assistant agents and local LLMs, this system provides a robust framework for generating comprehensive and personalized travel recommendations.

