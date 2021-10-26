from datetime import datetime


class GeneratorLogger:

    def log(self, id, signal_name, value):
        print(str(datetime.now()) + " Signal: " + str(signal_name) + " val: " + str(value) + " id: " + str(id))