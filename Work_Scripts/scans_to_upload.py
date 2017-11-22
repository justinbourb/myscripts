#scan_to_upload.py
#10/24/17 written by and copyright Justin Bourbonniere
'''moves files from upload folder
into Order#### folders based on the order numbers of files present in folder.
First checks if folder exists - if not create it then
move the files to the correct folder.
'''

import os
def createFoldersFunc():
	for dirpath, dirnames, filenames in os.walk('.'):
		for file in filenames:
			folderName = 'Order'+file.split('$')[0]
			'''create folders based on order number from files names'''
			try:
				folderName = int(folderName)
				if not os.path.exists(folderName):
					os.makedirs(folderName)
			except:
				continue
def moveFilesFunc():
	for dirpath, dirnames, filenames in os.walk('.'):
		for file in filenames:
			for folders in dirnames:
				#if order # from file == order # from the folders then move the file to the folder

				try:
					file_number = int(str(file)[0:4])
					folder_number=int(str(folders)[5:9])
					if file_number == folder_number:
						os.rename('I:/1UploadtoS3/'+file, folders+'/'+file)
				except:
					continue
	return()

upload_path=r'I:/1UploadtoS3'
os.chdir(upload_path)
createFoldersFunc()
moveFilesFunc()
