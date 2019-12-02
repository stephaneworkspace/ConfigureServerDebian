#!/usr/bin/env python3
"""
    My personal config for Ovh vps Debian
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
# import os
# from subprocess import CalledProcessError
# from . import const
from . import apt


class main:
    def run(self):
        """
        Run configuration
        """
    def sudo_run_1(self):
        """
        Run first part in sudo
        Installation of:
            - mc
        """
        a = apt()
        a.install('mc')
        a.install('curl')
        a.install('python-pip')
        a.install('python3-pip')
        a.remove('vim-tiny')
        a.install('vim')
        a.install('vim-nox')
        a.install('exuberant-ctags')
        a.install('powerline')
        a.install('fonts-powerline')
        a.install('neofetch')
        a.install('build-essential')
        a.install('cmake')
        a.install('python3-dev')
