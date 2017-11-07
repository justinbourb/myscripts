#hoi3_organize_provinces.py
#11/5/17 written by and copyright Justin Bourbonniere
'''This program will open the files and move them from the 'asia' folder
to a folder based on the owner name (country name)'''
#reasoning: makes the file structure more organized and easier to find
#each coutries territories
import os, sys, fileinput, re




def openFilesFunc():
    'path and regex definitions'
    path_to_search = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron 3\history\provinces\asia"
    text_to_search = r"(owner = )(\D{3})?"
    path_to_move = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron 3\history\provinces"

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'find regex match (country name)'
            match = re.search(text_to_search, filetext)
            country = str(match[2])
            'if the path_to_move+country dir does not exist, make it'
            'Then move the corresponding file to the new dir'
            try:
                if not os.path.exists(path_to_move+country):
                    os.makedirs(path_to_move+country)
                print('moving from:',os.path.join(path_to_search,file))
                print('moving to:',os.path.join(path_to_move,country,file))
                os.rename(os.path.join(path_to_search,file), os.path.join(path_to_move,country,file))
            except:
                continue
        except:
            continue


openFilesFunc()
