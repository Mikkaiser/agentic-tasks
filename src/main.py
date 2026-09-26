from rich.console import Console
from rich.live import Live
from api import call_llm
import tools

console = Console()

with Live(console=console, auto_refresh=False) as live:
    tools.set_live(live)

    while True:
        user_prompt = input("User: ")
        call_llm(user_prompt)


