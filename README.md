<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI System with Multiple Agents</title>
</head>
<body>

<h1>AI System with Multiple Agents</h1>

<p>This project implements a multi-agent system where each agent performs specific tasks, such as managing applications, handling audio processing, performing mathematical calculations, and more. The system includes a supervisor that delegates tasks to the appropriate agents.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#examples">Examples</a>
        <ul>
            <li><a href="#adding-and-processing-tasks">Adding and Processing Tasks</a></li>
            <li><a href="#audio-processing">Audio Processing</a></li>
            <li><a href="#screen-capture">Screen Capture</a></li>
            <li><a href="#system-monitoring">System Monitoring</a></li>
            <li><a href="#sending-emails">Sending Emails</a></li>
            <li><a href="#training-and-saving-models">Training and Saving Models</a></li>
            <li><a href="#loading-models">Loading Models</a></li>
        </ul>
    </li>
    <li><a href="#available-agents-and-commands">Available Agents and Commands</a>
        <ul>
            <li><a href="#application-management-agents">Application Management Agents</a></li>
            <li><a href="#audio-processing-agents">Audio Processing Agents</a></li>
            <li><a href="#communication-agents">Communication Agents</a></li>
            <li><a href="#file-management-agents">File Management Agents</a></li>
            <li><a href="#monitoring-agents">Monitoring Agents</a></li>
            <li><a href="#multimedia-agents">Multimedia Agents</a></li>
            <li><a href="#networking-agents">Networking Agents</a></li>
            <li><a href="#os-management-agents">OS Management Agents</a></li>
            <li><a href="#scheduler-agents">Scheduler Agents</a></li>
            <li><a href="#ai-and-machine-learning-agents">AI and Machine Learning Agents</a></li>
            <li><a href="#database-agent">Database Agent</a></li>
            <li><a href="#utility-agents">Utility Agents</a></li>
        </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#support">Support</a></li>
</ul>

