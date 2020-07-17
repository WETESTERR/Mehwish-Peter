import logging

import os

class Loggs:

    def loggers(self):
        logger = logging.getLogger(__name__)
        #file handler is an other class which needs to be pass in addhandler method
        #filehandler is used for file location
        directory = "C:\\Users\\AY54109\\Desktop\\Automation.project\\Mehwish-Peter\\utilities"
        os.mkdir("logfile.log")

        if not os.path.exists(directory):
            os.mkdir(directory)


        logfile = logging.FileHandler('testlogs.log')
        stream_handler = logging.StreamHandler()
        logger.addHandler(logfile)
        logger.addHandler(stream_handler)


        logformat = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        logfile.setFormatter(logformat)

        logger.info("Check the minior issues in your code")
        logger.debug("Code check Debug")
        logger.warning("The issue needs to resolve as soon as posible")
        logger.critical("The issue  is severe and need to fixed")
        logger.error("An Error")



        "Mehwish Peter Testing for Remi For Finniar"