from setuptools import setup, find_packages

setup(
    name = "greengraph",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['numpy', 'io', 'matplotlib', 'requests', 'geopy', 'argparse', 'setuptools']
)