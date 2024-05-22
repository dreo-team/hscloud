"""hscloud setup script."""

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'hscloud',
    packages = ['hscloud'],
    include_package_data=True,
    version = '1.0.0',
    license='MIT',
    description = 'Library to login to Dreo cloud and get device info.',
    author = 'Kane Wang',
    author_email = 'app@hesung.com',
    url = 'https://github.com/dreo-team/hscloud',
    download_url = 'https://github.com/dreo-team/hscloud/dist/hscloud-1.0.0.tar.gz',
    install_requires=[
        'requests',
        'tzlocal',
        'click',
        'pycryptodome'
    ],
    entry_points='''
        [console_scripts]
        micloud=micloud.cli:cli
    ''',
)