from rabbitmq.rabbitmq import RabbitMq


class RabbitMqManager:

    def __init__(self):
        self.rabbitmq = RabbitMq()

    def connect(self):
        print("RabbitMqManager connecting")
        self.rabbitmq.connect()
        print("RabbitMqManager connected")

    def send(self, message):
        self.rabbitmq.send(message)