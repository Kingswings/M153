# logger.py
import logging

logging.basicConfig(filename='buchmanager.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger()
