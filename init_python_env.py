# -*- coding: utf-8 -*-

import os

login_name = "root"
user_name = "zouyingjie"

os.mkdir("/home/zouyingjie/source_code")
os.system("cd /home/zouyingjie/source_code")
os.system("wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz")
os.system("tar -zxvf Python-3.6.2.tgz")
os.system("cd Python-3.6.2")
os.system("./configure --prefix=/usr/local/ --enable-shared")
os.system("make and make install")


