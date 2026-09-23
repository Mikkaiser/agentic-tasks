from rich.console import Console
from rich.live import Live

import time

console = Console()

with Live(console=console, auto_refresh=False) as live:
    for task in tasks_list:
        time.sleep(1)

        #execution of the task

        updated_checklist = update_checklist(completed_tasks, task)

        live.update(updated_checklist)
        live.refresh()


