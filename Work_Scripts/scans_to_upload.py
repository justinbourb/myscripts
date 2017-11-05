#scan_to_upload.py
#10/24/17 written by and copyright Justin Bourbonniere
'''moves files from upload folder
into Order#### folders based on the order numbers of files present in folder.
First checks if folder exists - if not create it then
move the files to the correct folder.
'''

import os
def createFoldersFunc():
	os.chdir(r'/home/jb/myscripts/test_move')
	for dirpath, dirnames, filenames in os.walk('.'):
		for file in filenames:
			folderName = 'Order'+file.split('$')[0]
			'''create folders based on order number from files names'''
			if not os.path.exists(folderName):
				os.makedirs(folderName)
def moveFilesFunc():
	for dirpath, dirnames, filenames in os.walk('.'):
		for file in filenames:
			for folders in dirnames:
				'''if order # from file == order # from the folders then move the file to the folder'''
				if file.split('$')[0] == folders.split('r')[2]:
					os.rename('/home/jb/myscripts/test_move/'+file, folders+'/'+file)
createFoldersFunc()
moveFilesFunc()
				
			
