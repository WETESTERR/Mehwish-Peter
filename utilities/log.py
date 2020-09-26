import logging
import os

import config

class Logger:


    def create_logs(self):
        logger = logging.getLogger(__name__)
          #file handler is an other class which needs to be pass in addhandler method
        #filehandler is used for file location

        if not os.path.exists(config.logs_path):
            os.mkdir(config.logs_path)
        #Get current working directory ==> I have to run in parent directory
        #Method to create logs directory

        logfile = logging.FileHandler(config.logs_path+'/testlogs.log')
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


#l = Logger() for debugging
#l.create_logs()