from setuptools import setup, find_packages

VERSION = '1.2.0'
DESCRIPTION = 'A Takeout client for Python.'
LONG_DESCRIPTION = "Takeout.py is an API wrapper for Takeout's API. See more information at https://github.com/Takeout-bysourfruit/takeout.py"

setup(
    name="takeout.py",
    version=VERSION,
    author="Takeout by Sourfruit",
    author_email="<hello@def-not-hacking-the.net>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'certifi'],
    keywords=['python', 'takeout.py', 'takeout', 'sourfruit'],
)