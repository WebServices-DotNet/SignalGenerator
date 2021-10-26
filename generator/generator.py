from generator.car_generator import CarGenerator


class GeneratorManager:

    def __init__(self):
        self.hz = 0.2
        self.numberOfCars = 2
        self.thread = None
        self._create_cars()

    def _create_cars(self):
        self.cars = []
        for i in range(self.numberOfCars):
            self.cars.append({"hz": self.hz, "id": i + 1})

    def _stop_thread(self):
        if self.thread is None:
            pass
        else:
            self.thread.stop()
            self.thread.join()

    def _start_thread(self):
        self.thread = CarGenerator(self.cars)
        self.thread.start()

    def _start(self):
        self._create_cars()
        self._stop_thread()
        self._start_thread()

    def _stop(self):
        self._start_thread()

    def on_car_number_change(self, value):
        self.numberOfCars = 2
        print("change number of cars")

    def on_hz_change(self, value):
        self.hz = 0.1
        print("change signal hz")

    def on_start(self):
        self._start()

    def on_stop(self):
        self._stop()
