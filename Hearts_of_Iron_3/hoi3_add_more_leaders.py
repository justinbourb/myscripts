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

def oslistdir_and_match_text_Func(text_to_search):
        for file in os.listdir('.'):
            try:
                textfile = open(file, 'r')
                filetext = textfile.read()
                textfile.close()
                'find regex match (leader_id)'
                match = re.findall(text_to_search, filetext)
            except:
                    continue
        return(match,file)

def fileinput_replace_text_Func(text_to_search, text_to_replace):
    for file in os.listdir('.'):
        try:
            for line in fileinput.input(file, inplace=True):
                line = re.sub(text_to_search, text_to_replace, line.rstrip())
                print(line)
        except:
            continue
    return(file)

def source_id_Func(source_id,source_country,source_file):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\source"
    text_to_search = r"(\d{6} )"
    country_to_search = r"(country = [A-Z]{3})"
    'opens and reads file'
    os.chdir(path_to_search)
    match,file = oslistdir_and_match_text_Func(text_to_search)
    'returns last leader_id in source file'
    'can +1 this number to add new leaders'
    source_id = match[-1]
    match2 = oslistdir_and_match_text_Func(country_to_search)
    source_country = list(set(list(match2[0])))[0]
    source_file = file


    return (source_id, source_country, source_file)


def donor_file_Func(source_id,source_country,donor_files):
    'path and regex definitions'
    path_to_search = r"D:\Python36-32\MyScripts\test\donor"
    text_to_search = r"(\d{5,6} )"
    country_to_search = r"(country = )([A-Z]{3})"
    country_to_replace = source_country
    keys=[]
    values=[]
    source_id=int(source_id)
    source_id+=1
    line_counter=0

    'opens and reads file'
    os.chdir(path_to_search)
    for file in os.listdir('.'):
        try:
            for line in fileinput.input(file, inplace=True):
                text_to_replace = str(source_id)+" "
                new_line = re.sub(text_to_search, text_to_replace, line.rstrip())
                print(new_line)
                line_counter+=1
                if (line_counter % 10) == 0:
                    source_id+=1
                    line_counter=0


        except:
            continue
    file = fileinput_replace_text_Func(country_to_search,country_to_replace)
    donor_files = file
    return (donor_files)

def append_files_Func():
    '''TODO: refactor to make this dry, shouldn't hardcode path's.
    feed this function from donor and source functions'''
    source_file = open(r"D:\Python36-32\MyScripts\test\source\PER.txt", 'w')
    for file in os.listdir(r"D:\Python36-32\MyScripts\test\donor"):
        donor_file = open(file, 'r')
        source_file.write(donor_file.read())
        donor_file.close()
    source_file.close()
    return()


if __name__ == "__main__":
    source_id=''
    source_country=''
    source_file=''
    donor_files=''
    source_id,source_country,source_file=source_id_Func(source_id,source_country,source_file)
    donor_files = donor_file_Func(source_id,source_country, donor_files)
    append_files_Func()


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
