import threading
import time
from datetime import datetime
import math
import random

class Car:
    def __init__(self, hz, id, request):
        self.id = id
        self.diff_seconds = 1.0 / hz
        self.hz = hz
        self.last_tick = datetime.now()
        self.request = request
        self.x_1 = 0
        self.x_2 = 0
        self.x_3 = 0
        self.x_4 = 0

        self.amplitude = 1

        self.diff_seconds_speed = 1.0 / 1.0
        self.last_speed_tick = datetime.now()
        # 1 - 50

        self.diff_seconds_accel = 1.0 / 2.0
        self.last_accel_tick = datetime.now()

        self.diff_seconds_temperature = 1.0 / 0.5
        self.last_temperature_tick = datetime.now()
        # 41 - 250

        self.diff_seconds_engine_speed = 1.0 / 2.0
        self.last_engine_speed_tick = datetime.now()
        # 0 - 6
    #     speed -> 1hz
    #     accel -> 2hz
    #     engine temperature ->  0.5hz
    #     engine speed -> 2hz

    def tick(self):
        now = datetime.now()

        if (now - self.last_speed_tick).total_seconds() > self.diff_seconds_speed:
            self.x_1 += 0.1
            self.last_speed_tick = now
            value = self.amplitude * math.sin(self.x_1)
            self.request.request(self.id, str(self.id), "speed", str({"value": random.randrange(1, 50)}))

        if (now - self.last_accel_tick).total_seconds() > self.diff_seconds_accel:
            self.x_2 += 0.1
            self.last_accel_tick = now
            value = self.amplitude * math.sin(self.x_2)
            self.request.request(self.id, str(self.id), "accel", str({"x": value, "y": value, "z": value}))

        if (now - self.last_temperature_tick).total_seconds() > self.diff_seconds_temperature:
            self.x_3 += 0.1
            self.last_temperature_tick = now
            value = self.amplitude * math.sin(self.x_3)
            self.request.request(self.id, str(self.id), "temperature", str({"value": random.randrange(41, 250)}))

        if (now - self.last_engine_speed_tick).total_seconds() > self.diff_seconds_engine_speed:
            self.x_4 += 0.1
            self.last_engine_speed_tick = now
            value = self.amplitude * math.sin(self.x_4)
            self.request.request(self.id, str(self.id), "engine", str({"rpm": random.randrange(1, 3)}))


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
            time.sleep(0.001)

    def stop(self):
        self._stop_event.set()

    def _stopped(self):
        return self._stop_event.is_set()
