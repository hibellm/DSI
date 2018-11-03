import time
from colorama import Fore, Back, Style
import logging


logging.basicConfig(filename='code2run.log',level=logging.INFO)
logger = logging.getLogger()
logger.info('mjh')
logger.info('<div class="ui segment green inverted">Starting</div>')
for x in range(10):
            time.sleep(0.1)
            logger.info('code2run - this is '+str(x))
            if x%2==0:
                logger.info('this is an even number')
            else:
                logger.info('this is an Odd number')
logger.info('<div class="ui segment green inverted">Finished</div>')

         