# Multi-Agent System with LangGraph and MCP Adapters

This project demonstrates a multi-agent system built using `langgraph` for agentic orchestration and `langchain-mcp-adapters` for seamless communication with specialized microservices. It showcases how a Large Language Model (LLM) can leverage external tools to expand its capabilities.

`uv` was chosen for its significant speed and efficiency in Python package and dependency management compared to `conda` or standard virtual environments.

## Project Overview

The core idea is to have a central "smart brain" (an LLM) that can understand complex requests and delegate specific tasks to specialized "workers" (microservices). This allows the LLM to perform actions or access information beyond its inherent training data.

## Key Technologies Used

* **LangGraph**: A library for building robust and stateful agentic workflows.
* **Langchain-MCP-Adapters**: Facilitates communication between Langchain agents and Micro-service Communication Protocol (MCP) servers.
* **MCP (Micro-service Communication Protocol)**: A protocol for defining and interacting with microservices.
* **Langchain-Groq**: Integration with Groq's high-performance inference engine for LLMs (specifically `gemma2-9b-it`).
* **Python 3.13**: The primary programming language.

## Project Structure

* `main.py`: A simple entry point for the project.
* `client.py`: The main application where the LLM agent is initialized, tools are registered, and the agentic workflow is executed.
* `mathserver.py`: Defines an MCP server providing mathematical tools (addition, multiplication).
* `weather.py`: Defines another MCP server providing a simple weather tool.
* `pyproject.toml` & `requirements.txt`: Define project dependencies.
* `.env`: Used to store environment variables, such as the `GROQ_API_KEY`.
* `.python-version`: Specifies the Python version used by the project.
* `.gitignore`: Specifies files/folders to be ignored by Git.
* `uv.lock`: Dependency lock file.

## How it Works (Conceptual Steps)

1.  **Define Specialized Workers (Microservices)**:
    * `mathserver.py` and `weather.py` are set up as independent microservices using `FastMCP`. They expose specific functionalities (e.g., `add`, `get_weather`).
2.  **Central Intelligence (LLM Agent)**:
    * In `client.py`, a `langchain-groq` model is initialized to serve as the brain.
3.  **Tool Integration**:
    * The `MultiServerMCPClient` in `client.py` connects to the running `mathserver` and `weather` servers, making their exposed functionalities available as callable "tools" to the LLM agent.
4.  **Orchestration (LangGraph)**:
    * `langgraph` is used to define the agent's decision-making process. When a user asks a question, `langgraph` guides the LLM to:
        * Analyze the query.
        * Determine which specific tool (math or weather) is needed.
        * Invoke the tool via the `MCP` adapter.
        * Process the tool's output.
        * Formulate a final response.
5.  **Execution**:
    * The `client.py` script runs the agent, allowing it to process user inputs and dynamically use the math or weather tools as required.
