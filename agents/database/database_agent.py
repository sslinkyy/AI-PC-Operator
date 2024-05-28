import sqlite3
from agents.base_agent import NeuralNetworkAgent

class DatabaseAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("execute_query"):
            _, db_path, query = user_command.split(maxsplit=2)
            return self.execute_query(db_path, query)
        return self.respond(f"Unknown command: {user_command}")

    def execute_query(self, db_path, query):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            conn.close()
            return self.respond(f"Query executed successfully. Results: {results}")
        except Exception as e:
            return self.respond(f"Failed to execute query: {query}. Error: {str(e)}")
