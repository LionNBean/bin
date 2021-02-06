#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to show the python version"
__author__ = "LionNBean"

import sys, os, platform, getpass, site


class Sys_info():

    def __init__(self):
        self._os_type_explain = '操作系统类型'
        self._os_platform_explain = '操作系统标识'
        self._os_name_explain = '操作系统名称'
        self._os_release_explain = '操作系统版本'
        self._user_name_explain = '当前用户名'
        self._user_passwd_explain = '当前用户密码'
        self._user_gid_explain = '当前进程组ID'
        self._python_version_explain = 'Python版本'
        self._python_sitepackage_explain = 'Python sitepackage位置'

    @property
    def os_type(self):
        self._os_type =  os.name
        return self._os_type

    @property
    def os_platform(self):
        self._os_platform =  sys.platform
        return self._os_platform

    @property
    def os_name(self):
        self._os_name = platform.system()
        return self._os_name

    @property
    def os_release(self):
        self._os_release = platform.release()
        return self._os_release

    @property
    def user_name(self):
        self._user_name = getpass.getuser()
        return self._user_name

    @property
    def user_passwd(self):
        self._user_passwd = getpass.getpass()
        return self._user_passwd
    
    # @property
    # def user_gid(self):
    #     self._user_gid = os.getgid()
    #     return self._user_gid

    @property
    def python_version(self):
        self._python_version = sys.version
        return self._python_version

    @property
    def python_sitepackage(self):
        self._python_sitepackage = site.getsitepackages
        return self._python_sitepackage()

    def print_all(self):
        print('\n',
        self._os_type_explain, self.os_type, '\n',
        self._os_platform_explain, self.os_platform, '\n',
        self._os_name_explain, self.os_name, '\n',
        self._os_release_explain, self.os_release, '\n',
        self._user_name_explain, self.user_name, '\n',
        self._user_passwd_explain, self.user_passwd, '\n',
#       self._user_gid_explain, self.user_gid, '\n',
        self._python_version_explain, self.python_version, '\n',
        self._python_sitepackage_explain, self.python_sitepackage, '\n',
        end=''
        )
    
if __name__=="__main__":
    sys_info = Sys_info()
    if len(sys.argv) == 1:
        sys_info.print_all()
    else:
        for item in sys.argv[1:]:
            print(item, getattr(sys_info, item),'\n')
            
    quit = input("\nPress any button to quit.\n")
