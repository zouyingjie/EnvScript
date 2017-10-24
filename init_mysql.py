# -*- coding: utf-8 -*-

import os

# os.system("wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz")
# os.system("tar -zxvf mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz")
# os.system("mv mysql-5.7.20-linux-glibc2.12-x86_64 /usr/local/mysql")
#
# os.system("yum install libaio")
# os.system("groupadd mysql")
# os.system("useradd -r -g mysql -s /bin/false mysql")
os.system("cd /usr/local/mysql")
os.system("mkdir mysql-files")
os.system("chmod 750 mysql-files")
os.system("chown -R mysql .")
os.system("chgrp -R mysql .")
os.system("bin/mysqld --initialize --user=mysql")
os.system("bin/mysql_ssl_rsa_setup  ")
os.system("chown -R root .")
os.system("chown -R mysql data mysql-files")
os.system("bin/mysqld_safe --user=mysql &")
