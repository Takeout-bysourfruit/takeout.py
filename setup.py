from setuptools import setup, find_packages

VERSION = '1.3.1'
DESCRIPTION = 'A Takeout client for Python.'
LONG_DESCRIPTION = "Takeout.py is an API wrapper for Takeout's API. See more information at https://github.com/Takeout-bysourfruit/takeout.py"

setup(
    name="takeout.py",
    version=VERSION,
    author="Takeout by Sourfruit",
    author_email="<hello@def-not-hacking-the.net>",
    url="https://github.com/Takeout-bysourfruit/takeout.py",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'certifi'],
    keywords=['python', 'takeout.py', 'takeout', 'sourfruit'],
)

# python3 setup.py sdist bdist_wheel
# twine upload dist/*