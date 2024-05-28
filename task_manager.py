class TaskManagerWithErrorHandling:
    def __init__(self):
        self.top_agent = TopLevelAgentWithErrorHandling("TopLevel")
        self.stock_analyst = StockAnalyst("StockAnalyst", self.top_agent)
        self.stock_broker = StockBroker("StockBroker", self.top_agent)
        self.error_handler = self.top_agent.error_handling_agent

    def execute_task(self, user_command):
        response = self.top_agent.execute_task(user_command)
        print(response)
