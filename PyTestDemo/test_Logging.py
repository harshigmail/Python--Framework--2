import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler(
        'logdetails.log')  # filehandler object , we need to show below logs in somewhere so we used file to show these logs
    formatter = logging.Formatter(
        " %(asctime)s : %(levelname)s : %(name)s : %(message)s ")  # format we used in file to show the logs
    fileHandler.setFormatter(formatter)  # building connection between formatter and logger
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)  # help to see specific logs
    logger.debug("print message")
    logger.info("info statements")
    logger.warning("warning message")
    logger.error("A major error")
    logger.critical("")