<h2 id="project-structure">Project Structure</h2>
<ul>
    <li><code>agents/</code>: Contains all agent classes.
        <ul>
            <li><code>base_agent.py</code>: The base class for all agents.</li>
            <li><code>application/</code>: Agents related to application management.
                <ul>
                    <li><code>application_agent.py</code>: Manages opening applications.</li>
                    <li><code>web_agent.py</code>: Creates simple web projects.</li>
                </ul>
            </li>
            <li><code>audio/</code>: Agents related to audio processing.
                <ul>
                    <li><code>audio_agent.py</code>: Processes audio files using Whisper for speech-to-text.</li>
                    <li><code>voice_control_agent.py</code>: Processes voice commands.</li>
                </ul>
            </li>
            <li><code>communication/</code>: Agents related to communication.
                <ul>
                    <li><code>email_agent.py</code>: Manages email sending and receiving.</li>
                    <li><code>notification_agent.py</code>: Sends notifications via email, SMS, etc.</li>
                </ul>
            </li>
            <li><code>file_management/</code>: Agents related to file management.
                <ul>
                    <li><code>file_management_agent.py</code>: Manages advanced file operations like compression and encryption.</li>
                    <li><code>document_agent.py</code>: Reads and extracts text from documents.</li>
                    <li><code>backup_agent.py</code>: Manages system backups and restores.</li>
                    <li><code>clipboard_agent.py</code>: Interacts with the system clipboard.</li>
                    <li><code>checksum_agent.py</code>: Calculates and verifies file checksums.</li>
                </ul>
            </li>
            <li><code>monitoring/</code>: Agents related to system monitoring.
                <ul>
                    <li><code>system_monitoring_agent.py</code>: Monitors system performance metrics.</li>
                    <li><code>power_management_agent.py</code>: Manages power settings and monitors battery status.</li>
                    <li><code>system_information_agent.py</code>: Retrieves detailed system information.</li>
                    <li><code>security_agent.py</code>: Handles security operations like scanning for vulnerabilities.</li>
                </ul>
            </li>
            <li><code>multimedia/</code>: Agents related to multimedia processing.
                <ul>
                    <li><code>graphics_agent.py</code>: Renders 3D objects and plots graphs.</li>
                    <li><code>video_agent.py</code>: Processes video files.</li>
                    <li><code>screen_capture_agent.py</code>: Captures screenshots.</li>
                </ul>
            </li>
            <li><code>networking/</code>: Agents related to networking.
                <ul>
                    <li><code>network_agent.py</code>: Performs network operations like pinging and checking connectivity.</li>
                    <li><code>browser_automation_agent.py</code>: Automates browser tasks.</li>
                </ul>
            </li>
            <li><code>os_management/</code>: Agents related to OS management.
                <ul>
                    <li><code>operating_system_agent.py</code>: Manages OS-level tasks like navigating directories.</li>
                    <li><code>update_agent.py</code>: Manages software updates and installations.</li>
                </ul>
            </li>
            <li><code>scheduler/</code>: Agents related to task scheduling.
                <ul>
                    <li><code>scheduler_agent.py</code>: Schedules tasks to be executed at specific times.</li>
                    <li><code>automation_agent.py</code>: Runs automation scripts.</li>
                </ul>
            </li>
            <li><code>ai/</code>: Agents related to AI and machine learning.
                <ul>
                    <li><code>ai_model_training_agent.py</code>: Trains and evaluates machine learning models.</li>
                    <li><code>natural_language_agent.py</code>: Processes text for sentiment analysis.</li>
                    <li><code>tensor_core_agent.py</code>: Provides information about CUDA and tensors.</li>
                </ul>
            </li>
            <li><code>database/</code>: Agents related to database management.
                <ul>
                    <li><code>database_agent.py</code>: Interacts with databases (SQL and NoSQL).</li>
                </ul>
            </li>
            <li><code>utility/</code>: Utility agents for various tasks.
                <ul>
                    <li><code>input_agent.py</code>: Handles real-time user input.</li>
                    <li><code>priority_agent.py</code>: Manages task prioritization.</li>
                    <li><code>math_agent.py</code>: Performs mathematical calculations.</li>
                    <li><code>speech_synthesis_agent.py</code>: Converts text to speech.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><code>supervisor.py</code>: Manages all agents and delegates tasks.</li>
    <li><code>main.py</code>: Entry point for running the system.</li>
    <li><code>requirements.txt</code>: List of required Python packages.</li>
    <li><code>README.md</code>: Project documentation.</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/sslinkyy/AI-PC-Operator.git
cd AI-PC-Operator
        </code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<p>Run the <code>main.py</code> file to start the system:</p>
<pre><code>python main.py</code></pre>

<h2 id="examples">Examples</h2>

<h3 id="adding-and-processing-tasks">Adding and Processing Tasks</h3>
<p>Add tasks with priorities and process them:</p>
<pre><code>supervisor.delegate_task("add_task 1 open_application calculator")
supervisor.delegate_task("add_task 2 navigate_directory /home/user")
supervisor.delegate_task("process_tasks")
</code></pre>

<h3 id="audio-processing">Audio Processing</h3>
<p>Process an audio file for transcription:</p>
<pre><code>supervisor.delegate_task("process_audio /path/to/audio/file.wav")
</code></pre>

<h3 id="screen-capture">Screen Capture</h3>
<p>Capture a screenshot:</p>
<pre><code>supervisor.delegate_task("capture_screen /path/to/save/screenshot.png")
</code></pre>

<h3 id="system-monitoring">System Monitoring</h3>
<p>Monitor system performance:</p>
<pre><code>supervisor.delegate_task("monitor_system")
</code></pre>

<h3 id="sending-emails">Sending Emails</h3>
<p>Send an email:</p>
<pre><code>supervisor.delegate_task("send_email recipient@example.com 'Subject' 'Email body'")
</code></pre>

<h3 id="training-and-saving-models">Training and Saving Models</h3>
<p>Train a model and save it:</p>
<pre><code>supervisor.delegate_task("train_model")
supervisor.delegate_task("save_model /path/to/model.pth")
</code></pre>

<h3 id="loading-models">Loading Models</h3>
<p>Load a previously saved model:</p>
<pre><code>supervisor.delegate_task("load_model /path/to/model.pth")
</code></pre>

