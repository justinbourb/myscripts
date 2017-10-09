#hoi3_change_leader_start_date.py
#10/8/17 written by and wcopyright Justin Bourbonniere
'''This program will open all of the leader files in the
Hearts of Iron 3/history/leaders folder and change the text for
        history = {
                1930.1.1 = { rank = 1 }
                1940.1.1 = { rank = 0 }
        }
if the first line is not 1930.1.1 = { rank = 1 }, it will add it.'''
#reasoning: Hoi3 suffers from lack of leaders, increase # of leaders at the start
'''Secondary objective.  Find any lines with rank = 0 and remove them.'''
#reasoning: rank = 0 means the leader is not available (dies)
import os, sys, fileinput

'open all files in the directory and change rank 1 start to 1930'
def openFilesFunc():
    os.chdir(r'D:\Python36-32\MyScripts\test')
    years = ['1937','1938','1939','1940','1941','1942','1943','1944','1945','1946']
    for year in years:
        try:
            for file in os.listdir('.'):
                with fileinput.FileInput(file, inplace=True) as file:
                    for line in file:
                        print(line.replace(year+'.1.1 = { rank = 1 }', '1930.1.1 = { rank = 1 }'), end='')
        except:
            continue

openFilesFunc()
