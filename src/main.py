from rich.console import Console
from rich.live import Live
from api import call_llm
import json
console = Console()


# with Live(console=console, auto_refresh=False) as live:
while True:
    user_prompt = input("User: ")
    response = call_llm(user_prompt)
    console.print(json.dumps(response, indent=2))
        


