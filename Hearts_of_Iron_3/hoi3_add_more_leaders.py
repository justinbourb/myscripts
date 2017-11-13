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
import os, sys, fileinput, re, string


def source_id_Func(source_id):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\source"
    text_to_search = r"(\d{6} )"


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


def donor_file_Func(source_id):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\donor"
    text_to_search = r"(\d{5,6} )"
    country_name = r"(country = )([A-Z]{3})"
    keys=[]
    values=[]
    source_id=int(source_id)
    source_id+=1
    line_counter=0

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            for line in fileinput.input(file, inplace=True):
                text_to_replace = str(source_id)+" "
                line = re.sub(text_to_search, text_to_replace, line.rstrip())
                print(line)
                line_counter+=1
                '''not 100% accurate but attempts to iterate source_id
                for every match, not every line'''
                if (line_counter % 10 == 0):
                    source_id+=1
                    line_counter=0
            ''' this sounds cool: https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python
            but I'm just going to repeat my code instead. Lazy/Bad_code_warning=True'''



            '''creates a list from the regex matches (leader_id)'
            'from the donor file'
            text_to_find = re.findall(text_to_search, filetext)
            'removes duplicates from the list, sets do not have duplicates'
            text_to_find = list(set(text_to_find))
            'sorts the list, sets are not sorted'
            text_to_find.sort()
            'replaces the matched leader_id with next source_id'
            'TODO: write this to the file somehow?'
            for i,s in enumerate(text_to_find):
                text_to_replace = str(source_id)+" ="
                for line in fileinput.input(file, inplace=True):
                    print line.replace(str(text_to_find[i])+" =",text_to_replace )
                source_id+=1
            'store values for dict creation'
            '''
            keys.append(str(file))
            values.append(text_to_find[1])




        except:
            continue
    'create dictionary to allow backfilling donor files with combined'
    'source file data'
    dictionary = dict(zip(keys, values))
    print(dictionary)
    return ()



source_id=''
source_id=source_id_Func(source_id)
donor_file_Func(source_id)
