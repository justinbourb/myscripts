'''scan_to_upload.py moves .svs files from upload folder
into Order#### folders based on the order numbers of files present in folder.
If the folder exists - move the files.  If no folder exists - create it then
move the files

This is a remake of an already working program that was lost due to
laptop hard drive failure'''


#TODO: regex to find files
#(/n/n/n/n)(.*).svs

#TODO: create folders
#order number = regex(1)
#if not folder Order%s, %order number
#create folder Order%s, %order number

#TODO: moves files to folder
#for files in folder
#if Order#### = ####.svs
#move file to folder
