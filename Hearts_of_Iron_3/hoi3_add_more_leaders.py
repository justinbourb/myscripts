#hoi3_add_more_leaders.py
#11/5/17 written by and copyright Justin Bourbonniere
'''This program will open the files, find all the leader_ids (from donor files)
based on regex match and change the number to follow receipient file
fformat'''
#reasoning: makes the file structure more organized and easier to find
#each coutries territories
import os, sys, fileinput, re




def openFilesFunc():
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test"
    text_to_search = r"(\d{6})"
    #text_to_search = r'(.*)'
    leader_id_list = []
    

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'find regex match (leader_id)'
            match = re.findall(text_to_search, filetext)
            'create a list of all leader ids to find max # +1 this'
            'number for additional entries'
            for i in match:
                leader_id_list.append(i)
        except:
            continue
        print("This file:",file,"contains these leader_ids:",leader_id_list[-1:])

openFilesFunc()
