from __future__ import annotations

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import my_tools


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert Indian financial researcher. Provide concise, "
            "well-reasoned answers and use tools when needed.",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_tool_calling_agent(llm, my_tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=my_tools, verbose=True)
