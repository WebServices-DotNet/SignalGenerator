import threading
from datetime import datetime

from generator.generator_request import GeneratorRequest


class Car:
    def __init__(self, hz, id):
        self.id = id
        self.diff_seconds = 1.0 / hz
        self.hz = hz
        self.last_tick = datetime.now()
        self.request = GeneratorRequest()

    def tick(self):
        now = datetime.now()
        if (now - self.last_tick).total_seconds() > self.diff_seconds:
            self.last_tick = now
            self._generate()

    def _generate(self):
        self.request.request(self.id, "speed", 1.0)
        

class CarGenerator(threading.Thread):

    def __init__(self, cars):
        threading.Thread.__init__(self)
        self.cars = [Car(car["hz"], car["id"]) for car in cars]
        self._stop_event = threading.Event()
        self.thread = None

    def run(self):
        while True:
            if self._stopped():
                return
            for car in self.cars:
                car.tick()

    def stop(self):
        self._stop_event.set()

    def _stopped(self):
        return self._stop_event.is_set()
