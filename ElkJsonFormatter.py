import logging
import logging.config
from pythonjsonlogger import jsonlogger
import ecs_logging
from datetime import datetime


class ElkJsonFormatter(jsonlogger.JsonFormatter):

    def __init__(self):
        self._log_format = ecs_logging.StdlibFormatter()

    def get_file_handler(self):
        file_handler = logging.FileHandler('logs2.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self._log_format)
        return file_handler

    def get_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(self._log_format)
        return stream_handler

    def get_logger(self):
        logging.basicConfig(level="INFO")
        logging.info("Creating handler")
        logger = logging.getLogger()
        logger.addHandler(self.get_file_handler())
        logger.addHandler(self.get_stream_handler())
        return logger


