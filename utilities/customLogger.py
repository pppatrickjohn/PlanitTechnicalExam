import logging

class logGeneration:
    @staticmethod
    def logGen():
        logging.basicConfig(filename=".\\Logs.\\TestExecution.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger