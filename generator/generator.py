from generator.car_generator import CarGenerator
from generator.generator_request import GeneratorRequest
import uuid

from generator.names import Names


class GeneratorManager:

    def __init__(self):
        self.hz = 0.2
        self.numberOfCars = 30
        self.thread = None
        self._create_cars()
        self.request = GeneratorRequest()

    def _create_cars(self):
        self.cars = []
        for i in range(self.numberOfCars):
            self.cars.append({"hz": self.hz, "id": str(i+1), "name": Names.names[i]})

    def _stop_thread(self):
        if self.thread is None:
            pass
        else:
            self.thread.stop()
            self.thread.join()

    def _start_thread(self):
        self.thread = CarGenerator(self.cars, self.request)
        self.thread.start()

    def _start(self):
        self._create_cars()
        self._stop_thread()
        self._start_thread()

    def _stop(self):
        self._stop_thread()

    def on_car_number_change(self, value):
        self.numberOfCars = value

    def on_hz_change(self, value):
        self.hz = value

    def on_start(self):
        self._start()

    def on_stop(self):
        self._stop()
