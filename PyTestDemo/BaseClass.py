import inspect
import logging


class BaseClass:
    def test_loggingDemo(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logdata.log')
        formatter = logging.Formatter(
            " %(asctime)s : %(levelname)s : %(name)s : %(message)s ")  # format we used in file to show the logs
        fileHandler.setFormatter(formatter)  # building connection between formatter and logger
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)  # help to see specific logs
        return logger
