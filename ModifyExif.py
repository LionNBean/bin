#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to modify the exif of a photo."
__author__ = "LionNBean"

import glob, os, pyexiv2, re

class ModifyExif():

    def __init__(self):
        self._include_dir = True
        self._files = []
        self.get_files_in_dir(os.getcwd(), True)

    def get_files_in_dir(self, dir_value, include_dir):
        if os.path.isfile(dir_value):
            if dir_value.split('.')[-1] in ['jpg', 'png']:
                self._files.append(dir_value)
            return
        else:
            if include_dir == True:
                for each in glob.glob(os.path.join(dir_value,"*")):
                    self.get_files_in_dir(each, self._include_dir)

    def modify_by_LNB_format(self):
        for each in self._files:
            pic_full_name = each.split('/')[-1].split('\\')[-1]
            pic_name = pic_full_name.split('.')[0] 
            if re.match(r'^\d{11}', pic_name):
                try:
                    with pyexiv2.Image(each) as img:
                        origin_exif = img.read_exif()
#                        for item in ['Exif.Photo.DateTimeDigitized', 'Exif.Photo.DateTimeOriginal', 'Exif.Image.DateTime']:
                        for item in ['Exif.Photo.DateTimeOriginal']:
                            img.modify_exif({item:pic_name[:4]
                            + ':' + pic_name[4:6] + ':' + pic_name[6:8]
                            + origin_exif[item][10:]})
                except: print('There is something wrong with', pic_full_name)

if __name__=="__main__":
    
    me = ModifyExif()
    me.modify_by_LNB_format()

    quit = input('\nPress Enter to quit.\n')

    
    
    