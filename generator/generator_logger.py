
class GeneratorLogger:

    def log(self, id, signal_name, value):
        print("Signal: " + str(signal_name) + " val: " + str(value) + " id: " + str(id))