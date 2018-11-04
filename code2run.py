import time
from colorama import Fore, Back, Style
import logging


logging.basicConfig(filename='code2run.log',filemode='w', level=logging.INFO)
logger = logging.getLogger()
# logger.info('This is the new code')
# logger.info('<div class="ui segment blue inverted">Starting</div>')
# for x in range(10):
#             time.sleep(0.1)
#             logger.info('code2run - this is '+str(x))
#             if x%2==0:
#                 logger.info('this is an even number')
#             else:
#                 logger.info('this is an Odd number')
# logger.info('<div class="ui segment red inverted">Finished</div>')




#TESTING SOME NEW CODE
import datetime
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
logger.info(st)
logger.info('this should have printed the time the code was ran..is it  right?')
logger.info('I have zipped the file ABC to folder ./delivery')
logger.warning('<div class="ui teal label inverted basic">this is a test dont panic!</div>')
logger.error('<div class="ui red label inverted basic">this is a test dont panic - but it is an error!</div>')


         