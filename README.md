# agentic-tasks

> 🚧 **Work in progress.** This project is under active development. The code is incomplete, APIs will change, and things may not run yet.

A small demonstration of how AI agents plan work: the agent breaks a goal into a **checklist of tasks** and then **updates that checklist through tool calls** as it completes each step, rendered live in the terminal.

## Idea

1. The agent receives a goal.
2. It calls `define_checklist` to lay out the tasks it plans to do.
3. As it finishes each task, it calls `update_checklist` to mark it done.
4. The terminal shows the checklist updating in real time (via [Rich](https://github.com/Textualize/rich)).

## Project layout

- `src/tools.py`: checklist state, the tool functions, and their JSON tool schemas
- `src/main.py`: live terminal rendering loop

## Status

- [x] Tool schemas for `define_checklist` and `update_checklist`
- [x] Live checklist rendering with Rich
- [ ] Wire up an LLM that calls the tools
- [ ] Agent loop that executes tasks and reports progress
- [ ] Runnable end-to-end demo

## Running

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv):

```bash
uv sync
uv run src/main.py
```

(The demo isn't runnable end-to-end yet. See Status above.)
