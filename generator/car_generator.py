import threading
import time
from datetime import datetime
import math


class Car:
    def __init__(self, hz, id, request):
        self.id = id
        self.diff_seconds = 1.0 / hz
        self.hz = hz
        self.last_tick = datetime.now()
        self.request = request
        self.x = 0
        self.amplitude = 1

    def tick(self):
        now = datetime.now()
        if (now - self.last_tick).total_seconds() > self.diff_seconds:
            self.last_tick = now
            self._generate()

    def _generate(self):
        self.x += 0.1
        self.request.request(self.id, "speed", self.amplitude * math.sin(self.x))


class CarGenerator(threading.Thread):

    def __init__(self, cars, request):
        threading.Thread.__init__(self)
        self.cars = [Car(car["hz"], car["id"], request) for car in cars]
        self._stop_event = threading.Event()
        self.thread = None

    def run(self):
        while True:
            if self._stopped():
                return
            for car in self.cars:
                car.tick()
            time.sleep(0.1)

    def stop(self):
        self._stop_event.set()

    def _stopped(self):
        return self._stop_event.is_set()
