#bulk_create_tiff_from_svs.py
#10/11/17 written by and copyright Justin Bourbonniere
'''This program will open the files and convert them from .svs to .tiff files
using the openslide-python module'''
#reasoning: need tiff files for thumbnails, svs files are too large
import os, re, openslide


'open files create thumbnails'
def openFilesFunc():
    #os.chdir(r'I:\images\need_qc\need_recuts\need_recuts_archive')
    os.chdir(r'D:\Python36-32\Myscripts\test')
    for file in os.listdir('.'):
        try:
            openslide.OpenSlide(file).get_thumbnail(5000,5000)
        except:
            continue


openFilesFunc()
