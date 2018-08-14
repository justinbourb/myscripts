#hoi3_add_more_leaders.py
#11/5/17 written by and copyright Justin Bourbonniere
'''This program will:
1)open the "copy_data_to" file and find the next leader_id to use and
the "copy_data_to" file country name
2) Open all the files in the "copy_data_from" directory.  Find and replace
their leader id #'s with the next leader_id number (next leader_id number
incremented +1 each time).  It will also update the country name from
whatever it is to the copy_data_to country name.
3) It will append the updated copy_data_from file to the copy_data_to file, thus adding
more leaders to the copy_data_to file (objective of the program).
4) Optional objective: backfill the copy_data_from files with the updated copy_data_to file content
but change the leader id's and country name to the copy_data_from file format.
TODO: make a dictionary to contain copy_data_from file: leader_id.  Can find both
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

def copy_data_to_id_Func(copy_data_to_id,copy_data_to_country,copy_data_to_fil, copy_data_to_path_to_search):
    'path and regex definitions'
    text_to_search = r"(\d{4,6} )"
    country_to_search = r"(country = [A-Z]{3})"
    'opens and reads file'
    os.chdir(copy_data_to_path_to_search)
    match,file = oslistdir_and_match_text_Func(text_to_search)
    'returns last leader_id in copy_data_to file'
    'can +1 this number to add new leaders'
    copy_data_to_id = match[-1]
    match2 = oslistdir_and_match_text_Func(country_to_search)
    copy_data_to_country = list(set(list(match2[0])))[0]
    copy_data_to_file = file


    return (copy_data_to_id, copy_data_to_country, copy_data_to_file)


def copy_data_from_file_Func(copy_data_to_id,copy_data_to_country,copy_data_from_files, copy_data_from_path_to_search):
    'path and regex definitions'
    text_to_search = r"(\d{5,6} )"
    country_to_search = r"(country = )([A-Z]{3})"
    country_to_replace = copy_data_to_country
    keys=[]
    values=[]
    copy_data_to_id=int(copy_data_to_id)
    copy_data_to_id+=1
    line_counter=0

    'opens and reads file'
    os.chdir(copy_data_from_path_to_search)
    for file in os.listdir('.'):
        try:
            for line in fileinput.input(file, inplace=True):
                text_to_replace = str(copy_data_to_id)+" "
                new_line = re.sub(text_to_search, text_to_replace, line.rstrip())
                print(new_line)
                line_counter+=1
                if (line_counter % 10) == 0:
                    copy_data_to_id+=1
                    line_counter=0


        except:
            continue
    file = fileinput_replace_text_Func(country_to_search,country_to_replace)
    copy_data_from_files = file
    return (copy_data_from_files)

def append_files_Func(copy_data_to_path_to_search, copy_data_from_path_to_search, copy_data_to_file):
    '''TODO: refactor to make this dry, shouldn't hardcode path's.
    feed this function from copy_data_from and copy_data_to functions'''
    file_to_open = copy_data_to_path_to_search+"\\"+copy_data_to_file
    copy_data_to_file = open(file_to_open, 'a')
    for file in os.listdir(copy_data_from_path_to_search):
        copy_data_from_file = open(file, 'r')
        copy_data_to_file.write(copy_data_from_file.read())
        copy_data_from_file.close()
    copy_data_to_file.close()
    return()


if __name__ == "__main__":
    '''declaring variables'''
    copy_data_to_id=''
    copy_data_to_country=''
    copy_data_to_file=''
    copy_data_from_files=''

    '''specify paths to search (copy to and from):'''
    copy_data_from_path_to_search = r"C:\Program Files\Python36\MyScripts\test\copy_data_from"
    copy_data_to_path_to_search = r"C:\Program Files\Python36\MyScripts\test\copy_data_to"

    '''functions to run'''
    copy_data_to_id,copy_data_to_country,copy_data_to_file=copy_data_to_id_Func(copy_data_to_id,copy_data_to_country,copy_data_to_file, copy_data_to_path_to_search)
    copy_data_from_files = copy_data_from_file_Func(copy_data_to_id,copy_data_to_country, copy_data_from_files, copy_data_from_path_to_search)
    append_files_Func(copy_data_to_path_to_search, copy_data_from_path_to_search, copy_data_to_file)


'''creates a list from the regex matches (leader_id)'
'from the copy_data_from file'
text_to_find = re.findall(text_to_search, filetext)
'removes duplicates from the list, sets do not have duplicates'
text_to_find = list(set(text_to_find))
'sorts the list, sets are not sorted'
text_to_find.sort()
'replaces the matched leader_id with next copy_data_to_id'
'TODO: write this to the file somehow?'
for i,s in enumerate(text_to_find):
    text_to_replace = str(copy_data_to_id)+" ="
    for line in fileinput.input(file, inplace=True):
        print line.replace(str(text_to_find[i])+" =",text_to_replace )
    copy_data_to_id+=1
'store values for dict creation'
keys.append(str(file))
values.append(text_to_find[1])
'create dictionary to allow backfilling copy_data_from files with combined'
'copy_data_to file data'
dictionary = dict(zip(keys, values))
print(dictionary)
'''

