from langchain.tools import tool
import requests
import os

@tool
def linkedin_tool(query: str) -> dict:
    """
    Fetch LinkedIn posts or profiles using LinkedIn API
    """

    token = os.getenv("LINKEDIN_ACCESS_TOKEN")

    url = "https://api.linkedin.com/v2/search?q=people"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "LinkedIn API failed"}

    data = response.json()

    return {
        "query": query,
        "results": data
    }