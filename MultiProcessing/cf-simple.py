#!/usr/bin/env python3

import concurrent.futures
from logbook import Logger, StreamHandler
from logbook.more import ColorizedStderrHandler
import time

log_handler = ColorizedStderrHandler()

logger = Logger('mp-example')

# Important scientific data
data = (
    # name, wait_time
    ['a', '10'], 
    ['b', '10'], 
    ['c', '5'], 
    ['d', '5'],
    ['e', '1'], 
    ['f', '3'], 
    ['g', '5'], 
    ['h', '7']
)

def mp_worker(input_data):
    """The worker
    
    This represents either a CPU or an IO bound process. 
    Here we simulate that by simply waiting for the desired
    amount of time.
    
    Note that we accept a single list of arguments and need to unpack them.
    """
    # Unpack our arguments.
    name, wait_time = input_data
    
    logger.info(f"Starting {name} \t Waiting {wait_time}s seconds to mark complete")
    
    # SCIENCE GOES HERE!
    time.sleep(int(wait_time))
    
    logger.critical(f"\t Finished inside {name}")

    return name, wait_time


def main(num_processes=2):
    """
    """
    logger.notice('Starting pool')

    with concurrent.futures.ProcessPoolExecutor(num_processes) as executor:
        for name, wait_time in executor.map(mp_worker, data):
            logger.info(f"Totally finished {name} in {wait_time}s")
    
    logger.info('All done!')

    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Run some multiprocessing")
    parser.add_argument('--pool-size', default=2, type=int, help='Number of processes')    
    
    # Load the arguments.
    args = parser.parse_args()    
    
    # Call our main function.
    with log_handler.applicationbound():
        main(num_processes=args.pool_size)