<h2 id="available-agents-and-commands">Available Agents and Commands</h2>

<h3 id="application-management-agents">Application Management Agents</h3>

<h4>ApplicationAgent</h4>
<p><strong>Purpose</strong>: Manages opening applications.</p>
<p><strong>Command</strong>: <code>open_application &lt;app_name&gt;</code></p>
<p><strong>Example</strong>: <code>open_application calculator</code></p>

<h4>WebAgent</h4>
<p><strong>Purpose</strong>: Creates simple web projects.</p>
<p><strong>Command</strong>: <code>create_web &lt;project_details&gt;</code></p>
<p><strong>Example</strong>: <code>create_web MyWebProject</code></p>

<h3 id="audio-processing-agents">Audio Processing Agents</h3>

<h4>AudioAgent</h4>
<p><strong>Purpose</strong>: Processes audio files using Whisper for speech-to-text.</p>
<p><strong>Command</strong>: <code>process_audio &lt;audio_path&gt;</code></p>
<p><strong>Example</strong>: <code>process_audio /path/to/audio/file.wav</code></p>

<h4>VoiceControlAgent</h4>
<p><strong>Purpose</strong>: Processes voice commands.</p>
<p><strong>Command</strong>: <code>voice_command</code></p>
<p><strong>Example</strong>: Say a command after running: <code>python main.py</code></p>

<h3 id="communication-agents">Communication Agents</h3>

<h4>EmailAgent</h4>
<p><strong>Purpose</strong>: Manages email sending and receiving.</p>
<p><strong>Command</strong>: <code>send_email &lt;recipient&gt; &lt;subject&gt; &lt;body&gt;</code></p>
<p><strong>Example</strong>: <code>send_email recipient@example.com 'Hello' 'This is a test email.'</code></p>

<h4>NotificationAgent</h4>
<p><strong>Purpose</strong>: Sends notifications via email, SMS, etc.</p>
<p><strong>Command</strong>: <code>send_notification &lt;email&gt; &lt;message&gt;</code></p>
<p><strong>Example</strong>: <code>send_notification user@example.com 'This is a notification message.'</code></p>

<h3 id="file-management-agents">File Management Agents</h3>

<h4>FileManagementAgent</h4>
<p><strong>Purpose</strong>: Manages advanced file operations like compression and encryption.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>compress_file &lt;source&gt; &lt;destination&gt;</code>: Compresses the source directory into a ZIP file at the destination.</li>
    <li><code>encrypt_file &lt;file_path&gt;</code>: Encrypts the specified file.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>compress_file /path/to/source /path/to/destination</code></li>
    <li><code>encrypt_file /path/to/file.txt</code></li>
</ul>

<h4>DocumentAgent</h4>
<p><strong>Purpose</strong>: Reads and extracts text from documents.</p>
<p><strong>Command</strong>: <code>read_document &lt;document_path&gt;</code></p>
<p><strong>Example</strong>: <code>read_document /path/to/document.docx</code></p>

<h4>BackupAgent</h4>
<p><strong>Purpose</strong>: Manages system backups and restores.</p>
<p><strong>Command</strong>: <code>backup &lt;source&gt; &lt;destination&gt;</code></p>
<p><strong>Example</strong>: <code>backup /path/to/source /path/to/destination</code></p>

<h4>ClipboardAgent</h4>
<p><strong>Purpose</strong>: Interacts with the system clipboard.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>copy_to_clipboard &lt;text&gt;</code>: Copies the specified text to the clipboard.</li>
    <li><code>paste_from_clipboard</code>: Pastes the text from the clipboard.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>copy_to_clipboard 'Hello, World!'</code></li>
    <li><code>paste_from_clipboard</code></li>
</ul>

<h4>ChecksumAgent</h4>
<p><strong>Purpose</strong>: Calculates and verifies file checksums.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>calculate_checksum &lt;file_path&gt;</code>: Calculates the checksum for the specified file.</li>
    <li><code>verify_checksum &lt;file_path&gt; &lt;expected_checksum&gt;</code>: Verifies the checksum of the specified file.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>calculate_checksum /path/to/file.txt</code></li>
    <li><code>verify_checksum /path/to/file.txt abcdef123456</code></li>
