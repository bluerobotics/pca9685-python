#!/usr/bin/python3

import argparse
from pca9685 import PCA9685

parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group(required=True)
group1.add_argument('--get', action='store', nargs='+', type=int)
group1.add_argument('--set', action='store', nargs='+', type=int)
group1.add_argument('--frequency', action='store', type=int, default=250)
args = parser.parse_args()

pca = PCA9685()
pca.set_pwm_frequency(args.frequency)
pca.output_enable()

if args.get:
    for channel in args.get:
        print(f'channel {channel} pwm: {pca.pwm[channel]}') 
else:
    for channel in args.set[:-1]:
        pca.pwm[channel] = args.set[-1]
