import openpyxl, docx, os
'''concept: Dr. Bronson submitted a report in word format,
but the customer wants it in excel.
problem: this is tedious to to manually.
solution: lets do it in python.
6/27/17'''

'''TODO: open excel file, open word file.  Find all samples names in a column
on excel, match them to list from word.

for cell in range(1,maxcolumns()):
    if cell == lookup cell in word:
        copy word for each sample letter
        ***question: does each sample have the same number of sample letters?
        ***Find this out by counting columns between sample names?
        past word info into correct excel cell
        ***find correct excel cell from word documnent?'''

'''TODO: change directory to find excel sheet'''
############part 1 - find excel info ###################
#opens excel WB
wb=openpyxl.load_workbook('2017-05-10_Histowiz 3rd Batch.xlsx')
#opens sheet of excel WB
sheet=wb.get_sheet_by_name('Histowiz_SFA_aging')
#finds max row, needed for range to sort through data
max_row=sheet.max_row+1
#add A to max row
max_row='A'+(str(max_row))
#define column1 list
column1=[]
#make list of sample names from column 1
for cellObj in sheet.column[1]:
    #skips over blank cells
    if cellObj!='NULL':
        #appends each cell with a value into column1 list
        column1=column1.append(cellObj)
print(column1)

#########part 2 - find word document info ###############
doc = docx.Document('Histowiz Order 2658')

#loops over samples from excel
for sample in column1:
    #loops over samples in word
    for para in doc.paragraphs:
        #if word sample == excel sample
        if para == sample:
'''TODO: how to get data from word to excel?  Can I locate paragraph
# of para? loop until blankspace?'''
