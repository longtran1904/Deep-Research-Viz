from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import requests
import json

def perform_research(topic: str) -> str:
        """
        Calls the deep-research API to initiate and retrieve research.
        You'll need to figure out the exact endpoint and payload.
        """
        base_url = "http://localhost:3333/api" # Adjust port if needed
        research_endpoint = f"{base_url}/research" # This is an educated guess, verify in repo
        payload = {"topic": topic} # Again, verify payload structure

        try:
                # Assuming a POST request to start research and get a report back
                response = requests.post(research_endpoint, json=payload, timeout=300) # Long timeout for research
                response.raise_for_status() # Raise an exception for HTTP errors

                # The response will depend on the deep-research API.
                # If it returns the full report directly:
                research_report = response.json().get("report", "") # Assuming JSON response with a 'report' key
                return research_report
        except requests.exceptions.Timeout:
                return "Error: Deep research request timed out."
        except requests.exceptions.RequestException as e:
                return f"Error calling deep research API: {e}"
        except json.JSONDecodeError:
                return "Error: Deep research API returned invalid JSON."
        
deep_research_tool = FunctionTool(
    func=perform_research,
    description="Performs deep research on a given topic using an external API.",
    input_schema={
        "topic": {"type": "string", "description": "The topic to research deeply."}
    }
)

root_agent = Agent(
    name="deep_research_agent",
    model="gemini-2.0-flash",
    description="Agent to perform deep research on a given topic.",
    instruction="You are a helpful agent who performs deep research on topics using external APIs.",
    tools=[deep_research_tool],
)