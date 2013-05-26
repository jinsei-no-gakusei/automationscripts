#SWGA EMR Data Process-Martinez
import codecs
import os, string,sys
import pyodbc
import csv

'''Script to write '''


lfiles = os.listdir(r"E:\MyData\SW\E_PData") 
nfiles = os.listdir(r"E:\MyData\SW\E_PData")
a = ('SW.csv') #name of new file to be written into 

"""Checks directory for existing file with same name and deletes it"""
for n in lfiles:
    local_filename = os.path.join(r"E:\MyData\SW\E_PData",n)
    global a
    n_file = os.path.join(r"E:\MyData\SW\E_PData",a) 
    
	#check path to see if a file with same name exists
	#if such file exists then delete it 
    if os.path.exists(n_file):
        try:
            print n_file
            os.remove(n_file)
        except:
            print "Exception: ",str(sys.exc_info())
			
    else:
        print 'File not found at Directory'

lfiles = os.listdir(r"E:\MyData\SW\E_PData") 
nfiles = os.listdir(r"E:\MyData\SW\E_PData")
a = ('SWGA_EMR_Data.csv') #name of new file to be written into

"""Read csv file,fill empty cells in first column with name of the preceding cell and then remove last row""" 		
for n in lfiles:
    
    local_filename = os.path.join(r"E:\MyData\SW\E_PData",n)
    global a
    n_file = os.path.join(r"E:\MyData\SW\E_PData",a) 
    ifile  = open(local_filename, "rb")
    reader = csv.reader(ifile)

    ofile = open(os.path.join(r"E:\MyData\SW\E_PData",a), "wb")
    writer = csv.writer(ofile, delimiter=',', quotechar='|',quoting=csv.QUOTE_ALL)
    Break = False
    for row in reader:
        for char in row[0]:
            try:
                int(char)
                Break = True
            except:
                pass     #to remove the last row which is un-wanted
			
        if Break:
            row = ''
            break
        if row[0] != '':
            prev = row[0] #if the row is not empty then assign value of that row to prev
        
        if row[0] == '':
            row[0] = prev
            #writer.writerow(row) #if the row of the first column is empty then assign the value of prev to that row
         
        writer.writerow(row) # now write everything into the new file kapish!
		
ifile.close()
ofile.close()