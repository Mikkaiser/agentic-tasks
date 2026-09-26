import json
from rich.console import Console
from rich.text import Text

console = Console()

tasks_list = []

_live = None


def set_live(live_instance):
    global _live
    _live = live_instance


def define_checklist(tasks):
    global tasks_list
    tasks_list += tasks
    return tasks_list

def update_checklist(recent_task_index):
    tasks_list[recent_task_index] += " - DONE";
    return tasks_list


def update_user_interface(message, update=False):
    if(update and _live is not None):
        _live.update(message)
        _live.refresh()
        return

    _live.console.print(message)
    


def handle_tool_calls(tool_calls):
  results = []
  for tool_call in tool_calls:
        args = tool_call.function.arguments
        json_parsing=json.loads(args)

        if tool_call.function.name == "define_checklist":
          output = define_checklist(json_parsing["tasks"])
        if tool_call.function.name == "update_checklist":
          output = update_checklist(json_parsing["recent_task"])

          rendered = Text()
          for line in output:
              style = "green strike" if line.endswith(" - DONE") else "white"
              rendered.append(line + "\n", style=style)
          update_user_interface(rendered, True)

        results.append({
          "tool_call_id": tool_call.id,
          "content": output
        })

  return results

DEFINE_CHECKLIST_TOOL_JSON = {
    "type": "function",
    "function": {
      "name": "define_checklist",
      "description": "Defines the list of tasks for the execution of the full task.",
      "parameters": {
        "type": "object",
        "properties": {
          "tasks": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of task names to add to the checklist."
          }
        },
        "required": ["tasks"]
      }
    }
  }

UPDATE_CHECKLIST_TOOL_JSON = {
    "type": "function",
    "function": {
      "name": "update_checklist",
      "description": "Marks a task as completed in the checklist and returns the updated list with completed items marked as DONE. Proceed to the next task until all are finished.",
      "parameters": {
        "type": "object",
        "properties": {
          "recent_task": {
            "type": "integer",
            "description": "The task index that was just completed. Just the index within the list."
          }
        },
        "required": ["recent_task"]
      }
    }
  }

tools = [
  DEFINE_CHECKLIST_TOOL_JSON,
  UPDATE_CHECKLIST_TOOL_JSON
]
