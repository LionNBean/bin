#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to show document struction."
__author__ = "LionNBean"

import glob, os


class Doc_struction():

    def __init__(self):
        self._doc_struct = []
        self._dir =''
        self._stack = 0
    
    def get_dirs(self, dir_value = ''):
        self._files = glob.glob(os.path.join(dir_value,'*'))
        for each in self._files[:]:
            if os.path.isdir(each):
                self._doc_struct.append([self._stack, each, each.split('/')[-1].split('\\')[-1]])
                self._stack += 1
                self.get_dirs(each)
                self._stack -= 1

    def output_profile(self):
        with open('Struct.txt', 'w') as f:
            f.write('The struction of this dir is: \n')
            for each in self._doc_struct:
                if each[0] < 4:
                    f.write(each[0] * '  '+each[2]+'\n')


if __name__=="__main__":

    ds = Doc_struction()
    ds.get_dirs()
    ds.output_profile()

    quit = input('\nPress any button to quit.\n')