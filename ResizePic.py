#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to resize pictures."
__author__ = "LionNBean"

import glob, os
from PIL import Image

class WrappedImage():

    def __init__(self):
        self._files = []
        self.get_files_in_dir(os.getcwd())

    def get_files_in_dir(self, dir):
        if os.path.isfile(dir):
            if dir.split('.')[-1] in ['jpg', 'png']:
                self._files.append(dir)
            return
        else:
            for each in glob.glob(os.path.join(dir,"*")):
                self.get_files_in_dir(each)

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width_value):
        self._width = width_value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height_value):
        self._height = height_value

    def resize_image(self):
        if self._files == []:
            print('\nThere is no pics here.\n')
        else:
            try:
                os.mkdir('output')
            finally:
                self._width, self._height = tuple(map(int, input('w,h\n').split(',')))
                for each in self._files:
                    pic_full_name =  each.split('/')[-1].split('\\')[-1]
                    pic_name = pic_full_name.split('.')[0] 
                    pic_format = pic_full_name.split('.')[-1] 
                    im = Image.open(each)
                    im.thumbnail((self._width, self._height))
                    im.save(os.path.join('output', pic_name + '.png'), 'png')

if __name__=="__main__":
    
    im = WrappedImage()
    im.resize_image()

    quit = input('\nPress Enter to quit.\n')