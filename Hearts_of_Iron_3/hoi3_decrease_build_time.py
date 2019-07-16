#hoi3_increase_range.py
#7/15/19 written by and copyright Justin Bourbonniere
'''This program will open the files and decrease build time 3/5'''
#reasoning: ships take too long to build
import os, sys, fileinput, re



'open files and increase range by 2/3'
def openFilesFunc():
    os.chdir(r'C:\test')
    for file in os.listdir('.'):
        try:
            print('file before regex:',file)
            'finds range'
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'need rangeInitial[2] to find the range'
            buildTimeInitial = re.search("(build_time = )(\d{3})?", filetext)
            buildTimeInitial = str(buildTimeInitial[2])
            print('buildTimeInitial[2]:',buildTimeInitial)
            'decrease buildTimeInital by 3/5 and removes .0 from rangeFinal'
            buildTimeFinal = str((int(buildTimeInitial)*3/5)).split('.')[0]
            print(buildTimeFinal)
            
            with fileinput.FileInput(file, inplace=True) as file:
                for line in file:
                    print(line.replace(buildTimeInitial, buildTimeFinal), end='')
        except:
            continue


openFilesFunc()
