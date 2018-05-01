# python
# -*- coding:UTF-8 -*-
import logging
import logging.config

logging.config.fileConfig('logging.conf')

logging.debug('debug message')
logging.info('info message')
logging.warn('warning message')
logging.error('error message')
logging.critical('critical message')
