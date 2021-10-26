from generator.generator_logger import GeneratorLogger
from rabbitmq.rabbitmq_manager import RabbitMqManager


class GeneratorRequest:

    def __init__(self):
        self.rabbit_manager = RabbitMqManager()
        self.logger = GeneratorLogger()
        self.rabbit_manager.connect()

    def request(self, id, signal_name, value):
        self.logger.log(id, signal_name, value)
        self.rabbit_manager.send(str(signal_name) + " " + str(value))
