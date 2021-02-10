#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to rename my roms."
__author__ = "LionNBean"

import os, glob, sys, shutil, stat, zipfile
from unrar import rarfile

class roms():

    def __init__(self):
        self._include_dir = False
        self._files = []
        self.get_files_in_dir(os.path.split(os.path.abspath(sys.argv[0]))[0], True)

    def get_files_in_dir(self, dir_value, include_dir_value):
        if os.path.isfile(dir_value):
            #if dir_value.split('.')[-1] in ['lnx', 'rar', 'RAR', 'zip', 'ZIP']:
            self._files.append(dir_value)
            return
        else:
            if include_dir_value == True:
                for each in glob.glob(os.path.join(dir_value,"*")):
                    self.get_files_in_dir(each, self._include_dir)

    def unzip_rename(self):
        for each in self._files[:]:
            if '.py' not in each and 'Hack ' not in each and 'Demo ' not in each:
                path, rom_full_name = os.path.split(each)
                rom_ext= rom_full_name.split('.')[-1]
                if rom_ext in ['rar', 'RAR', 'zip', 'ZIP']:
                    new_path = (each.replace('_', ' ').split('.' + rom_ext)[0].split('(')[0]).rstrip()
                    if not os.path.isdir(new_path):
                        os.mkdir(new_path)
                    if rom_ext in ['rar', 'RAR']:
                        z = rarfile.RarFile(each)
                        z.extractall(new_path)
                    elif rom_ext in ['zip', 'ZIP']:
                        z = zipfile.ZipFile(each, 'r')
                        z.extractall(new_path)
                        z.close()
                    try:
                        os.remove(each)
                    except PermissionError:
                        os.chmod(each, stat.S_IWRITE)
                        os.remove(each)  
                    self._files.remove(each)       

    def move(self):
        for each in self._files[:]:
            if '.py' not in each and 'Hack ' not in each and 'Demo ' not in each:
                path, rom_full_name = os.path.split(each)
                rom_ext= rom_full_name.split('.')[-1]
                new_path = each.replace('_', ' ').split('.' + rom_ext)[0].split('(')[0].rstrip()
                if not os.path.isdir(new_path):
                    os.mkdir(new_path)
                shutil.move(each, os.path.join(new_path, rom_full_name))

if __name__=="__main__":

    r = roms()
    r.unzip_rename()
    r.move()

    quit = input('\nPress Enter to quit.\n')