#!/usr/bin/env python

import yaml
import json
import numpy as np
from matplotlib import pyplot as plt

planet_config = 'planet_config.yaml'
planet_name = 'Bob'

# Our convenience function (could be loaded rather than copied):
def load_config(filename):
    with open(filename, 'r') as f:
        my_config = yaml.safe_load(f.read())
        
    return my_config

# Load our planet info
planets = load_config(planet_config)

fig, ax = plt.subplots(1)
fig.set_size_inches(12, 9)

for lc_json_file in planets[planet_name]:
    # Load the json data
    with open(lc_json_file, 'r') as f:
        lc0 = json.loads(f.read())
            
    ax.plot(np.array(lc0))
    ax.set_title(planet_name)
    
fig.savefig(f'plots/{planet_name.lower()}-light-curve.png')
plt.close(fig)
