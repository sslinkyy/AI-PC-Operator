# AI System with Multiple Agents

This project implements a multi-agent system where each agent performs specific tasks, such as managing applications, handling audio processing, performing mathematical calculations, and more. The system includes a supervisor that delegates tasks to the appropriate agents.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Examples](#examples)
    1. [Adding and Processing Tasks](#adding-and-processing-tasks)
    2. [Audio Processing](#audio-processing)
    3. [Screen Capture](#screen-capture)
    4. [System Monitoring](#system-monitoring)
    5. [Sending Emails](#sending-emails)
    6. [Training and Saving Models](#training-and-saving-models)
    7. [Loading Models](#loading-models)
5. [Available Agents and Commands](#available-agents-and-commands)
    1. [Application Management Agents](#application-management-agents)
    2. [Audio Processing Agents](#audio-processing-agents)
    3. [Communication Agents](#communication-agents)
    4. [File Management Agents](#file-management-agents)
    5. [Monitoring Agents](#monitoring-agents)
    6. [Multimedia Agents](#multimedia-agents)
    7. [Networking Agents](#networking-agents)
    8. [OS Management Agents](#os-management-agents)
    9. [Scheduler Agents](#scheduler-agents)
    10. [AI and Machine Learning Agents](#ai-and-machine-learning-agents)
    11. [Database Agent](#database-agent)
    12. [Utility Agents](#utility-agents)
6. [Contributing](#contributing)
7. [License](#license)
8. [Support](#support)

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
Purpose: Manages opening applications.
Command: open_application <app_name>
Example: open_application calculator
WebAgent
Purpose: Creates simple web projects.
Command: create_web <project_details>
Example: create_web MyWebProject
Audio Processing Agents
AudioAgent
Purpose: Processes audio files using Whisper for speech-to-text.
Command: process_audio <audio_path>
Example: process_audio /path/to/audio/file.wav
VoiceControlAgent
Purpose: Processes voice commands.
Command: voice_command
Example: Say a command after running: python main.py
Communication Agents
EmailAgent
Purpose: Manages email sending and receiving.
Command: send_email <recipient> <subject> <body>
Example: send_email recipient@example.com 'Hello' 'This is a test email.'
NotificationAgent
Purpose: Sends notifications via email, SMS, etc.
Command: send_notification <email> <message>
Example: send_notification user@example.com 'This is a notification message.'
File Management Agents
FileManagementAgent
Purpose: Manages advanced file operations like compression and encryption.
Commands:
compress_file <source> <destination>: Compresses the source directory into a ZIP file at the destination.
encrypt_file <file_path>: Encrypts the specified file.
Examples:
compress_file /path/to/source /path/to/destination
encrypt_file /path/to/file.txt
DocumentAgent
Purpose: Reads and extracts text from documents.
Command: read_document <document_path>
Example: read_document /path/to/document.docx
BackupAgent
Purpose: Manages system backups and restores.
Command: backup <source> <destination>
Example: backup /path/to/source /path/to/destination
ClipboardAgent
Purpose: Interacts with the system clipboard.
Commands:
copy_to_clipboard <text>: Copies the specified text to the clipboard.
paste_from_clipboard: Pastes the text from the clipboard.
Examples:
copy_to_clipboard 'Hello, World!'
paste_from_clipboard
ChecksumAgent
Purpose: Calculates and verifies file checksums.
Commands:
calculate_checksum <file_path>: Calculates the checksum for the specified file.
verify_checksum <file_path> <expected_checksum>: Verifies the checksum of the specified file.
Examples:
calculate_checksum /path/to/file.txt
verify_checksum /path/to/file.txt abcdef123456
Monitoring Agents
SystemMonitoringAgent
Purpose: Monitors system performance metrics.
Command: monitor_system
Example: monitor_system
PowerManagementAgent
Purpose: Manages power settings and monitors battery status.
Commands:
check_battery: Checks the battery status.
shutdown_system: Shuts down the system.
Examples:
check_battery
shutdown_system
SystemInformationAgent
Purpose: Retrieves detailed system information.
Command: get_system_info
Example: get_system_info
SecurityAgent
Purpose: Handles security operations like scanning for vulnerabilities.
Command: scan_vulnerabilities
Example: scan_vulnerabilities
Multimedia Agents
GraphicsAgent
Purpose: Renders 3D objects and plots graphs.
Commands:
render_3d <object_name>: Renders a 3D object.
plot_graph <equation>: Plots a graph for the given equation.
Examples:
render_3d Cube
plot_graph 'x**2'
VideoAgent
Purpose: Processes video files.
Command: process_video <video_path>
Example: process_video /path/to/video.mp4
ScreenCaptureAgent
Purpose: Captures screenshots.
Command: capture_screen <file_path>
Example: capture_screen /path/to/screenshot.png
Networking Agents
NetworkAgent
Purpose: Performs network operations like pinging and checking connectivity.
Commands:
ping <hostname>: Pings the specified hostname.
check_bandwidth: Checks the network bandwidth.
Examples:
ping google.com
check_bandwidth
BrowserAutomationAgent
Purpose: Automates browser tasks.
Commands:
navigate_to <url>: Navigates to the specified URL.
find_element <selector>: Finds an element on the web page by its CSS selector.
Examples:
navigate_to https://www.google.com
find_element '#search'
OS Management Agents
OperatingSystemAgent
Purpose: Manages OS-level tasks like navigating directories.
Commands:
navigate_directory <directory>: Navigates to the specified directory.
list_directory: Lists the files in the current directory.
create_file <file_name>: Creates a file with the specified name.
Examples:
navigate_directory /home/user
list_directory
create_file newfile.txt
UpdateAgent
Purpose: Manages software updates and installations.
Command: update_system
Example: update_system
Scheduler Agents
SchedulerAgent
Purpose: Schedules tasks to be executed at specific times.
Command: schedule_task <time_str> <task>
Example: schedule_task 12:00 open_application calculator
AutomationAgent
Purpose: Runs automation scripts.
Command: run_script <script_path>
Example: run_script /path/to/script.sh
AI and Machine Learning Agents
AIModelTrainingAgent
Purpose: Trains and evaluates machine learning models.
Commands:
train_model: Trains a machine learning model.
save_model <file_path>: Saves the trained model to the specified file.
load_model <file_path>: Loads a model from the specified file.
Examples:
train_model
save_model /path/to/model.pth
load_model /path/to/model.pth
NaturalLanguageAgent
Purpose: Processes text for sentiment analysis.
Command: process_text <text>
Example: process_text 'I love programming!'
TensorCoreAgent
Purpose: Provides information about CUDA and tensors.
Commands:
cuda_info: Provides information about CUDA availability.
tensor_info: Provides information about tensors.
Examples:
cuda_info
tensor_info
Database Agent
DatabaseAgent
Purpose: Interacts with databases (SQL and NoSQL).
Command: execute_query <db_path> <query>
Example: execute_query /path/to/database.db 'SELECT * FROM users'
Utility Agents
InputAgent
Purpose: Handles real-time user input.
Command: *delegates to appropriate agent*
Example: open_application calculator
PriorityAgent
Purpose: Manages task prioritization.
Commands:
add_task <priority> <task>: Adds a task with the specified priority.
process_tasks: Processes the queued tasks based on their priority.
Examples:
add_task 1 open_application calculator
process_tasks
MathAgent
Purpose: Performs mathematical calculations.
Command: calculate <expression>
Example: calculate '2 + 2 * 2'
SpeechSynthesisAgent
Purpose: Converts text to speech.
Command: speak <text>
Example: speak 'Hello, World!'
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License.

Support
For support, please contact support@imobracingonline.com.
