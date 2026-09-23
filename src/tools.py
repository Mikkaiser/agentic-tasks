from rich.text import Text

text = Text()

tasks_list = ["task 1", "task 2", "task 3", "task 4", "task 5", "task 6", "task 7"]
completed_tasks = []


def define_checklist(tasks):
    tasks_list += tasks
    return tasks_list

def update_checklist(recent_task):
    completed_tasks.append(recent_task)
    text = Text()
    for task in tasks_list:
        if task in completed_tasks:
            text.append(task + "\n", style="strike")
        else:
            text.append(task + "\n", style="bold green")

    return text


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