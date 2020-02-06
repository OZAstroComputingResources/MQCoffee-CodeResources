#!/usr/bin/env python3

from logbook import Logger, StreamHandler
from logbook.more import ColorizedStderrHandler

log_handler = ColorizedStderrHandler()

import multiprocessing
import time

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
    
    logger.critical(f"\t Finished {name}")

    
def main(num_processes=2):
    """
    """
    logger.notice('Starting pool')
    
    # Create the pool.
    p = multiprocessing.Pool(int(num_processes))
    
    # Map each argument to a separate worker.
    p.map(mp_worker, data)
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