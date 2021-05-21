import inspect
import logging


class LogGen:
    @staticmethod
    def logGen():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # c_handler = logging.StreamHandler()
        f_Handler = logging.FileHandler('automation.log')

        # c_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        f_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                                        datefmt="%m/%d/%Y %I:%M:%S %p")

        # c_handler.setFormatter(c_formatter)
        f_Handler.setFormatter(f_formatter)

        # logger.addHandler(c_handler)
        logger.addHandler(f_Handler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger
