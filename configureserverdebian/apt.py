"""
    My personal config for Ovh vps Debian
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError

ERR_APT_INSTALL = 'Unable to install %s'
ERR_APT_REMOVE = 'Unable to uninstall %s'


class apt:
    def install(self, program):
        """
        Command apt install
        """
        global APTOUTPUT
        try:
            cmd_list = ['apt', 'install', program]
            cmd = Popen(cmd_list)
            cmd.wait
            APTOUTPUT = cmd.communicate()[0]
            self.log.add_log(APTOUTPUT)
        except CalledProcessError:
            self.log.add_log(ERR_APT_INSTALL % program)

    def remove(self, program):
        """
        Command apt install
        """
        global APTOUTPUT
        try:
            cmd_list = ['apt', 'remove', program]
            cmd = Popen(cmd_list)
            cmd.wait
            APTOUTPUT = cmd.communicate()[0]
            self.log.add_log(APTOUTPUT)
        except CalledProcessError:
            self.log.add_log(ERR_APT_REMOVE % program)
