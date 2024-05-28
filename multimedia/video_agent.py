import cv2
from agents.base_agent import NeuralNetworkAgent

class VideoAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("process_video"):
            _, video_path = user_command.split(maxsplit=1)
            return self.process_video(video_path)
        return self.respond(f"Unknown command: {user_command}")

    def process_video(self, video_path):
        try:
            cap = cv2.VideoCapture(video_path)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            cap.release()
            return self.respond(f"Processed video: {video_path}. Frame count: {frame_count}")
        except Exception as e:
            return self.respond(f"Failed to process video: {video_path}. Error: {str(e)}")
