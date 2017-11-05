#hoi3_decrease_air_attack.py
#10/8/17 written by and copyright Justin Bourbonniere
'''This program will open the files and increase the attack = by 2/3'''
#reasoning: planes are damaged too easily, ground units should not be able to damage planes
import os, sys, fileinput, re

'open files and decrease air attack to 0.1'
def openFilesFunc():
    os.chdir(r'D:\Python36-32\MyScripts\test')
    for file in os.listdir('.'):
        try:
            print('file before regex:',file)
            'finds attack'
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'need attackInitial[2] to find the attack'
            attackInitial = re.search("(air_attack = 0.)(\d{2})?", filetext)
            attackInitial = str(attackInitial[0])
            print(attackInitial)
            'replace attackInital with attackFinal'
            attackFinal = 'air_attack = 0.01'
            print(type(attackFinal))

            with fileinput.FileInput(file, inplace=True) as file:
                for line in file:
                    print(line.replace(attackInitial, attackFinal), end='')
        except:
            continue


openFilesFunc()
