class TopLevelAgentWithErrorHandling(NeuralNetworkAgent):
    def __init__(self, name):
        super().__init__(name, level=1)
        self.error_handling_agent = ErrorHandlingAgent("ErrorHandler", self)

    def execute_task(self, user_command):
        try:
            if user_command.startswith("analyze_stock"):
                return self.address("StockAnalyst", user_command)
            elif user_command.startswith("make_trade"):
                return self.address("StockBroker", user_command)
            else:
                return f"TopLevelAgent received unknown command: {user_command}"
        except Exception as e:
            error_message = str(e)
            return self.address("ErrorHandler", f"handle_error: {error_message}")
