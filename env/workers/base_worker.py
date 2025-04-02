class BaseWorker:
    def __init__(self, config=None):
        self.config = config

    def run(self, task_input):
        raise NotImplementedError("Each worker must implement the run() method.")
