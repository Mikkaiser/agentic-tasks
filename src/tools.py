from rich.text import Text
import json


text = Text()

tasks_list = []
completed_tasks = []


def define_checklist(tasks):
    global tasks_list
    tasks_list += tasks

def update_checklist(recent_task):
    completed_tasks.append(recent_task)
    text = Text()
    for task in tasks_list:
        if task in completed_tasks:
            text.append(task + "\n", style="strike")
        else:
            text.append(task + "\n", style="bold green")

    return text


def handle_tool_calls(tool_calls):
  for tool_call in tool_calls:
            args = tool_call.function.arguments
            json_parsing=json.loads(args)
            define_checklist(json_parsing["tasks"])


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
      "description": "Marks a task as completed in the checklist and returns the updated styled text.",
      "parameters": {
        "type": "object",
        "properties": {
          "recent_task": {
            "type": "string",
            "description": "The task name that was just completed."
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