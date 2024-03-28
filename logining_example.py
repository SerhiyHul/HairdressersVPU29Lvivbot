import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG

)

logging.debug('Debug massage')
logging.info('info massage')
logging.warning('warning massage')
logging.error('error massage')
logging.critical('critical massage')