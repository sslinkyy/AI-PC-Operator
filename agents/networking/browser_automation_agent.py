from selenium import webdriver
from selenium.webdriver.common.by import By
from agents.base_agent import NeuralNetworkAgent

class BrowserAutomationAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        self.driver = webdriver.Chrome()
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("navigate_to"):
            _, url = user_command.split(maxsplit=1)
            return self.navigate_to(url)
        elif user_command.startswith("find_element"):
            _, selector = user_command.split(maxsplit=1)
            return self.find_element(selector)
        return self.respond(f"Unknown command: {user_command}")

    def navigate_to(self, url):
        try:
            self.driver.get(url)
            return self.respond(f"Navigated to {url}")
        except Exception as e:
            return self.respond(f"Failed to navigate to {url}. Error: {str(e)}")

    def find_element(self, selector):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            return self.respond(f"Found element: {element.text}")
        except Exception as e:
            return self.respond(f"Failed to find element {selector}. Error: {str(e)}")
