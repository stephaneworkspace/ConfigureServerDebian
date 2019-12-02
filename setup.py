"""
    My personal config for Ovh vps Debian
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


GNU = 'GNU Lesser General Public License v3 or later (LGPLv3+)'

setup(
    name='configureserverdebian',
    version='0.0.1',
    description='Configure a debian server',
    long_description=(read('README.rst')),
    url='https://github.com/stephaneworkspace/ConfigureServerDebian.git',
    author='Stéphane Bressani',
    author_email='s.bressani@bluewin.ch',
    license='GPLv3+',
    packages=find_packages(include=['configureserverdebian',
                                    'configureserverdebian.*']),
    install_requires=[
        'toml==0.10.0'
    ],
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ' + GNU,
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ],
)
