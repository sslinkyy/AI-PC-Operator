# AI-PC-Operator
AI PC Operator with stock analysis capabilities
# Hierarchical Agent System with Error Handling
# AI System with Multiple Agents

This project implements a multi-agent system where each agent performs specific tasks, such as managing applications, handling audio processing, performing mathematical calculations, and more. The system includes a supervisor that delegates tasks to the appropriate agents.

## Project Structure

- `agents/`: Contains all agent classes.
  - `base_agent.py`: The base class for all agents.
  - `application/`: Agents related to application management.
    - `application_agent.py`: Manages opening applications.
    - `web_agent.py`: Creates simple web projects.
  - `audio/`: Agents related to audio processing.
    - `audio_agent.py`: Processes audio files using Whisper for speech-to-text.
    - `voice_control_agent.py`: Processes voice commands.
  - `communication/`: Agents related to communication.
    - `email_agent.py`: Manages email sending and receiving.
    - `notification_agent.py`: Sends notifications via email, SMS, etc.
  - `file_management/`: Agents related to file management.
    - `file_management_agent.py`: Manages advanced file operations like compression and encryption.
    - `document_agent.py`: Reads and extracts text from documents.
    - `backup_agent.py`: Manages system backups and restores.
    - `clipboard_agent.py`: Interacts with the system clipboard.
    - `checksum_agent.py`: Calculates and verifies file checksums.
  - `monitoring/`: Agents related to system monitoring.
    - `system_monitoring_agent.py`: Monitors system performance metrics.
    - `power_management_agent.py`: Manages power settings and monitors battery status.
    - `system_information_agent.py`: Retrieves detailed system information.
    - `security_agent.py`: Handles security operations like scanning for vulnerabilities.
  - `multimedia/`: Agents related to multimedia processing.
    - `graphics_agent.py`: Renders 3D objects and plots graphs.
    - `video_agent.py`: Processes video files.
    - `screen_capture_agent.py`: Captures screenshots.
  - `networking/`: Agents related to networking.
    - `network_agent.py`: Performs network operations like pinging and checking connectivity.
    - `browser_automation_agent.py`: Automates browser tasks.
  - `os_management/`: Agents related to OS management.
    - `operating_system_agent.py`: Manages OS-level tasks like navigating directories.
    - `update_agent.py`: Manages software updates and installations.
  - `scheduler/`: Agents related to task scheduling.
    - `scheduler_agent.py`: Schedules tasks to be executed at specific times.
    - `automation_agent.py`: Runs automation scripts.
  - `ai/`: Agents related to AI and machine learning.
    - `ai_model_training_agent.py`: Trains and evaluates machine learning models.
    - `natural_language_agent.py`: Processes text for sentiment analysis.
    - `tensor_core_agent.py`: Provides information about CUDA and tensors.
  - `database/`: Agents related to database management.
    - `database_agent.py`: Interacts with databases (SQL and NoSQL).
  - `utility/`: Utility agents for various tasks.
    - `input_agent.py`: Handles real-time user input.
    - `priority_agent.py`: Manages task prioritization.
    - `math_agent.py`: Performs mathematical calculations.
    - `speech_synthesis_agent.py`: Converts text to speech.

- `supervisor.py`: Manages all agents and delegates tasks.
- `main.py`: Entry point for running the system.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/sslinkyy/AI-PC-Operator.git
   cd AI-PC-Operator
Install the required packages:
sh
Copy code
pip install -r requirements.txt
Usage
Run the main.py file to start the system:

sh
Copy code
python main.py
Examples
Adding and Processing Tasks
Add tasks with priorities and process them:

python
Copy code
supervisor.delegate_task("add_task 1 open_application calculator")
supervisor.delegate_task("add_task 2 navigate_directory /home/user")
supervisor.delegate_task("process_tasks")
Audio Processing
Process an audio file for transcription:

python
Copy code
supervisor.delegate_task("process_audio /path/to/audio/file.wav")
Screen Capture
Capture a screenshot:

python
Copy code
supervisor.delegate_task("capture_screen /path/to/save/screenshot.png")
System Monitoring
Monitor system performance:

python
Copy code
supervisor.delegate_task("monitor_system")
Sending Emails
Send an email:

python
Copy code
supervisor.delegate_task("send_email recipient@example.com 'Subject' 'Email body'")
Training and Saving Models
Train a model and save it:

python
Copy code
supervisor.delegate_task("train_model")
supervisor.delegate_task("save_model /path/to/model.pth")
Loading Models
Load a previously saved model:

python
Copy code
supervisor.delegate_task("load_model /path/to/model.pth")
Available Agents and Commands
Application Management Agents
ApplicationAgent
Command: open_application <app_name>
WebAgent
Command: create_web <project_details>
Audio Processing Agents
AudioAgent
Command: process_audio <audio_path>
VoiceControlAgent
Command: voice_command
Communication Agents
EmailAgent
Command: send_email <recipient> <subject> <body>
NotificationAgent
Command: send_notification <email> <message>
File Management Agents
FileManagementAgent
Commands: compress_file <source> <destination>, encrypt_file <file_path>
DocumentAgent
Command: read_document <document_path>
BackupAgent
Command: backup <source> <destination>
ClipboardAgent
Commands: copy_to_clipboard <text>, paste_from_clipboard
ChecksumAgent
Commands: calculate_checksum <file_path>, verify_checksum <file_path> <expected_checksum>
Monitoring Agents
SystemMonitoringAgent
Command: monitor_system
PowerManagementAgent
Commands: check_battery, shutdown_system
SystemInformationAgent
Command: get_system_info
SecurityAgent
Command: scan_vulnerabilities
Multimedia Agents
GraphicsAgent
Commands: render_3d <object_name>, plot_graph <equation>
VideoAgent
Command: process_video <video_path>
ScreenCaptureAgent
Command: capture_screen <file_path>
Networking Agents
NetworkAgent
Commands: ping <hostname>, check_bandwidth
BrowserAutomationAgent
Commands: navigate_to <url>, find_element <selector>
OS Management Agents
OperatingSystemAgent
Commands: navigate_directory <directory>, list_directory, create_file <file_name>
UpdateAgent
Command: update_system
Scheduler Agents
SchedulerAgent
Command: schedule_task <time_str> <task>
AutomationAgent
Command: run_script <script_path>
AI and Machine Learning Agents
AIModelTrainingAgent
Commands: train_model, save_model <file_path>, load_model <file_path>
NaturalLanguageAgent
Command: process_text <text>
TensorCoreAgent
Commands: cuda_info, tensor_info
Database Agent
DatabaseAgent
Command: execute_query <db_path> <query>
Utility Agents
InputAgent
Command: *delegates to appropriate agent*
PriorityAgent
Commands: add_task <priority> <task>, process_tasks
MathAgent
Command: calculate <expression>
SpeechSynthesisAgent
Command: speak <text>
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License.

Support
For support, please contact support@imobracingonline.com.