</ul>

<h3 id="monitoring-agents">Monitoring Agents</h3>

<h4>SystemMonitoringAgent</h4>
<p><strong>Purpose</strong>: Monitors system performance metrics.</p>
<p><strong>Command</strong>: <code>monitor_system</code></p>
<p><strong>Example</strong>: <code>monitor_system</code></p>

<h4>PowerManagementAgent</h4>
<p><strong>Purpose</strong>: Manages power settings and monitors battery status.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>check_battery</code>: Checks the battery status.</li>
    <li><code>shutdown_system</code>: Shuts down the system.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>check_battery</code></li>
    <li><code>shutdown_system</code></li>
</ul>

<h4>SystemInformationAgent</h4>
<p><strong>Purpose</strong>: Retrieves detailed system information.</p>
<p><strong>Command</strong>: <code>get_system_info</code></p>
<p><strong>Example</strong>: <code>get_system_info</code></p>

<h4>SecurityAgent</h4>
<p><strong>Purpose</strong>: Handles security operations like scanning for vulnerabilities.</p>
<p><strong>Command</strong>: <code>scan_vulnerabilities</code></p>
<p><strong>Example</strong>: <code>scan_vulnerabilities</code></p>

<h3 id="multimedia-agents">Multimedia Agents</h3>

<h4>GraphicsAgent</h4>
<p><strong>Purpose</strong>: Renders 3D objects and plots graphs.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>render_3d &lt;object_name&gt;</code>: Renders a 3D object.</li>
    <li><code>plot_graph &lt;equation&gt;</code>: Plots a graph for the given equation.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>render_3d Cube</code></li>
    <li><code>plot_graph 'x**2'</code></li>
</ul>

<h4>VideoAgent</h4>
<p><strong>Purpose</strong>: Processes video files.</p>
<p><strong>Command</strong>: <code>process_video &lt;video_path&gt;</code></p>
<p><strong>Example</strong>: <code>process_video /path/to/video.mp4</code></p>

<h4>ScreenCaptureAgent</h4>
<p><strong>Purpose</strong>: Captures screenshots.</p>
<p><strong>Command</strong>: <code>capture_screen &lt;file_path&gt;</code></p>
<p><strong>Example</strong>: <code>capture_screen /path/to/screenshot.png</code></p>

<h3 id="networking-agents">Networking Agents</h3>

<h4>NetworkAgent</h4>
<p><strong>Purpose</strong>: Performs network operations like pinging and checking connectivity.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>ping &lt;hostname&gt;</code>: Pings the specified hostname.</li>
    <li><code>check_bandwidth</code>: Checks the network bandwidth.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>ping google.com</code></li>
    <li><code>check_bandwidth</code></li>
</ul>

<h4>BrowserAutomationAgent</h4>
<p><strong>Purpose</strong>: Automates browser tasks.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>navigate_to &lt;url&gt;</code>: Navigates to the specified URL.</li>
    <li><code>find_element &lt;selector&gt;</code>: Finds an element on the web page by its CSS selector.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>navigate_to https://www.google.com</code></li>
    <li><code>find_element '#search'</code></li>
</ul>

<h3 id="os-management-agents">OS Management Agents</h3>

<h4>OperatingSystemAgent</h4>
<p><strong>Purpose</strong>: Manages OS-level tasks like navigating directories.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>navigate_directory &lt;directory&gt;</code>: Navigates to the specified directory.</li>
    <li><code>list_directory</code>: Lists the files in the current directory.</li>
    <li><code>create_file &lt;file_name&gt;</code>: Creates a file with the specified name.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>navigate_directory /home/user</code></li>
    <li><code>list_directory</code></li>
    <li><code>create_file newfile.txt</code></li>
</ul>

<h4>UpdateAgent</h4>
<p><strong>Purpose</strong>: Manages software updates and installations.</p>
<p><strong>Command</strong>: <code>update_system</code></p>
<p><strong>Example</strong>: <code>update_system</code></p>

