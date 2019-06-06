#!/usr/bin/env python

import os
import yaml
import json
import numpy as np
from matplotlib import pyplot as plt

def main(filename, planet_name, overwrite=False, verbose=False):
    if verbose:
        print(f'Making plot for {planet_name}')

    # Our convenience function (could be loaded rather than copied):
    def load_config(filename):
        if verbose:
            print(f'Loading {filename}')

        with open(filename, 'r') as f:
            my_config = yaml.safe_load(f.read())
            
        return my_config

    # Load our planet info
    planets = load_config(filename)

    fig, ax = plt.subplots(1)
    fig.set_size_inches(12, 9)

    for lc_json_file in planets[planet_name]:
        # Load the json data
        with open(lc_json_file, 'r') as f:
            lc0 = json.loads(f.read())
                
        ax.plot(np.array(lc0))
        ax.set_title(planet_name)
        
    plot_filename = f'plots/{planet_name.lower()}-light-curve.png'

    if os.path.exists(plot_filename) is False or overwrite is True:
        fig.savefig(plot_filename)
        if verbose:
            print(f'Plot created for {planet_name} at {plot_filename}')
    else:
        print(f'Plot already exists for {planet_name}, use --overwrite')

    plt.close(fig)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="Make a plot for a planet")
    parser.add_argument('--config', default='planet_config.yaml',
                        help='Config file to use')
    parser.add_argument('--planet-name', required=True,
                        help='Planet to plot')
    parser.add_argument('--overwrite', action='store_true', default=False,
                        help='Overwrite any existing files, default False.')
    parser.add_argument('--verbose', action='store_true', default=False, help='Verbose.')

    # Load the arguments
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print("Config file does not exist:", args.config)

    clean_dir = main(
            filename=args.config,
            planet_name=args.planet_name,
            overwrite=args.overwrite,
            verbose=args.verbose
            )
    if args.verbose:
        print("Done making plot for", args.planet_name)
