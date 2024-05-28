import torch
from agents.base_agent import NeuralNetworkAgent

class TensorCoreAgent(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("cuda_info"):
            return self.get_cuda_info()
        elif user_command.startswith("tensor_info"):
            return self.get_tensor_info()
        return self.respond(f"Unknown command: {user_command}")

    def get_cuda_info(self):
        try:
            cuda_available = torch.cuda.is_available()
            cuda_device_count = torch.cuda.device_count()
            cuda_device_name = torch.cuda.get_device_name(0) if cuda_available else "N/A"
            return self.respond(f"CUDA available: {cuda_available}, Device count: {cuda_device_count}, Device name: {cuda_device_name}")
        except Exception as e:
            return self.respond(f"Failed to retrieve CUDA info. Error: {str(e)}")

    def get_tensor_info(self):
        try:
            tensor = torch.randn(3, 3)
            tensor_info = {
                'shape': tensor.shape,
                'dtype': tensor.dtype,
                'device': tensor.device
            }
            return self.respond(f"Tensor info: {tensor_info}")
        except Exception as e:
            return self.respond(f"Failed to retrieve tensor info. Error: {str(e)}")
