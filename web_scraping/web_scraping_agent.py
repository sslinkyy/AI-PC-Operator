import requests
from bs4 import BeautifulSoup
from agents.base_agent import NeuralNetworkAgent

class WebScrapingAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("scrape_web"):
            _, url, element = user_command.split(maxsplit=2)
            return self.scrape_web(url, element)
        return self.respond(f"Unknown command: {user_command}")

    def scrape_web(self, url, element):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            result = soup.select(element)
            return self.respond(f"Scraped data: {[r.text for r in result]}")
        except Exception as e:
            return self.respond(f"Failed to scrape data from {url}. Error: {str(e)}")
