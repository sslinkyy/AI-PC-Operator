from typing_extensions import override
import re
from agents.base_agent import NeuralNetworkAgent
from agency_swarm.tools import FileSearch
from instructor import llm_validator

class TestingAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=1, supervisor=supervisor)
        self.supervisor = supervisor
        supervisor.add_subordinate(self)
        self._init_agent()

    def _init_agent(self):
        self.agent = Agent(
            name="TestingAgent",
            description="Agent responsible for testing and debugging other agents.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[FileSearch],
            tools_folder="./tools",
            validation_attempts=1,
            temperature=0,
            max_prompt_tokens=25000,
        )

    @override
    def response_validator(self, message):
        pattern = r'(```)((.*\n){5,})(```)'

        if re.search(pattern, message):
            # take only first 100 characters
            raise ValueError(
                "You returned a code snippet. Please never return code snippets to me. "
                "Use the FileWriter tool to write the code locally. Then, test it if possible. Continue."
            )

        llm_validator(
            statement="Verify whether the update from the AI Developer Agent confirms the task's "
                      "successful completion. If the task remains unfinished, provide guidance "
                      "within the 'reason' argument on the next steps the agent should take. For "
                      "instance, if the agent encountered an error, advise the inclusion of debug "
                      "statements for another attempt. Should the agent outline potential "
                      "solutions or further actions, direct the agent to execute those plans. "
                      "Message does not have to contain code snippets. Just confirmation.",
            client=self.agent.client
        )(message)

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
        methods = inspect.getmembers(agent, predicate=inspect.ismethod)
        for method_name, method in methods:
            if method_name.startswith("test_"):
                try:
                    result = method()
                    test_results.append(f"Method {method_name}: Passed")
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
