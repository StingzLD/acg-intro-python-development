# This will call the setuptools module, then import the setup and find_packages
# functions from it
from setuptools import setup, find_packages

# This will read the package description from our README.rst file
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

# This will actually do the calling out to setup, and set some of the information
# about the package itself
setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Your Name',
    author_email='youremail@example.com',
    packages=find_packages('1'),
    package_dir={'': '1'},
    install_requires=[],

    # This is essentially saying:
    # When you are installed, create an executable named hr,
    # that will call the "main" method inside the "cli" module,
    # inside of the "hr" package.
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
