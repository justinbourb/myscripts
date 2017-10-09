#hoi3_increase_range.py
#10/8/17 written by and copyright Justin Bourbonniere
'''This program will open the files and increase the range = by 2/3'''
#reasoning: planes are useless, can't reach any targets
import os, sys, fileinput, re



'open files and increase range by 2/3'
def openFilesFunc():
    os.chdir(r'D:\Python36-32\MyScripts\test')
    for file in os.listdir('.'):
        try:
            print('file before regex:',file)
            'finds range'
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'need rangeInitial[2] to find the range'
            rangeInitial = re.search("(range = )(\d{3})?", filetext)
            print('rangeInitial:',rangeInitial)
            rangeInitial = str(rangeInitial[2])
            print('rangeInitial[2]:',rangeInitial)
            'increase rangeInital by 1/3 and removes .0 from rangeFinal'
            rangeFinal = str((int(rangeInitial)/3)+int(rangeInitial)).split('.')[0]
            
            with fileinput.FileInput(file, inplace=True) as file:
                for line in file:
                    print(line.replace(rangeInitial, rangeFinal), end='')
        except:
            continue


openFilesFunc()
