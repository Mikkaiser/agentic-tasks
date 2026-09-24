from dotenv import load_dotenv
from openai import OpenAI
from tools import tools, handle_tool_calls, tasks_list

load_dotenv()
openai = OpenAI()

history = []

def call_llm(user_prompt):
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
        "content": response_message.content
    })
    
    full_response = []

    if response_message.tool_calls:
        handle_tool_calls(response_message.tool_calls)
        full_response.append({"From tool: ": tasks_list})
    if response_message.content:
        full_response.append({"From message: ": response_message.content})
    
    return full_response