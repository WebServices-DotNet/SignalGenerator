
import pika
import os


class RabbitMq:

    def __init__(self):
        url = os.environ.get('CLOUDAMQP_URL', 'amqps://stmyakko:jsbLtBdO7Y2CVzANgk8sCW4zhpUbxmdA@poodle.rmq2.cloudamqp.com/stmyakko')
        self.params = pika.URLParameters(url)
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.exchange_declare('test_exchange')
        self.channel.queue_declare(queue='test_queue')
        self.channel.queue_bind('test_queue', 'test_exchange', 'tests')

    def send(self, message):
        self.channel.basic_publish(exchange='test_exchange', routing_key='tests', body=message)
