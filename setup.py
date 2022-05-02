from setuptools import setup

import nymeria

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='nymeria',
    version=nymeria.__version__,
    description='Discover contact details such as phone numbers, email addresses and social links using Nymeria\'s service.',
    url='https://git.nymeria.io/nymeria.py',
    author=nymeria.__author__,
    author_email='dev@nymeria.io',
    license='MIT',
    packages=['nymeria'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
