import argparse
import logging
import logging.config
from src.exceptions import HostExceptions


# logger = logging.getLogger(__name__)

# Define Logger
def get_logger():
    log_config = 'lib/configs/logging.conf'
    # log_config = 'lib/configs/logging.yml'
    logging.config.fileConfig(log_config)
    # log = logging.getLogger(__name__)
    

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='pinger')
    # Add some arguments
    parser.add_argument('-f', '--file', dest='host_file', help='A file containing the hosts which to execute against.')
    # parser.add_argument()
    return parser.parse_args()

def get_hosts(passed_file):
    hosts = None

    if not passed_file:
        raise HostExceptions.MissingHostsException()
    with open(passed_file, 'r') as input_file:
        hosts = input_file.readlines()
        hosts = [h.strip() for h in hosts]
    # Should the file size be checked instead?
    if not hosts:
        raise HostExceptions.MissingHostsException('The hosts file passed appears to be empty!')
    return hosts


if __name__ == '__main__':
    # instantiate the logger
    get_logger()
    logger = logging.getLogger('main')
    # get the arguments
    pargs = get_args()
    get_hosts(pargs.host_file)
    pass
