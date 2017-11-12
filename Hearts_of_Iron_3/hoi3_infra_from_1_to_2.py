#hoi3_infra_from_1_to_2.py
#10/8/17 written by and copyright Justin Bourbonniere
'''This program will open all the provinces files and increase infra
from 1 to 2.'''
#reasoning: troops cannot pass infra 1 zones
import os, sys, fileinput, re

'open files and decrease air attack to 0.1'
def openFilesFunc():
    path = r'D:/Python36-32/MyScripts/test2/provinces'
    os.chdir(path)
    text_to_find = 'infra = 1'
    text_to_replace = 'infra = 2'
    for dirpath, dirnames, filenames in os.walk('.'):
        'find the subfolders'
        for dir in dirnames:
            'create path to subfolder'
            sub_path = path+"/"+dir
            os.chdir(sub_path)
            'loops over each file in subfolder'
            for file in os.listdir('.'):
                try:
                    'replaces the text'
                    for line in fileinput.input(file, inplace=True):
                        print line.replace(text_to_find, text_to_replace)
                except:
                    continue


openFilesFunc()
