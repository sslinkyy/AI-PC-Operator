# AI-PC-Operator
AI PC Operator with stock analysis capabilities
# Hierarchical Agent System with Error Handling

This project implements a hierarchical agent system designed for stock analysis and trading, equipped with advanced error handling capabilities. The system uses a neural network-based architecture for persistent learning and integrates various agents to perform specific tasks. Over time, the system aims to reduce its dependence on the OpenAI API by storing knowledge persistently and learning from previous tasks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Detailed Description](#detailed-description)
  - [Agent](#agent)
  - [NeuralNetworkAgent](#neuralnetworkagent)
  - [StockAnalyst](#stockanalyst)
  - [StockBroker](#stockbroker)
  - [ErrorHandlingAgent](#errorhandlingagent)
  - [TopLevelAgentWithErrorHandling](#toplevelagentwitherrorhandling)
  - [TaskManagerWithErrorHandling](#taskmanagerwitherrorhandling)
- [Error Handling](#error-handling)
- [Reducing Dependence on OpenAI API](#reducing-dependence-on-openai-api)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Features

- **Hierarchical Structure**: The system is composed of multiple agents, each responsible for specific tasks.
  - **TopLevelAgent**: Oversees the entire system and delegates tasks to subordinate agents.
  - **StockAnalyst**: Analyzes stock data, market sentiment, and news.
  - **StockBroker**: Makes trade decisions based on analysis provided by the StockAnalyst.
  - **ErrorHandlingAgent**: Identifies, logs, and resolves errors autonomously.

- **Persistent Learning**: Agents save and load knowledge to/from disk, allowing them to learn and improve over time.

- **Advanced Error Handling**: The ErrorHandlingAgent provides robust error resolution strategies for network, file, and API issues.

- **Reducing Dependence on OpenAI API**: The system aims to minimize its reliance on the OpenAI API by persistently storing learned knowledge and using it to handle future tasks.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/sslinkyy/AI-PC-Operator.git
   cd hierarchical-agent-system
Create a Virtual Environment and Activate it

sh
Copy code
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the Required Packages

sh
Copy code
pip install -r requirements.txt
Requirements
Python 3.7+
PyTorch
Transformers
yfinance
requests
BeautifulSoup4
textblob
pickle
logging
Usage
Running the System
To run the system and test its functionalities:

sh
Copy code
python main.py
Example Usage
python
Copy code
if __name__ == "__main__":
    task_manager = TaskManagerWithErrorHandling()
    task_manager.execute_task("analyze_stock AAPL")
    task_manager.execute_task("make_trade AAPL")
    
    # Simulating an error scenario
    try:
        task_manager.execute_task("unknown_command")
    except Exception as e:
        task_manager.execute_task(f"handle_error: {str(e)}")
Project Structure
main.py: Entry point of the system.
agent.py: Base agent classes and neural network agent implementations.
stock_analyst.py: StockAnalyst agent implementation.
stock_broker.py: StockBroker agent implementation.
error_handling_agent.py: ErrorHandlingAgent implementation.
task_manager.py: TaskManager class to oversee and execute tasks.
Detailed Description
Agent
The base class for all agents. It includes methods for managing knowledge persistence, executing tasks, and interacting with other agents.

NeuralNetworkAgent
A subclass of Agent that includes methods for loading, saving, training, and using neural network models.

StockAnalyst
Analyzes stock data, market sentiment, and news headlines.

get_stock_data: Retrieves historical stock data using yfinance.
get_market_sentiment: Analyzes market sentiment from news headlines using TextBlob.
get_news_analysis: Retrieves recent news headlines related to a stock symbol.
StockBroker
Makes trade decisions based on the analysis provided by the StockAnalyst.

make_trade: Decides whether to buy, sell, or hold a stock.
decide_trade: Makes a trade decision based on sentiment and stock data.
calculate_position_size: Determines the position size for a trade based on portfolio value and stock volatility.
set_stop_loss: Sets a stop loss price.
set_take_profit: Sets a take profit price.
get_portfolio_value: Retrieves the current portfolio value.
calculate_moving_average: Calculates the moving average of stock prices.
calculate_volatility: Calculates the volatility of stock prices.
ErrorHandlingAgent
Identifies, logs, and resolves errors autonomously.

handle_error: Logs the error and attempts to resolve it.
resolve_network_issue: Attempts to resolve network connectivity issues.
resolve_file_issue: Attempts to resolve file-related issues.
resolve_api_issue: Attempts to resolve API-related issues.
default_resolution: Applies a default resolution for unspecified issues.
TopLevelAgentWithErrorHandling
Oversees the entire system and delegates tasks to subordinate agents. It integrates the ErrorHandlingAgent for robust error handling.

TaskManagerWithErrorHandling
Oversees task execution and error handling. It coordinates between the TopLevelAgentWithErrorHandling, StockAnalyst, StockBroker, and ErrorHandlingAgent.

Error Handling
The ErrorHandlingAgent provides comprehensive strategies to resolve common issues:

Network Issues: Verifies internet connectivity by attempting to reach Google.
File Issues: Checks file existence, read/write permissions, and handles permission errors.
API Issues: Verifies API health by making health check requests.
Default Resolution: Logs and applies a default resolution for unspecified issues.
Reducing Dependence on OpenAI API
The system is designed to gradually reduce its reliance on the OpenAI API by learning from tasks and storing knowledge persistently. When an agent encounters a new task, it first checks its knowledge base. If the task is not found, it queries the OpenAI API and stores the response. Over time, as the knowledge base grows, the system becomes more self-sufficient, relying less on external API calls.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
PyTorch
Hugging Face Transformers
yfinance
BeautifulSoup
TextBlob
Contact
For any questions or issues, please contact support@imobracingonline.com.
