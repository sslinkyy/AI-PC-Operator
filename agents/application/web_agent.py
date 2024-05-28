from agents.base_agent import NeuralNetworkAgent

class WebAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("create_web"):
            _, project_details = user_command.split(maxsplit=1)
            return self.create_web_project(project_details)
        return self.respond(f"Unknown command: {user_command}")

    def create_web_project(self, project_details):
        try:
            # Create a simple HTML file with provided project details
            html_content = f"<html><body><h1>{project_details}</h1></body></html>"
            with open("index.html", "w") as file:
                file.write(html_content)
            return self.respond(f"Created web project with details: {project_details}")
        except Exception as e:
            return self.respond(f"Failed to create web project. Error: {str(e)}")
