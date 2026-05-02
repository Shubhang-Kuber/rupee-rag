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
        "well-reasoned answers and use tools when needed. Format every response "
        "with clear section headings and bullet points. Use this structure:\n"
        "1) Price Summary: bullet list\n"
        "2) Recent News: bullet list with dates if available\n"
        "3) Purchasing Power: bullet list with calculation\n"
        "4) Notes: bullet list for caveats."
    ),
    debug=False,
)
