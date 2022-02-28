import logging


def log_to_file(level, message):
    logging.basicConfig(filename='app.log', filemode='a+', format='%(levelname)s - %(message)s', level=logging.DEBUG)
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.warning(message)
