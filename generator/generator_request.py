from generator.generator_logger import GeneratorLogger


class GeneratorRequest:

    def __init__(self):
        self.logger = GeneratorLogger()

    def request(self, id, signal_name, value):
        self.logger.log(id, signal_name, value)
        # TODO
        pass
