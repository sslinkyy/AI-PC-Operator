import docx
from agents.base_agent import NeuralNetworkAgent

class DocumentAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("read_document"):
            _, document_path = user_command.split(maxsplit=1)
            return self.read_document(document_path)
        return self.respond(f"Unknown command: {user_command}")

    def read_document(self, document_path):
        try:
            doc = docx.Document(document_path)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            return self.respond(f"Read document: {document_path}. Content: {' '.join(full_text)}")
        except Exception as e:
            return self.respond(f"Failed to read document: {document_path}. Error: {str(e)}")
