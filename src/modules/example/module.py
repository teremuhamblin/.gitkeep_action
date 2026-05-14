class Module:
    def __init__(self, config):
        self.config = config

    def run(self):
        print(f"[ExampleModule] Running with config: {self.config}")
