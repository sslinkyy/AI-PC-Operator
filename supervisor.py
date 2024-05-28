from agents.application.application_agent import ApplicationAgent
from agents.application.web_agent import WebAgent
from agents.audio.audio_agent import AudioAgent
from agents.audio.voice_control_agent import VoiceControlAgent
from agents.communication.email_agent import EmailAgent
from agents.communication.notification_agent import NotificationAgent
from agents.file_management.file_management_agent import FileManagementAgent
from agents.file_management.document_agent import DocumentAgent
from agents.file_management.backup_agent import BackupAgent
from agents.file_management.clipboard_agent import ClipboardAgent
from agents.file_management.checksum_agent import ChecksumAgent
from agents.monitoring.system_monitoring_agent import SystemMonitoringAgent
from agents.monitoring.power_management_agent import PowerManagementAgent
from agents.monitoring.system_information_agent import SystemInformationAgent
from agents.monitoring.security_agent import SecurityAgent
from agents.multimedia.graphics_agent import GraphicsAgent
from agents.multimedia.video_agent import VideoAgent
from agents.multimedia.screen_capture_agent import ScreenCaptureAgent
from agents.networking.network_agent import NetworkAgent
from agents.networking.browser_automation_agent import BrowserAutomationAgent
from agents.os_management.operating_system_agent import OperatingSystemAgent
from agents.os_management.update_agent import UpdateAgent
from agents.scheduler.scheduler_agent import SchedulerAgent
from agents.scheduler.automation_agent import AutomationAgent
from agents.ai.ai_model_training_agent import AIModelTrainingAgent
from agents.ai.natural_language_agent import NaturalLanguageAgent
from agents.ai.tensor_core_agent import TensorCoreAgent
from agents.database.database_agent import DatabaseAgent
from agents.utility.input_agent import InputAgent
from agents.utility.priority_agent import PriorityAgent
from agents.utility.math_agent import MathAgent
from agents.utility.speech_synthesis_agent import SpeechSynthesisAgent
from agents.ui.ui_agent import UIAgent
from agents.file_transfer.file_transfer_agent import FileTransferAgent
from agents.log_management.log_management_agent import LogManagementAgent
from agents.data_visualization.data_visualization_agent import DataVisualizationAgent
from agents.personal_assistant.personal_assistant_agent import PersonalAssistantAgent
from agents.backup_restore.backup_restore_agent import BackupRestoreAgent
from agents.email_client.email_client_agent import EmailClientAgent
from agents.data_processing.data_processing_agent import DataProcessingAgent
from agents.web_scraping.web_scraping_agent import WebScrapingAgent
from agents.virtual_assistant.virtual_assistant_agent import VirtualAssistantAgent
from agents.performance_monitoring.performance_monitoring_agent import PerformanceMonitoringAgent

class Supervisor:
    def __init__(self):
        self.agents = []
        self.register_agents()

    def register_agents(self):
        available_agents = {
            "InputAgent": InputAgent,
            "PriorityAgent": PriorityAgent,
            "AudioAgent": AudioAgent,
            "ApplicationAgent": ApplicationAgent,
            "OperatingSystemAgent": OperatingSystemAgent,
            "TensorCoreAgent": TensorCoreAgent,
            "GraphicsAgent": GraphicsAgent,
            "NaturalLanguageAgent": NaturalLanguageAgent,
            "EmailAgent": EmailAgent,
            "ChecksumAgent": ChecksumAgent,
            "DocumentAgent": DocumentAgent,
            "NotificationAgent": NotificationAgent,
            "BrowsingAgent": BrowserAutomationAgent,
            "MathAgent": MathAgent,
            "VideoAgent": VideoAgent,
            "WebAgent": WebAgent,
            "ScreenCaptureAgent": ScreenCaptureAgent,
            "DatabaseAgent": DatabaseAgent,
            "NetworkAgent": NetworkAgent,
            "SystemMonitoringAgent": SystemMonitoringAgent,
            "SecurityAgent": SecurityAgent,
            "UpdateAgent": UpdateAgent,
            "BackupAgent": BackupAgent,
            "SchedulerAgent": SchedulerAgent,
            "AIModelTrainingAgent": AIModelTrainingAgent,
            "FileManagementAgent": FileManagementAgent,
            "VirtualizationAgent": AutomationAgent,
            "VoiceControlAgent": VoiceControlAgent,
            "ClipboardAgent": ClipboardAgent,
            "PowerManagementAgent": PowerManagementAgent,
            "SystemInformationAgent": SystemInformationAgent,
            "BrowserAutomationAgent": BrowserAutomationAgent,
            "SpeechSynthesisAgent": SpeechSynthesisAgent,
            "UIAgent": UIAgent,
            "FileTransferAgent": FileTransferAgent,
            "LogManagementAgent": LogManagementAgent,
            "DataVisualizationAgent": DataVisualizationAgent,
            "PersonalAssistantAgent": PersonalAssistantAgent,
            "BackupRestoreAgent": BackupRestoreAgent,
            "EmailClientAgent": EmailClientAgent,
            "DataProcessingAgent": DataProcessingAgent,
            "WebScrapingAgent": WebScrapingAgent,
            "VirtualAssistantAgent": VirtualAssistantAgent,
            "PerformanceMonitoringAgent": PerformanceMonitoringAgent,
        }

        print("Select agents to use (comma separated):")
        for agent_name in available_agents:
            print(agent_name)
        
        selected_agents = input("Enter selected agents: ").split(',')

        for agent_name in selected_agents:
            agent_name = agent_name.strip()
            if agent_name in available_agents:
                self.agents.append(available_agents[agent_name](agent_name, self))
            else:
                print(f"Agent {agent_name} not found")

    def add_subordinate(self, agent):
        self.agents.append(agent)

    def delegate_task(self, user_command):
        for agent in self.agents:
            response = agent.execute_task(user_command)
            if "Unknown command" not in response:
                return response
        return f"No agent could handle the command: {user_command}"
