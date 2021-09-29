#!/usr/bin/env python3

from setuptools import setup

setup(
    name='pca9685',
    version='0.0.1',
    description='pca9685 driver',
    author='Blue Robotics',
    url='https://github.com/bluerobotics/pca9685-python',
    packages=['pca9685'],
    install_requires=[
        'RPi.GPIO',
        'smbus2',
    ],
)
