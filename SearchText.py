#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to search text in a folder."
__author__ = "LionNBean"

import glob, os

class List_all_files():

    def __init__(self):
        self._files = []
        self._sentence = []
        self._count = 0
        self._text = ''
        self.get_files()
        self._lan = 'en'

    @property
    def lan(self):
        return self._lan
    
    @lan.setter
    def lan(self, value):
        self._lan = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def get_files(self):
        for each in glob.glob('*'):
            dir = os.path.abspath(each)
            self.get_files_in_dir(dir)

    def get_files_in_dir(self, dir):
        if os.path.isfile(dir):
            if dir.split('.')[-1] in ['md']:
                self._files.append(dir)
            return
        else:
            for each in glob.glob(os.path.join(dir,"*")):
                self.get_files_in_dir(each)

    def search_text(self, text_value = ''):
        if text_value == '': text_value = self._text
        for each_file in self._files:
            with open(each_file, 'r', encoding='UTF-8') as f:
                if self._lan == 'en': split_str = '.'
                else: split_str = '，'
                file_text = f.read().replace('\n', split_str)
                sentences = file_text.split(split_str) 
                for each_sentence in sentences:
                    if text_value in each_sentence: 
                        self._count += 1
                        self._sentence.append([self._count, each_file, each_sentence])

    def print_result(self):
        print('The result of %s is :\n'% self._text)
        for each in self._sentence:
            print("{0:0>3d}:  {1}\n        {2}\n".format(*each))


if __name__=="__main__":
    
    l = List_all_files()
    l.lan = input('zh or en ? (zh)')
    l.text = input('输入搜索词：')
    l.search_text()
    l.print_result()

    quit = input('Press any button to quit.')
