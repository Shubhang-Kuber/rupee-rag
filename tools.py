from __future__ import annotations

from math import floor
from typing import List

import yfinance as yf
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


@tool
def search_tool(query: str) -> str:
    """Search the web using DuckDuckGo."""
    return DuckDuckGoSearchRun().run(query)


@tool
def get_stock_price(ticker: str) -> str:
    """
    Get the latest closing price for a stock.

    IMPORTANT: Because you are analyzing the Indian market, you MUST append
    '.NS' to NSE ticker symbols before calling this tool (e.g., RELIANCE ->
    RELIANCE.NS).
    """
    history = yf.Ticker(ticker).history(period="5d")
    if history.empty:
        return "INR 0.00"

    latest_close = history["Close"].dropna().iloc[-1]
    return f"INR {latest_close:.2f}"


@tool
def calculate_purchasing_power(budget: float, stock_price: float) -> int:
    """Return how many whole shares can be bought with the given budget."""
    if stock_price <= 0:
        return 0
    return int(floor(budget / stock_price))


my_tools: List = [search_tool, get_stock_price, calculate_purchasing_power]
