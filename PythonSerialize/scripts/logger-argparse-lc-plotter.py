#!/usr/bin/env python

import os
import sys
import yaml
import json
import numpy as np
from matplotlib import pyplot as plt

# Set up our logging. A name is not required but is nice.
import logging
logger = logging.getLogger('planet_plotter')

def main(filename, planet_name=None, overwrite=False):
    logging.debug(f'Entering main')
    
    # Our convenience function (could be loaded rather than copied):
    def load_config(filename):
        logger.debug(f'Loading {filename}')

        with open(filename, 'r') as f:
            my_config = yaml.safe_load(f.read())
            
        return my_config

    # Load our planet info
    planets = load_config(filename)
    
    if planet_name is not None:
        # Check for planet
        if planet_name not in planets:
            logger.warning(f'{planet_name} not in list of planets, exiting.')
            return

        # Otherwise use only that planet
        planets = { planet_name: planets[planet_name] }
    else:
        planet_name = 'All Planets'

    logger.info(f'Making plot for {planet_name}')        
        
    fig, ax = plt.subplots(1)
    fig.set_size_inches(12, 9)

    for name, json_files in planets.items():
        for lc_json_file in json_files:
            logger.debug(f'Getting {lc_json_file} for {name}')
            # Load the json data
            with open(lc_json_file, 'r') as f:
                lc0 = json.loads(f.read())

            ax.plot(np.array(lc0))
            ax.set_title(planet_name)
        
    plot_fn = planet_name.lower().replace(' ', '-')
        
    logger.debug(f'Using {plot_fn}')
    plot_path = f'plots/{plot_fn}-light-curve.png'

    if os.path.exists(plot_path) is False or overwrite is True:
        fig.savefig(plot_path)
        logger.info(f'Plot created for {planet_name} at {plot_path}')
    else:
        logger.warning(f'Plot already exists for {planet_name}, use --overwrite')
        sys.exit(1)

    plt.close(fig)
    
    return plot_fn

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="Make a plot for a planet")
    parser.add_argument('--config', default='planet_config.yaml',
                        help='Config file to use')
    parser.add_argument('--planet-name', help='Planet to plot, otherwise plot all planets')
    parser.add_argument('--overwrite', action='store_true', default=False,
                        help='Overwrite any existing files, default False.')
    # See logging: https://docs.python.org/3.7/howto/logging.html#logging-advanced-tutorial
    parser.add_argument('--log-level', default='info', help='Log level, default INFO')

    # Load the arguments
    args = parser.parse_args()

    log_levels = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
    }
    
    logger.setLevel(log_levels[args.log_level])
    
    if not os.path.exists(args.config):
        logger.warning("Config file does not exist:", args.config)

    planet_name = main(
            filename=args.config,
            planet_name=args.planet_name,
            overwrite=args.overwrite,
            )
    
    if planet_name is not None:
        logger.info(f"Done making plot for {planet_name}")
