"""
    My personal config for Ovh vps Debian
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import crypt

password = "p@ssw0rd"
encPass = crypt.crypt(password, "22")
"""useradd -p "+encPass+" johnsmith"""
