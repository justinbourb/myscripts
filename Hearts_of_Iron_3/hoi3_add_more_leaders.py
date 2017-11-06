#hoi3_add_more_leaders.py
#11/5/17 written by and copyright Justin Bourbonniere
'''This program will:
1)open the "source" file and find the next leader_id to us and
the "source" file country name
2) Open all the files in the "donor" directory.  Find and replace
their leader id #'s with the next leader_id number (next leader_id number
incremented +1 each time).  It will also update the country name from
whatever it is to the source country name.
3) It will append the updated donor file to the source file, thus adding
more leaders to the source file (objective of the program).'''
#reasoning: Major nations have upto 900 leaders.  Minor nations have 10-60.
#I would like to combine minor nation leader lists of countries with
#similar leader naming conventions to increase the number of minor nation
#leaders without giving the nations leaders which are too powerful/skilled.
#I prefer this method to just creating new leader from scratch.  I don't want
#to create new names (need name generator) and I don't want to make leaders
#which are overpowered / too powerful / too skilled which seems likely to
#happen.  Though perhaps random leader generator is a better approach.
import os, sys, fileinput, re


def source_id_Func(source_id):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\source"
    text_to_search = r"(\d{6})"

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'find regex match (leader_id)'
            match = re.findall(text_to_search, filetext)
            'returns last leader_id in source file'
            'can +1 this number to add new leaders'
            source_id = match[-1]
        except:
                continue
    return (source_id)


def leader_id_list_Func(leader_id_list):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\donor"
    text_to_search = r"(\d{5,6})"
    total=[]
    

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'creates a list from the regex matches (leader_id)'
            'from the donor file'
            leader_id_list = re.findall(text_to_search, filetext)
            'removes duplicates from the list, sets do not have duplicates'
            leader_id_list = list(set(leader_id_list))
            'sorts the list, sets are not sorted'
            leader_id_list.sort()
            print(file,":",len(leader_id_list))
        except:
            continue
    return (leader_id_list)



source_id=''
source_id=source_id_Func(source_id)
print(source_id)
leader_id_list=[]
leader_id_list=leader_id_list_Func(leader_id_list)
print(leader_id_list)