<h3 id="scheduler-agents">Scheduler Agents</h3>

<h4>SchedulerAgent</h4>
<p><strong>Purpose</strong>: Schedules tasks to be executed at specific times.</p>
<p><strong>Command</strong>: <code>schedule_task &lt;time_str&gt; &lt;task&gt;</code></p>
<p><strong>Example</strong>: <code>schedule_task 12:00 open_application calculator</code></p>

<h4>AutomationAgent</h4>
<p><strong>Purpose</strong>: Runs automation scripts.</p>
<p><strong>Command</strong>: <code>run_script &lt;script_path&gt;</code></p>
<p><strong>Example</strong>: <code>run_script /path/to/script.sh</code></p>

<h3 id="ai-and-machine-learning-agents">AI and Machine Learning Agents</h3>

<h4>AIModelTrainingAgent</h4>
<p><strong>Purpose</strong>: Trains and evaluates machine learning models.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>train_model</code>: Trains a machine learning model.</li>
    <li><code>save_model &lt;file_path&gt;</code>: Saves the trained model to the specified file.</li>
    <li><code>load_model &lt;file_path&gt;</code>: Loads a model from the specified file.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>train_model</code></li>
    <li><code>save_model /path/to/model.pth</code></li>
    <li><code>load_model /path/to/model.pth</code></li>
</ul>

<h4>NaturalLanguageAgent</h4>
<p><strong>Purpose</strong>: Processes text for sentiment analysis.</p>
<p><strong>Command</strong>: <code>process_text &lt;text&gt;</code></p>
<p><strong>Example</strong>: <code>process_text 'I love programming!'</code></p>

<h4>TensorCoreAgent</h4>
<p><strong>Purpose</strong>: Provides information about CUDA and tensors.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>cuda_info</code>: Provides information about CUDA availability.</li>
    <li><code>tensor_info</code>: Provides information about tensors.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>cuda_info</code></li>
    <li><code>tensor_info</code></li>
</ul>

<h3 id="database-agent">Database Agent</h3>

<h4>DatabaseAgent</h4>
<p><strong>Purpose</strong>: Interacts with databases (SQL and NoSQL).</p>
<p><strong>Command</strong>: <code>execute_query &lt;db_path&gt; &lt;query&gt;</code></p>
<p><strong>Example</strong>: <code>execute_query /path/to/database.db 'SELECT * FROM users'</code></p>

<h3 id="utility-agents">Utility Agents</h3>

<h4>InputAgent</h4>
<p><strong>Purpose</strong>: Handles real-time user input.</p>
<p><strong>Command</strong>: <code>*delegates to appropriate agent*</code></p>
<p><strong>Example</strong>: <code>open_application calculator</code></p>

<h4>PriorityAgent</h4>
<p><strong>Purpose</strong>: Manages task prioritization.</p>
<p><strong>Commands</strong>:</p>
<ul>
    <li><code>add_task &lt;priority&gt; &lt;task&gt;</code>: Adds a task with the specified priority.</li>
    <li><code>process_tasks</code>: Processes the queued tasks based on their priority.</li>
</ul>
<p><strong>Examples</strong>:</p>
<ul>
    <li><code>add_task 1 open_application calculator</code></li>
    <li><code>process_tasks</code></li>
</ul>

<h4>MathAgent</h4>
<p><strong>Purpose</strong>: Performs mathematical calculations.</p>
<p><strong>Command</strong>: <code>calculate &lt;expression&gt;</code></p>
<p><strong>Example</strong>: <code>calculate '2 + 2 * 2'</code></p>

<h4>SpeechSynthesisAgent</h4>
<p><strong>Purpose</strong>: Converts text to speech.</p>
<p><strong>Command</strong>: <code>speak &lt;text&gt;</code></p>
<p><strong>Example</strong>: <code>speak 'Hello, World!'</code></p>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please fork the repository and submit a pull request with your improvements.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License.</p>

<h2 id="support">Support</h2>
<p>For support, please contact <a href="mailto:support@imobracingonline.com">support@imobracingonline.com</a>.</p>

</body>
</html>
