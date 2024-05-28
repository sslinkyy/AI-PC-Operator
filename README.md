██╗ ███╗ ███╗  ██████╗ ██████╗
██║████╗ ████║██╔═══██╗██╔══██╗
██║██╔████╔██║██║   ██║██████╔╝
██║██║╚██╔╝██║██║   ██║██╔══██╗
██║██║ ╚═╝ ██║╚██████╔╝██████║
╚═╝╚═╝ ╚═╝ ╚══    ═══╝ ╚═╝ ╚═╝
# AI System with Multiple Agents

This project implements a multi-agent system where each agent performs specific tasks, such as managing applications, handling audio processing, performing mathematical calculations, and more. The system includes a supervisor that delegates tasks to the appropriate agents.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
  - [Application Agents](#application-agents)
  - [Audio Agents](#audio-agents)
  - [Backup and Restore Agents](#backup-and-restore-agents)
  - [Communication Agents](#communication-agents)
  - [Data Processing Agents](#data-processing-agents)
  - [Database Agents](#database-agents)
  - [Email Client Agents](#email-client-agents)
  - [File Management Agents](#file-management-agents)
  - [File Transfer Agents](#file-transfer-agents)
  - [Log Management Agents](#log-management-agents)
  - [Monitoring Agents](#monitoring-agents)
  - [Multimedia Agents](#multimedia-agents)
  - [Networking Agents](#networking-agents)
  - [OS Management Agents](#os-management-agents)
  - [Performance Monitoring Agents](#performance-monitoring-agents)
  - [Scheduler Agents](#scheduler-agents)
  - [AI Agents](#ai-agents)
  - [Utility Agents](#utility-agents)
  - [Virtual Assistant Agents](#virtual-assistant-agents)
  - [Web Scraping Agents](#web-scraping-agents)
  - [UI Agents](#ui-agents)
  - [Testing Agents](#testing-agents)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Project Structure

- `agents/`: Contains all agent classes.
  - `base_agent.py`: The base class for all agents.
  - `application/`: Agents related to application management.
    - `application_agent.py`: Manages opening applications.
    - `web_agent.py`: Creates simple web projects.
  - `audio/`: Agents related to audio processing.
    - `audio_agent.py`: Processes audio files using Whisper for speech-to-text.
    - `voice_control_agent.py`: Processes voice commands.
  - `backup_restore/`: Agents related to backup and restore operations.
    - `backup_restore_agent.py`: Manages system backups and restores.
  - `communication/`: Agents related to communication.
    - `email_agent.py`: Manages email sending and receiving.
    - `notification_agent.py`: Sends notifications via email, SMS, etc.
  - `data_processing/`: Agents related to data processing.
    - `data_processing_agent.py`: Processes data files.
  - `database/`: Agents related to database management.
    - `database_agent.py`: Interacts with databases (SQL and NoSQL).
  - `email_client/`: Agents related to email client operations.
    - `email_client_agent.py`: Manages sending and receiving emails.
  - `file_management/`: Agents related to file management.
    - `file_management_agent.py`: Manages advanced file operations like compression and encryption.
    - `document_agent.py`: Reads and extracts text from documents.
    - `backup_agent.py`: Manages system backups and restores.
    - `clipboard_agent.py`: Interacts with the system clipboard.
    - `checksum_agent.py`: Calculates and verifies file checksums.
  - `file_transfer/`: Agents related to file transfer.
    - `file_transfer_agent.py`: Manages file transfers over the network.
  - `log_management/`: Agents related to log management.
    - `log_management_agent.py`: Manages system logs.
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
  - `performance_monitoring/`: Agents related to performance monitoring.
    - `performance_monitoring_agent.py`: Monitors system performance.
  - `scheduler/`: Agents related to task scheduling.
    - `scheduler_agent.py`: Schedules tasks to be executed at specific times.
    - `automation_agent.py`: Runs automation scripts.
  - `ai/`: Agents related to AI and machine learning.
    - `ai_model_training_agent.py`: Trains and evaluates machine learning models.
    - `natural_language_agent.py`: Processes text for sentiment analysis.
    - `tensor_core_agent.py`: Provides information about CUDA and tensors.
  - `utility/`: Utility agents for various tasks.
    - `input_agent.py`: Handles real-time user input.
    - `priority_agent.py`: Manages task prioritization.
    - `math_agent.py`: Performs mathematical calculations.
    - `speech_synthesis_agent.py`: Converts text to speech.
  - `virtual_assistant/`: Agents related to virtual assistant functionalities.
    - `virtual_assistant_agent.py`: Provides virtual assistant capabilities.
  - `web_scraping/`: Agents related to web scraping.
    - `web_scraping_agent.py`: Scrapes data from websites.
  - `ui/`: Agents related to user interface rendering.
    - `ui_agent.py`: Manages UI components.
  - `testing/`: Agents related to testing and debugging.
    - `testing_agent.py`: Tests and debugs other agents.

- `supervisor.py`: Manages all agents and delegates tasks.
- `main.py`: Entry point for running the system.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sslinkyy/AI-PC-Operator.git
    cd AI-PC-Operator
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Follow the prompts to select agents and enter commands.

## Agents

### Application Agents

#### ApplicationAgent

- **Purpose**: Manages opening applications.
- **Command**: `open_application <app_name>`
- **Example**: `open_application calculator`

#### WebAgent

- **Purpose**: Creates simple web projects.
- **Command**: `create_web <project_details>`
- **Example**: `create_web MyProject`

### Audio Agents

#### AudioAgent

- **Purpose**: Processes audio files using Whisper for speech-to-text.
- **Command**: `process_audio <audio_path>`
- **Example**: `process_audio sample.wav`

#### VoiceControlAgent

- **Purpose**: Processes voice commands.
- **Command**: `voice_command`
- **Example**: `voice_command`

### Backup and Restore Agents

#### BackupRestoreAgent

- **Purpose**: Manages system backups and restores.
- **Commands**:
  - `backup <source> <destination>`
  - `restore <source> <destination>`
- **Examples**:
  - `backup /source/dir /backup/dir`
  - `restore /backup/dir /source/dir`

### Communication Agents

#### EmailAgent

- **Purpose**: Manages email sending and receiving.
- **Command**: `send_email <recipient> <subject> <body>`
- **Example**: `send_email example@example.com "Subject" "Email body"`

#### NotificationAgent

- **Purpose**: Sends notifications via email.
- **Command**: `send_notification <email> <message>`
- **Example**: `send_notification example@example.com "Notification message"`

### Data Processing Agents

#### DataProcessingAgent

- **Purpose**: Processes data files.
- **Command**: `process_data <file_path>`
- **Example**: `process_data data.csv`

### Database Agents

#### DatabaseAgent

- **Purpose**: Interacts with databases (SQL and NoSQL).
- **Command**: `execute_query <db_path> <query>`
- **Example**: `execute_query mydatabase.db "SELECT * FROM users"`

### Email Client Agents

#### EmailClientAgent

- **Purpose**: Manages sending and receiving emails.
- **Commands**:
  - `send_email <recipient> <subject> <body>`
  - `fetch_emails`
- **Examples**:
  - `send_email example@example.com "Subject" "Email body"`
  - `fetch_emails`

### File Management Agents

#### FileManagementAgent

- **Purpose**: Manages advanced file operations like compression and encryption.
- **Commands**:
  - `compress_file <source> <destination>`
  - `encrypt_file <file_path>`
- **Examples**:
  - `compress_file /source/dir /destination/dir`
  - `encrypt_file secret.txt`

#### DocumentAgent

- **Purpose**: Reads and extracts text from documents.
- **Command**: `read_document <document_path>`
- **Example**: `read_document document.docx`

#### BackupAgent

- **Purpose**: Manages system backups and restores.
- **Commands**:
  - `backup <source> <destination>`
- **Example**: `backup /source/dir /backup/dir`

#### ClipboardAgent

- **Purpose**: Interacts with the system clipboard.
- **Commands**:
  - `copy_to_clipboard <text>`
  - `paste_from_clipboard`
- **Examples**:
  - `copy_to_clipboard "Hello, World!"`
  - `paste_from_clipboard`

#### ChecksumAgent

- **Purpose**: Calculates and verifies file checksums.
- **Commands**:
  - `calculate_checksum <file_path>`
  - `verify_checksum <file_path> <expected_checksum>`
- **Examples**:
  - `calculate_checksum myfile.txt`
  - `verify_checksum myfile.txt 123456789abcdef`

### File Transfer Agents

#### FileTransferAgent

- **Purpose**: Manages file transfers over the network.
- **Command**: `transfer_file <hostname> <username> <password> <source> <destination>`
- **Example**: `transfer_file 192.168.1.1 user pass /source/file /destination/file`

### Log Management Agents

#### LogManagementAgent

- **Purpose**: Manages system logs.
- **Command**: `log_message <message>`
- **Example**: `log_message "This is a log message"`

### Monitoring Agents

#### SystemMonitoringAgent

- **Purpose**: Monitors system performance metrics.
- **Command**: `monitor_system`
- **Example**: `monitor_system`

#### PowerManagementAgent

- **Purpose**: Manages power settings and monitors battery status.
- **Commands**:
  - `check_battery`
  - `shutdown_system`
- **Examples**:
  - `check_battery`
  - `shutdown_system`

#### SystemInformationAgent

- **Purpose**: Retrieves detailed system information.
- **Command**: `get_system_info`
- **Example**: `get_system_info`

#### SecurityAgent

- **Purpose**: Handles security operations like scanning for vulnerabilities.
- **Command**: `scan_vulnerabilities`
- **Example**: `scan_vulnerabilities`

### Multimedia Agents

#### GraphicsAgent

- **Purpose**: Renders 3D objects and plots graphs.
- **Commands**:
  - `render_3d <object_name>`
  - `plot_graph <equation>`
- **Examples**:
  - `render_3d cube`
  - `plot_graph "sin(x)"`

#### VideoAgent

- **Purpose**: Processes video files.
- **Command**: `process_video <video_path>`
- **Example**: `process_video video.mp4`

#### ScreenCaptureAgent

- **Purpose**: Captures screenshots.
- **Command**: `capture_screen <file_path>`
- **Example**: `capture_screen screenshot.png`

### Networking Agents

#### NetworkAgent

- **Purpose**: Performs network operations like pinging and checking connectivity.
- **Commands**:
  - `ping <hostname>`
  - `check_bandwidth`
- **Examples**:
  - `ping google.com`
  - `check_bandwidth`

#### BrowserAutomationAgent

- **Purpose**: Automates browser tasks.
- **Commands**:
  - `navigate_to <url>`
  - `find_element <selector>`
- **Examples**:
  - `navigate_to https://example.com`
  - `find_element #main`

### OS Management Agents

#### OperatingSystemAgent

- **Purpose**: Manages OS-level tasks like navigating directories.
- **Commands**:
  - `navigate_directory <directory>`
  - `list_directory`
  - `create_file <file_name>`
- **Examples**:
  - `navigate_directory /home/user`
  - `list_directory`
  - `create_file newfile.txt`

#### UpdateAgent

- **Purpose**: Manages software updates and installations.
- **Command**: `update_system`
- **Example**: `update_system`

### Performance Monitoring Agents

#### PerformanceMonitoringAgent

- **Purpose**: Monitors system performance.
- **Command**: `monitor_performance`
- **Example**: `monitor_performance`

### Scheduler Agents

#### SchedulerAgent

- **Purpose**: Schedules tasks to be executed at specific times.
- **Commands**:
  - `schedule_task <time> <task>`
  - `process_tasks`
- **Examples**:
  - `schedule_task 12:00 "backup /source /destination"`
  - `process_tasks`

#### AutomationAgent

- **Purpose**: Runs automation scripts.
- **Command**: `run_script <script_path>`
- **Example**: `run_script script.sh`

### AI Agents

#### AIModelTrainingAgent

- **Purpose**: Trains and evaluates machine learning models.
- **Commands**:
  - `train_model`
  - `save_model <file_path>`
  - `load_model <file_path>`
- **Examples**:
  - `train_model`
  - `save_model model.pth`
  - `load_model model.pth`

#### NaturalLanguageAgent

- **Purpose**: Processes text for sentiment analysis.
- **Command**: `process_text <text>`
- **Example**: `process_text "I love programming!"`

#### TensorCoreAgent

- **Purpose**: Provides information about CUDA and tensors.
- **Commands**:
  - `cuda_info`
  - `tensor_info`
- **Examples**:
  - `cuda_info`
  - `tensor_info`

### Utility Agents

#### InputAgent

- **Purpose**: Handles real-time user input.
- **Command**: User-defined
- **Example**: User-defined

#### PriorityAgent

- **Purpose**: Manages task prioritization.
- **Commands**:
  - `add_task <priority> <task>`
  - `process_tasks`
- **Examples**:
  - `add_task 1 "backup /source /destination"`
  - `process_tasks`

#### MathAgent

- **Purpose**: Performs mathematical calculations.
- **Command**: `calculate <expression>`
- **Example**: `calculate "2+2"`

#### SpeechSynthesisAgent

- **Purpose**: Converts text to speech.
- **Command**: `speak <text>`
- **Example**: `speak "Hello, world!"`

### Virtual Assistant Agents

#### VirtualAssistantAgent

- **Purpose**: Provides virtual assistant capabilities.
- **Command**: `assist <query>`
- **Example**: `assist "What's the weather like?"`

### Web Scraping Agents

#### WebScrapingAgent

- **Purpose**: Scrapes data from websites.
- **Command**: `scrape_website <url>`
- **Example**: `scrape_website https://example.com`

### UI Agents

#### UIAgent

- **Purpose**: Manages UI components.
- **Command**: `render_ui <component>`
- **Example**: `render_ui button`

### Testing Agents

#### TestingAgent

- **Purpose**: Tests and debugs other agents.
- **Commands**:
  - `run_tests`
  - `test_agent <AgentName>`
- **Examples**:
  - `run_tests`
  - `test_agent ApplicationAgent`

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

For support, please contact [support@imobracingonline.com](mailto:support@imobracingonline.com).
