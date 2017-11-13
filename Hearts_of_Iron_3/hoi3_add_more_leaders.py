#hoi3_add_more_leaders.py
#11/5/17 written by and copyright Justin Bourbonniere
'''This program will:
1)open the "source" file and find the next leader_id to use and
the "source" file country name
2) Open all the files in the "donor" directory.  Find and replace
their leader id #'s with the next leader_id number (next leader_id number
incremented +1 each time).  It will also update the country name from
whatever it is to the source country name.
3) It will append the updated donor file to the source file, thus adding
more leaders to the source file (objective of the program).
4) Optional objective: backfill the donor files with the updated source file content
but change the leader id's and country name to the donor file format.
TODO: make a dictionary to contain donor file: leader_id.  Can find both
leader_id and country name (from file name) with this information.'''
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

        except:
            continue
    for file in os.listdir('.'):
        try:
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            for line in fileinput.input(file, inplace=True):
                line = re.sub(country_name, "country = PER", line.rstrip())
                print(line)
                line_counter+=1
        except:
            continue
        '''I think I should refactor this into it's own function.
        for file in os.listdir down to except : continue
        should be a new function called text_replace_Func()
        This function takes two arguements (text_to_search, text_to_replace)
        How do I handle the interation of source_id I I make a function that does not
        include this??  The second time I run the function I don't need that counter.
        Maybe ask Dana?
        TODO: return source file country name from source_id_Func instead of hard coding it
        in donor_file_Func to make my program more DRY
        TODO: return source file path from source_id_Func, instead of finding it again
        in append_files_Func to make my program more DRY'''
    return ()

def append_files_Func():
    '''TODO: fill out this function, replace example code with relevant information
    'f would be source file'
    f = open("bigfile.txt", "w")
    'tempfile would be the donor files'
    for tempfile in tempfiles:
        f.write(tempfile.read()
    return()'''

if __name__ == "__main__":
    source_id=''
    source_id=source_id_Func(source_id)
    donor_file_Func(source_id)


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

keys.append(str(file))
values.append(text_to_find[1])

'create dictionary to allow backfilling donor files with combined'
'source file data'
dictionary = dict(zip(keys, values))
print(dictionary)
'''
