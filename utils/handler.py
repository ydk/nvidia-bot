from signal import signal, SIGINT
from utils.logger import log

def sig_handler(shutdown, frame):
    log.info("Caught the stop, exiting.")
    exit(0)
