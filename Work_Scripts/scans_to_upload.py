#scan_to_upload.py
#10/24/17 written by and copyright Justin Bourbonniere
#11/22/17 rewritten and/or refactored, previous version was poorly written and not working properly JB
'''moves files from upload folder
into Order#### folders based on the order numbers of files present in folder.
First checks if folder exists - if not create it then
move the files to the correct folder.
'''
import os, re


'this function finds any files when given a path'
def find_files_func(file_path):
        file_list=[]
        for file in os.listdir('.'):
                if os.path.isfile(file) == True:
                        file_list.append(file)
        return(file_list)

'this function creates folders, if not present based on file names'
def make_folders_func(file_list):
        folder_name_validation=''
        for index in file_list:
                'catches order ID from file names and validates it is a number'
                'validates 4 digit numbers'
                try:
                        folder_name_validation=int(index[:4])
                        folderName = 'Order'+index[:4]
                except:
                        'validates 3 digit numbers'
                        try:
                                folder_name_validation=int(index[:3])
                                folderName = 'Order'+index[:3]
                        except:
                                continue
                if not os.path.exists(folderName):
                        os.makedirs(folderName)
        return()

'this function moves the files'
def move_files_func(file_path, file_list):
        for index in file_list:
                'moves files with 4 digit order numbers'
                try:
                        os.rename(file_path+'/'+index, 'Order'+index[:4]+'/'+index)
                except:
                        'moves files with 3 digit order numbers'
                        try:
                                os.rename(file_path+'/'+index, 'Order'+index[:3]+'/'+index)
                        except:
                                continue
        return()
        
def main():
        file_path = r'I:/1UploadtoS3'
        file_list=[]        
        os.chdir(file_path)
        file_list=find_files_func(file_path)
        make_folders_func(file_list)
        move_files_func(file_path, file_list)
        
if __name__ == "__main__":
        main()
        
                

