from dotenv import load_dotenv
from openai import OpenAI
from tools import tools, handle_tool_calls, update_user_interface

load_dotenv()
openai = OpenAI()

history = [
    {
        "role": "system",
        "content": (
            "You are a task-executing agent. For any multi-step user request, first call "
            "define_checklist with the list of tasks you will perform. Then, before moving on "
            "to each task, briefly tell the user what you're doing (e.g. 'Done with task 2, "
            "moving to task 3'), and once a task is finished call update_checklist with its "
            "index. Continue until every task is marked done."
        )
    }
]


def call_llm(user_prompt = None):
    if user_prompt:
        history.append({
            "role":"user",
            "content": user_prompt
        })

    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=history,
        tools=tools
    )

    response_message = response.choices[0].message
    history.append({
        "role":response_message.role,
        "content": response_message.content,
        "tool_calls": response_message.tool_calls
    })


    if response_message.content:
        update_user_interface(response_message.content)

    if response_message.tool_calls:
        tool_results = handle_tool_calls(response_message.tool_calls)

        for result in tool_results:
            history.append({
                "role": "tool",
                "tool_call_id": result["tool_call_id"],
                "content": str(result["content"])
            })

        call_llm()