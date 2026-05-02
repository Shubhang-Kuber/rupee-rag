from __future__ import annotations

from agent import agent_executor
from langchain_core.messages import HumanMessage


def main() -> None:
    question = (
        "What is the current stock price of Tata Motors? Summarize their "
        "recent news, and tell me how many shares I can buy with 50,000 INR."
    )
    result = agent_executor.invoke({"messages": [HumanMessage(question)]})
    messages = result.get("messages", [])
    output = messages[-1].content if messages else result
    print("=== Agent Output ===")
    print(output)


if __name__ == "__main__":
    main()
