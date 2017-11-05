#hoi3_decrease_build_cost_ic.py
#10/21/17 written by and copyright Justin Bourbonniere
'''This program will open the files and decrease build_cost_IC by 1/2'''
#reasoning: planes are useless, reduce IC cost
import os, sys, fileinput, re



'open files and 1/2 build_cost_ic'
def openFilesFunc():
    os.chdir(r'D:\Python36-32\MyScripts\test')
    for file in os.listdir('.'):
        try:
            print('file before regex:',file)
            'finds build_cost_ic'
            textfile = open(file, 'r')
            filetext = textfile.read()
            textfile.close()
            'need icInitial[2] to find the range'
            icInitial = re.search("(build_cost_ic = )(\d{1,2})?", filetext)
            print(icInitial[0],'regex[1]:',icInitial[1],' regex[2]:',icInitial[2])
            icInitial = str(icInitial[2])
            
            '1/2 icInitial and removes .0 from rangeFinal'
            icFinal = str((int(icInitial)/2)).split('.')[0]
            with fileinput.FileInput(file, inplace=True) as file:
                for line in file:
                    print(line.replace(icInitial, icFinal), end='')
        except:
            continue


openFilesFunc()
