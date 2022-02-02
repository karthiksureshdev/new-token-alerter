import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)


class LoggingHandler:
    def __init__(self, *args, **kwargs):
        self.log: logging.Logger = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.INFO)
