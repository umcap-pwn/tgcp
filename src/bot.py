import utils
import monitor
import logging


#Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,  
    format='[%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler()]  
)

