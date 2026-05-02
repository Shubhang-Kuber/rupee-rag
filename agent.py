from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import my_tools


load_dotenv()

model_name = os.getenv("GOOGLE_MODEL", "gemini-flash-latest")
llm = ChatGoogleGenerativeAI(model=model_name)

agent_executor = create_agent(
    model=llm,
    tools=my_tools,
    system_prompt=(
        "You are an expert Indian financial researcher. Provide concise, "
        "well-reasoned answers and use tools when needed."
    ),
    debug=True,
)
