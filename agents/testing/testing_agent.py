from typing_extensions import override
import re
import inspect
from agents.base_agent import NeuralNetworkAgent

class TestingAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=1, supervisor=supervisor)
        self.supervisor = supervisor
        supervisor.add_subordinate(self)

    @override
    def response_validator(self, message):
        pattern = r'(```)((.*\n){5,})(```)'

        if re.search(pattern, message):
            raise ValueError(
                "You returned a code snippet. Please never return code snippets to me. "
                "Use the FileWriter tool to write the code locally. Then, test it if possible. Continue."
            )

        # Add your own validation logic here if needed
        return message

    def execute_task(self, user_command):
        if user_command == "run_tests":
            return self.run_all_tests()
        elif user_command.startswith("test_agent"):
            _, agent_name = user_command.split(maxsplit=1)
            return self.test_agent(agent_name)
        return self.respond(f"Unknown command: {user_command}")

    def run_all_tests(self):
        results = []
        for agent in self.supervisor.agents:
            result = self.test_agent(agent.name)
            results.append(result)
        return self.respond(f"Test results: {results}")

    def test_agent(self, agent_name):
        agent = next((agent for agent in self.supervisor.agents if agent.name == agent_name), None)
        if not agent:
            return self.respond(f"Agent {agent_name} not found.")

        test_results = []
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for method_name, method in methods:
            if method_name.startswith(f"test_{agent_name.lower()}"):
                try:
                    result = method(agent)
                    test_results.append(result)
                except Exception as e:
                    test_results.append(f"Method {method_name}: Failed - {str(e)}")
        return self.respond(f"Test results for {agent_name}: {test_results}")

    def test_application_agent(self, agent):
        try:
            response = agent.execute_task("open_application calculator")
            assert "Opened application" in response, "open_application failed"
            return "ApplicationAgent: Passed"
        except AssertionError as e:
            return f"ApplicationAgent: Failed - {str(e)}"

    def test_audio_agent(self, agent):
        try:
            response = agent.execute_task("process_audio sample.wav")
            assert "Processed audio" in response, "process_audio failed"
            return "AudioAgent: Passed"
        except AssertionError as e:
            return f"AudioAgent: Failed - {str(e)}"

    def test_backup_restore_agent(self, agent):
        try:
            response = agent.execute_task("backup /source /backup")
            assert "Backup from /source to /backup completed successfully." in response, "backup failed"
            response = agent.execute_task("restore /backup /source")
            assert "Restore from /backup to /source completed successfully." in response, "restore failed"
            return "BackupRestoreAgent: Passed"
        except AssertionError as e:
            return f"BackupRestoreAgent: Failed - {str(e)}"

    # Add more specific tests for each agent's functionality...
