"""
    My personal config for Ovh vps Debian
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError
import crypt


class useradd:
    def __init__(self, username, password, log):
        self.username = username
        self.password = crypt.crypt(password, "22")
        self.log = log

    def cmd(self):
        """
        Command useradd
        """
        global USERADDOUTPUT
        try:
            cmd_list = ['useradd', '-p', self.password, self.useradd]
            cmd = Popen(cmd_list)
            cmd.wait
            USERADDOUTPUT = cmd.communicate()[0]
            self.log.add_log(USERADDOUTPUT)
        except CalledProcessError:
            # self.log.add_log(const.ERR_USERADD)
            #
            self.log.add_log('error msg')  # to do with user name
