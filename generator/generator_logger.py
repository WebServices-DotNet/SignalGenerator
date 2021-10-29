from datetime import datetime


class GeneratorLogger:

    def log(self, data):
        print(str(datetime.now()) + str(data))